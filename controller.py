import sys
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME
import logging
from datetime import datetime, timezone, timedelta
from ariadne import QueryType
from models import *

query = QueryType()
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
    bus_stop = BusStop()
    result = [models.Busstop(stop['id'], stop['bus_stop_id'], stop['bus_stop_name'], stop['lat'], stop['lon']) for stop in bus_stop.get()]
    return result

def get_busstop(stop_id):
    bus_stop = BusStop()
    query_result = bus_stop.get_by_id(stop_id)
    result = models.Busstop(
        query_result['id'],
        query_result['bus_stop_id'],
        query_result['name'],
        query_result['lat'],
        query_result['lon']
    )
    return result

def get_busstop_weather(stop_id):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT bus_stop_id, TIMESTAMP(DATE(ts), (HOUR(ts))*10000) AS d, AVG(value), sensor
            FROM weather 
            WHERE bus_stop_id=%s AND sensor="temperature"
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
            SELECT bus_stop_id, TIMESTAMP(DATE(ts), (HOUR(ts))*10000) AS d, AVG(value), sensor
            FROM weather 
            WHERE bus_stop_id=%s AND sensor="pm25"
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
            SELECT bus_stop_id, TIMESTAMP(DATE(ts), (HOUR(ts))*10000) AS d, AVG(value), sensor
            FROM weather 
            WHERE bus_stop_id=%s AND sensor="pm25"
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
            WHERE r1.bus_number=r2.bus_number AND r1.bus_stop_id=%s AND r2.bus_stop_id=%s
        """, [stop_id_origin, stop_id_dest])
        logging.info("Returning result...")
        result = [models.Route(*row) for row in cs.fetchall()]
        return result

def get_bus_route(bus_id):
    logging.info("Connecting to database...")
    with pool.connection() as conn, conn.cursor() as cs:
        logging.info("Executing query...")
        cs.execute("""
            SELECT DISTINCT bus_number, bus_stop_id
            FROM route
            WHERE bus_number=%s
        """, [bus_id])
        logging.info("Returning result...")
        busstops = [number for (_, number) in cs.fetchall()]
        return models.Bus(bus_id, busstops)

def put_population(stop_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            INSERT INTO population (ts, bus_stop_id)
            VALUES (
                %s, %s
            )
        """, [datetime.now(th_timezone), stop_id])
        conn.commit()
    return "Success"

def get_population(stop_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT TIMESTAMP(DATE(ts), (HOUR(ts)*10000) + ((MINUTE(ts) DIV 30)*30*100)) AS d, COUNT(*), bus_stop_id
            FROM population
            WHERE bus_stop_id=%s
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

@query.field("busstops")
def busstops_resolver(_, info):
    return get_busstops()

@query.field("busstop")
def busstop_resolver(_, info, stopId):
    return get_busstop(stopId)

@query.field("bus")
def get_takable_bus_resolver(_, info, stopIdDest, stopIdOrigin):
    return get_takable_bus(stopIdOrigin, stopIdDest)

@query.field("bus2")
def get_bus_resolver(_, info, busId):
    return get_bus_route(busId)

@query.field("busstopAqi")
def get_aqi_resolver(_, info, stopId):
    return get_busstop_aqi(stopId)

@query.field("busstopHumidity")
def get_humidity_resolver(_, info, stopId):
    return get_busstop_humidity(stopId)

@query.field("busstopTemperature")
def get_temperature_resolver(_, info, stopId):
    return get_busstop_weather(stopId)

@query.field("population")
def get_population_resolver(_, info, stopId):
    return get_population(stopId)

@query.field("routes")
def get_routes_resolver(_, info):
    return get_routes()
