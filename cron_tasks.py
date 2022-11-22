from controller import get_busstops
import pymysql
from dbutils.pooled_db import PooledDB
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
import requests
import os
from dotenv import load_dotenv
load_dotenv()

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

def weather_open_meteo():
    results = get_busstops()
    if results:
        for result in results:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={result.lat}&longitude={result.lon}&current_weather=true")
            data = response.json()
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    INSERT INTO open_meteo (bus_stop_id, temperature, windspeed)
                    VALUES (
                        %s, %s, %s
                    )
                """, [result.busstop_id, data['current_weather']['temperature'], data['current_weather']['windspeed']])
                conn.commit()

def pm25_aqicn():
    results = get_busstops()
    if results:
        for result in results:
            response = requests.get(f"http://api.waqi.info/feed/geo:{result.lat};{result.lon}/?token={os.getenv('AQICN_TOKEN')}")
            data = response.json()
            with pool.connection() as conn, conn.cursor() as cs:
                cs.execute("""
                    INSERT INTO aqi (bus_stop_id, value)
                    VALUES (
                        %s, %s
                    )
                """, [result.busstop_id, data['data']['aqi']])
                conn.commit()

if __name__ == '__main__':
    try:
        weather_open_meteo()
    except:
        print("Retrieve data from Open meteo error...")
    try:
        pm25_aqicn()
    except:
        print("Retireve data from AQICN error...")
