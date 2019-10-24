# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReviewsController(BaseTestCase):
    """ReviewsController integration test stubs"""

    def test_poi_poi_id_put(self):
        """Test case for poi_poi_id_put

        Update rating from one POI
        """
        query_string = [('upOrDown', true)]
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/{poiId}'.format(poiId=789),
            method='PUT',
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_review(self):
        """Test case for post_review

        Uploads an text review
        """
        data = dict(review='review_example')
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/{poiId}/review'.format(poiId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
