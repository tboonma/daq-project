# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.busstop import Busstop  # noqa: E501
from openapi_server.models.busstop_weather import BusstopWeather  # noqa: E501
from openapi_server.models.route import Route  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_bus_route(self):
        """Test case for controller_get_bus_route

        Returns all bus stops for given route
        """
        headers = { 
        }
        response = self.client.open(
            '/talai-api/v1/route/{bus_id}'.format(bus_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_buses(self):
        """Test case for controller_get_buses

        Returns all KU Talai bus number
        """
        headers = { 
        }
        response = self.client.open(
            '/talai-api/v1/buses',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_busstop(self):
        """Test case for controller_get_busstop

        Returns complete details of the specified Talai bus stop
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/talai-api/v1/busstop/{stop_id}'.format(stop_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_busstop_weather(self):
        """Test case for controller_get_busstop_weather

        Returns weather detail of the specified Talai bus stop
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/talai-api/v1/busstop/{stop_id}/weather'.format(stop_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_busstops(self):
        """Test case for controller_get_busstops

        Returns list of Talai bus stops in KU
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/talai-api/v1/busstops',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_population(self):
        """Test case for controller_get_population

        Get population density in each KU Talai bus
        """
        headers = { 
        }
        response = self.client.open(
            '/talai-api/v1/population/{stop_id}'.format(stop_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_routes(self):
        """Test case for controller_get_routes

        Returns a list of routes of KU Talai bus
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/talai-api/v1/routes',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_takable_bus(self):
        """Test case for controller_get_takable_bus

        Returns list of takable bus from origin to destination
        """
        headers = { 
        }
        response = self.client.open(
            '/talai-api/v1/bus/{stop_id_origin}/{stop_id_dest}'.format(stop_id_origin=56, stop_id_dest=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_put_population(self):
        """Test case for controller_put_population

        Increment people in KU Talai bus stop
        """
        headers = { 
        }
        response = self.client.open(
            '/talai-api/v1/population/{stop_id}'.format(stop_id=56),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
