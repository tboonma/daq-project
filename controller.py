import sys
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME
import logging
from datetime import datetime, timezone, timedelta

th_timezone = timezone(timedelta(hours=7))

sys.path.append(OPENAPI_STUB_DIR)
from openapi_server import models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)


def get_busstops():
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT id, bus_stop_id, bus_stop_name, lat, lon
            FROM bus_stop
        """)
        logging.info("Returning result...")
        result = [models.Busstop(*row) for row in cs.fetchall()]
        return result

def get_busstop(stop_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, bus_stop_id, bus_stop_name, lat, lon
            FROM bus_stop
            WHERE id=%s
        """, [stop_id])
        result = cs.fetchone()
        if result:
            return models.Busstop(*result)

def get_busstop_weather(stop_id):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT id, TIMESTAMP(DATE(ts), (HOUR(ts))*10000) AS d, AVG(value), sensor
            FROM weather 
            WHERE id=%s AND sensor="temperature"
            GROUP BY d
        """, [stop_id])
        logging.info("Returning result...")
        result = [models.BusstopWeather(*row) for row in cs.fetchall()]
        return result

def get_busstop_aqi(stop_id):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT id, TIMESTAMP(DATE(ts), (HOUR(ts))*10000) AS d, AVG(value), sensor
            FROM weather 
            WHERE id=%s AND sensor="pm25"
            GROUP BY d
        """, [stop_id])
        logging.info("Returning result...")
        result = [models.BusstopWeather(*row) for row in cs.fetchall()]
        return result

def get_busstop_humidity(stop_id):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT id, TIMESTAMP(DATE(ts), (HOUR(ts))*10000) AS d, AVG(value), sensor
            FROM weather 
            WHERE id=%s AND sensor="pm25"
            GROUP BY d
        """, [stop_id])
        logging.info("Returning result...")
        result = [models.BusstopWeather(*row) for row in cs.fetchall()]
        return result

def get_routes():
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT DISTINCT bus_number
            FROM route
        """)
        logging.info("Returning result...")
        result = [models.Route(*row) for row in cs.fetchall()]
        return result

def get_takable_bus(stop_id_origin, stop_id_dest):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT DISTINCT r1.bus_number
            FROM route r1
            INNER JOIN route r2
            WHERE r1.bus_number=r2.bus_number AND r1.id=%s AND r2.id=%s
        """, [stop_id_origin, stop_id_dest])
        logging.info("Returning result...")
        result = [models.Route(*row) for row in cs.fetchall()]
        return result

def get_bus_route(bus_id):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT DISTINCT bus_number, id
            FROM route
            WHERE bus_number=%s
        """, [bus_id])
        logging.info("Returning result...")
        busstops = [number for (_, number) in cs.fetchall()]
        return models.Bus(bus_id, busstops)

def put_population(stop_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            INSERT INTO population (ts, id)
            VALUES (
                %s, %s
            )
        """, [datetime.now(th_timezone), stop_id])
        conn.commit()
    return "Success"

def get_population(stop_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT TIMESTAMP(DATE(ts), (HOUR(ts)*10000) + ((MINUTE(ts) DIV 30)*30*100)) AS d, COUNT(*), id
            FROM population
            WHERE id=%s
            GROUP BY d
        """, [stop_id])
        previous_timestamp = None
        result = []
        for (timestamp, amount, _) in cs.fetchall():
            if previous_timestamp:
                while True:
                    timediff = timestamp - previous_timestamp
                    if (timediff.total_seconds()/60 > 31):
                        previous_timestamp += timedelta(minutes=30)
                        result.append(models.PopulationDensity(previous_timestamp, 0))
                    else:
                        break
            result.append(models.PopulationDensity(timestamp, amount))
            previous_timestamp = timestamp
        return result
