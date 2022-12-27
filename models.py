from database import Database
from decimal import Decimal
import logging
from boto3.dynamodb.conditions import Key
import uuid
from datetime import datetime, timezone, timedelta

logger = logging.getLogger(__name__)
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

class BusStop(Database):
    """Encapsulates an Amazon DynamoDB table of busstop data."""
    def __init__(self):
        super().__init__("bus_stop")
    
    def create(self, bus_stop_id: str, bus_stop_name: str, lat: float, lon: float, verified = False):
        """
        Adds a bus stop to the table.

        :param bus_stop_id: The ID of bus stop.
        :param bus_stop_name: The name of bus stop.
        :param lat: The latitude of bus stop.
        :param lon: The longitude of the bus stop.
        :param verified: Is bus stop data verified?.
        """
        items = {
            'id': uuid.uuid4().hex,
            'bus_stop_id': bus_stop_id,
            'bus_stop_name': bus_stop_name,
            'lat': Decimal(str(lat)),
            'lon': Decimal(str(lon)),
            'verified': bool(verified)
        }
        super().create(items)
    
    def get_by_id(self, id):
        return super().getByField({"id": id})


class OpenMeteo(Database):
    """Encapsulates an Amazon DynamoDB table of busstop data."""
    def __init__(self):
        super().__init__("open_meteo")
    
    def create(self, bus_stop_id: str, temperature: float, windspeed: float, ts = datetime.now(timezone(timedelta(hours=7)))):
        """
        Adds a bus stop to the table.

        :param bus_stop_id: The Bus stop ID of bus stop.
        :param temperature: The temperature of bus stop at the time.
        :param windspeed: The windspeed of the bus stop at the time.
        :param ts: timestamp of record.
        """
        items = {
            'id': uuid.uuid4().hex,
            'ts': ts.strftime(TIME_FORMAT),
            'bus_stop_id': bus_stop_id,
            'temperature': Decimal(str(temperature)),
            'windspeed': Decimal(str(windspeed))
        }
        super().create(items)

class AqiCn(Database):
    """Encapsulates an Amazon DynamoDB table of busstop data."""
    def __init__(self):
        super().__init__("aqicn")
    
    def create(self, bus_stop_id: str, value: float, ts = datetime.now(timezone(timedelta(hours=7)))):
        """
        Adds a bus stop to the table.

        :param bus_stop_id: The Bus stop ID of bus stop.
        :param value: The PM2.5 value of the bus stop at the time.
        :param ts: timestamp of record.
        """
        items = {
            'id': uuid.uuid4().hex,
            'ts': ts.strftime(TIME_FORMAT),
            'bus_stop_id': bus_stop_id,
            'value': Decimal(str(value))
        }
        super().create(items)

class IqAir(Database):
    """Encapsulates an Amazon DynamoDB table of busstop data."""
    def __init__(self):
        super().__init__("iqair")
    
    def create(self, bus_stop_id: str, temperature: float, humidity: float, windspeed: float, pm25: float, ts = datetime.now(timezone(timedelta(hours=7)))):
        """
        Adds a bus stop to the table.

        :param bus_stop_id: The Bus stop ID of bus stop.
        :param temperature: The temperature of the bus stop at the time.
        :param humidity: The humidity of the bus stop at the time.
        :param windspeed: The windspeed of the bus stop at the time.
        :param pm25: The PM2.5 value of the bus stop at the time.
        :param ts: timestamp of record.
        """
        items = {
            'id': uuid.uuid4().hex,
            'ts': ts.strftime(TIME_FORMAT),
            'bus_stop_id': bus_stop_id,
            'temperature': Decimal(str(temperature)),
            'humidity': Decimal(str(humidity)),
            'windspeed': Decimal(str(windspeed)),
            'pm25': Decimal(str(pm25))
        }
        super().create(items)

class Population(Database):
    """Encapsulates an Amazon DynamoDB table of busstop data."""
    def __init__(self):
        super().__init__("population")
    
    def create(self, bus_stop_id: str, ts = datetime.now(timezone(timedelta(hours=7)))):
        """
        Adds a bus stop to the table.

        :param bus_stop_id: The Bus stop ID of bus stop.
        :param ts: timestamp of record.
        """
        items = {
            'id': uuid.uuid4().hex,
            'ts': ts.strftime(TIME_FORMAT),
            'bus_stop_id': bus_stop_id,
        }
        super().create(items)

class Weather(Database):
    """Encapsulates an Amazon DynamoDB table of busstop data."""
    def __init__(self):
        super().__init__("weather")
    
    def create(self, bus_stop_id: str, sensor: str, source: str, value: float, ts = datetime.now(timezone(timedelta(hours=7)))):
        """
        Adds a bus stop to the table.

        :param bus_stop_id: The Bus stop ID of bus stop.
        :param sensor: The sensor obtained the value.
        :param source: The source obtained the value.
        :param value: The weather value of the bus stop at the time.
        :param ts: timestamp of record.
        """
        items = {
            'id': uuid.uuid4().hex,
            'ts': ts.strftime(TIME_FORMAT),
            'bus_stop_id': bus_stop_id,
            'sensor': sensor,
            'source': source,
            'value': Decimal(str(value))
        }
        super().create(items)
