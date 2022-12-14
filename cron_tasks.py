from controller import get_busstops
import pymysql
from dbutils.pooled_db import PooledDB
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
import requests
import os
import sys
from time import sleep
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import random
from models import *

th_timezone = timezone(timedelta(hours=7))
load_dotenv()

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

print(f"MySQL: {DB_USER}@{DB_HOST}")

def weather_open_meteo():
    print("[Open-Meteo] Getting all busstop...")
    results = get_busstops()
    open_meteo = OpenMeteo()
    if results:
        for result in results:
            print(f"[Open-Meteo] Getting weather data for {result.name}...")
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={result.lat}&longitude={result.lon}&current_weather=true")
            data = response.json()
            print(f"[Open-Meteo] Inserting weather data for {result.name}...")
            open_meteo.create(result.busstop_id, data['current_weather']['temperature'], data['current_weather']['windspeed'])
            print(f"[Open-Meteo] {result.name} weather data inserted...")

def pm25_aqicn():
    print("[AQICN] Getting all busstop...")
    results = get_busstops()
    if results:
        for result in results:
            print(f"[AQICN] Getting weather data for {result.name}...")
            response = requests.get(f"http://api.waqi.info/feed/geo:{result.lat};{result.lon}/?token={os.getenv('AQICN_TOKEN')}")
            data = response.json()
            print(data)
            print(f"[AQICN] Inserting weather data for {result.name}...")
            aqicn = AqiCn()
            aqicn.create(result.busstop_id, data['data']['aqi'])
            print(f"[AQICN] {result.name} weather data inserted...")

def iqair():
    print("[IQAir] Getting all busstop...")
    results = get_busstops()
    if results:
        for result in results:
            print(f"[IQAir] Getting weather data for {result.name}...")
            response = requests.get(f"http://api.airvisual.com/v2/nearest_city?lat={result.lat}&lon={result.lon}&key={os.getenv('IQAIR_TOKEN')}")
            data = response.json()
            print(data)
            print(f"[IQAir] Inserting weather data for {result.name}...")
            iqair = IqAir()
            iqair.create(
                result.busstop_id,
                data['data']['current']['weather']['tp'],
                data['data']['current']['weather']['hu'],
                data['data']['current']['weather']['ws'],
                data['data']['current']['pollution']['aqius']
            )
            print(f"[IQAir] {result.name} weather data inserted...")
            sleep(20)

def generate_population():
    if datetime.now(th_timezone).hour >= 17 or datetime.now(th_timezone).hour <= 7:
        sys.exit(0)
    print("[Population] Getting all busstop...")
    results = get_busstops()
    if results:
        for result in results:
            print(f"[Population] Generating population for {result.name}...")
            people = random.randint(0, 3)
            if people == 0:
                continue
            print(f"[Population] Inserting {people} population for {result.name}...")
            for _ in range(people):
                ppl = Population()
                ppl.create(result.busstop_id)
            print(f"[Population] {result.name} population inserted...")


def integrate_data():
    print("[Integrate] Getting IQAir weather information...")
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT bus_stop_id, AVG(temperature) AS temperature, AVG(pm25_value) AS pm25, AVG(humidity) AS humidity, AVG(wind_speed) AS wind_speed
            FROM iqair
            WHERE `ts` > NOW() - INTERVAL 2 HOUR
            GROUP BY bus_stop_id
        """)
        for data in cs.fetchall():
            busstop_id, temperature, pm25, humidity, wind_speed = data
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'temperature', 'iqair', %s
                )
            """, [busstop_id, datetime.now(th_timezone), temperature])
            conn.commit()
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'pm25', 'iqair', %s
                )
            """, [busstop_id, datetime.now(th_timezone), pm25])
            conn.commit()
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'humidity', 'iqair', %s
                )
            """, [busstop_id, datetime.now(th_timezone), humidity])
            conn.commit()
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'windspeed', 'iqair', %s
                )
            """, [busstop_id, datetime.now(th_timezone), wind_speed])
            conn.commit()
    print("[Integrate] Getting AQICN weather information...")
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT bus_stop_id, AVG(value) AS pm25
            FROM aqi
            WHERE `ts` > NOW() - INTERVAL 2 HOUR
            GROUP BY bus_stop_id
        """)
        for data in cs.fetchall():
            busstop_id, pm25 = data
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'pm25', 'aqi', %s
                )
            """, [busstop_id, datetime.now(th_timezone), pm25])
            conn.commit()
    print("[Integrate] Getting Open Meteo weather information...")
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT bus_stop_id, AVG(temperature) AS temperature, AVG(windspeed) AS windspeed
            FROM open_meteo
            WHERE `ts` > NOW() - INTERVAL 2 HOUR
            GROUP BY bus_stop_id
        """)
        for data in cs.fetchall():
            busstop_id, temperature, wind_speed = data
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'temperature', 'open_meteo', %s
                )
            """, [busstop_id, datetime.now(th_timezone), temperature])
            conn.commit()
            cs.execute("""
                INSERT into weather (bus_stop_id, ts, sensor, source, value)
                VALUES (
                    %s, %s, 'windspeed', 'open_meteo', %s
                )
            """, [busstop_id, datetime.now(th_timezone), wind_speed])
            conn.commit()


if __name__ == '__main__':
    if sys.argv[1] != None:
        globals()[sys.argv[1]]()
    else:
        try:
            weather_open_meteo()
        except:
            print("Retrieve data from Open meteo error...")
        try:
            pm25_aqicn()
        except:
            print("Retireve data from AQICN error...")
        try:
            iqair()
        except:
            print("Retireve data from IQAir error...")
