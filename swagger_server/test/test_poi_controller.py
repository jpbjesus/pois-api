# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.poi import POI  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPoiController(BaseTestCase):
    """PoiController integration test stubs"""

    def test_delete_poi(self):
        """Test case for delete_poi

        Deletes a POI
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/{poiId}'.format(poiId=789),
            method='DELETE',
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_poi(self):
        """Test case for post_poi

        Add a new POI to the database
        """
        body = POI()
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_poi(self):
        """Test case for put_poi

        Update an existing POI
        """
        body = POI()
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
