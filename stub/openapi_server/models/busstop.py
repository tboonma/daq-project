# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Busstop(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, busstop_id=None, name=None, lat=None, lon=None):  # noqa: E501
        """Busstop - a model defined in OpenAPI

        :param busstop_id: The busstop_id of this Busstop.  # noqa: E501
        :type busstop_id: int
        :param name: The name of this Busstop.  # noqa: E501
        :type name: str
        :param lat: The lat of this Busstop.  # noqa: E501
        :type lat: float
        :param lon: The lon of this Busstop.  # noqa: E501
        :type lon: float
        """
        self.openapi_types = {
            'busstop_id': int,
            'name': str,
            'lat': float,
            'lon': float
        }

        self.attribute_map = {
            'busstop_id': 'busstopId',
            'name': 'name',
            'lat': 'lat',
            'lon': 'lon'
        }

        self._busstop_id = busstop_id
        self._name = name
        self._lat = lat
        self._lon = lon

    @classmethod
    def from_dict(cls, dikt) -> 'Busstop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Busstop of this Busstop.  # noqa: E501
        :rtype: Busstop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def busstop_id(self):
        """Gets the busstop_id of this Busstop.


        :return: The busstop_id of this Busstop.
        :rtype: int
        """
        return self._busstop_id

    @busstop_id.setter
    def busstop_id(self, busstop_id):
        """Sets the busstop_id of this Busstop.


        :param busstop_id: The busstop_id of this Busstop.
        :type busstop_id: int
        """

        self._busstop_id = busstop_id

    @property
    def name(self):
        """Gets the name of this Busstop.


        :return: The name of this Busstop.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Busstop.


        :param name: The name of this Busstop.
        :type name: str
        """

        self._name = name

    @property
    def lat(self):
        """Gets the lat of this Busstop.


        :return: The lat of this Busstop.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Busstop.


        :param lat: The lat of this Busstop.
        :type lat: float
        """

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Busstop.


        :return: The lon of this Busstop.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Busstop.


        :param lon: The lon of this Busstop.
        :type lon: float
        """

        self._lon = lon