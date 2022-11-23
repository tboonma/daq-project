import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

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
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT bus_stop_id, bus_stop_name, lat, lon
            FROM bus_stop
        """)
        result = [models.Busstop(*row) for row in cs.fetchall()]
        return result

def get_busstop(stop_id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT bus_stop_id, bus_stop_name, lat, lon
            FROM bus_stop
            WHERE bus_stop_id=%s
        """, [stop_id])
        result = cs.fetchone()
        if result:
            return models.Busstop(*result)

def get_busstop_weather(stop_id):
    return "Doing something"

def get_routes():
    return "Doing something"

def get_takable_bus(stop_id_origin, stop_id_dest):
    return "Doing something"

def get_bus_route(bus_id):
    return "Doing something"

def get_buses():
    return "Doing something"

def put_population():
    return "Doing something"

def get_population():
    return "Doing something"