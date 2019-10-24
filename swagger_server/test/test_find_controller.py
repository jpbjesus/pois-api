# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.poi import POI  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFindController(BaseTestCase):
    """FindController integration test stubs"""

    def test_get_by_id(self):
        """Test case for get_by_id

        Find POI by ID
        """
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/{poiId}'.format(poiId=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_by_name_or_geocode(self):
        """Test case for get_by_name_or_geocode

        Returns an array of POIs
        """
        query_string = [('name', 'name_example'),
                        ('lat', 'lat_example'),
                        ('long', 'long_example'),
                        ('radius', 789)]
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/find',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_type(self):
        """Test case for get_type

        Find POIs by type
        """
        query_string = [('type', 'type_example'),
                        ('lat', 'lat_example'),
                        ('long', 'long_example'),
                        ('radius', 789)]
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/type',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
