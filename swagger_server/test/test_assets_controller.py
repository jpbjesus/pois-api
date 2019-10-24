# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAssetsController(BaseTestCase):
    """AssetsController integration test stubs"""

    def test_post_image(self):
        """Test case for post_image

        Uploads an image
        """
        data = dict(upfile1=(BytesIO(b'some file data'), 'file.txt'),
                    upfile2=(BytesIO(b'some file data'), 'file.txt'),
                    upfile3=(BytesIO(b'some file data'), 'file.txt'),
                    note='note_example')
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/{poiId}/image'.format(poiId=789),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_tag(self):
        """Test case for post_tag

        Uploads an tag to describe POI
        """
        data = dict(tag='tag_example')
        response = self.client.open(
            '/jpbjesus/poi_api/1.0.0/poi/{poiId}/tag'.format(poiId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
