import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.bus import Bus  # noqa: E501
from openapi_server.models.busstop import Busstop  # noqa: E501
from openapi_server.models.busstop_weather import BusstopWeather  # noqa: E501
from openapi_server.models.population_density import PopulationDensity  # noqa: E501
from openapi_server.models.route import Route  # noqa: E501
from openapi_server import util


def controller_get_bus_route(bus_id):  # noqa: E501
    """Returns all bus stops for given route

     # noqa: E501

    :param bus_id: 
    :type bus_id: int

    :rtype: Union[Bus, Tuple[Bus, int], Tuple[Bus, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_busstop(stop_id):  # noqa: E501
    """Returns complete details of the specified Talai bus stop

     # noqa: E501

    :param stop_id: 
    :type stop_id: int

    :rtype: Union[Busstop, Tuple[Busstop, int], Tuple[Busstop, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_busstop_aqi(stop_id):  # noqa: E501
    """Returns PM2.5 detail of the specified Talai bus stop

     # noqa: E501

    :param stop_id: 
    :type stop_id: int

    :rtype: Union[List[BusstopWeather], Tuple[List[BusstopWeather], int], Tuple[List[BusstopWeather], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_busstop_humidity(stop_id):  # noqa: E501
    """Returns humidity detail of the specified Talai bus stop

     # noqa: E501

    :param stop_id: 
    :type stop_id: int

    :rtype: Union[List[BusstopWeather], Tuple[List[BusstopWeather], int], Tuple[List[BusstopWeather], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_busstop_weather(stop_id):  # noqa: E501
    """Returns weather detail of the specified Talai bus stop

     # noqa: E501

    :param stop_id: 
    :type stop_id: int

    :rtype: Union[List[BusstopWeather], Tuple[List[BusstopWeather], int], Tuple[List[BusstopWeather], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_busstops():  # noqa: E501
    """Returns list of Talai bus stops in KU

     # noqa: E501


    :rtype: Union[List[Busstop], Tuple[List[Busstop], int], Tuple[List[Busstop], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_population(stop_id):  # noqa: E501
    """Get population density in each KU Talai bus

     # noqa: E501

    :param stop_id: 
    :type stop_id: int

    :rtype: Union[List[PopulationDensity], Tuple[List[PopulationDensity], int], Tuple[List[PopulationDensity], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_routes():  # noqa: E501
    """Returns a list of routes of KU Talai bus

     # noqa: E501


    :rtype: Union[List[Route], Tuple[List[Route], int], Tuple[List[Route], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_takable_bus(stop_id_origin, stop_id_dest):  # noqa: E501
    """Returns list of takable bus from origin to destination

     # noqa: E501

    :param stop_id_origin: 
    :type stop_id_origin: int
    :param stop_id_dest: 
    :type stop_id_dest: int

    :rtype: Union[List[Route], Tuple[List[Route], int], Tuple[List[Route], int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_put_population(stop_id):  # noqa: E501
    """Increment people in KU Talai bus stop

     # noqa: E501

    :param stop_id: 
    :type stop_id: int

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return 'do some magic!'
