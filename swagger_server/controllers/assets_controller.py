import connexion
import six

from swagger_server.models.api_response import ApiResponse 
from swagger_server import util

from pprint import pprint
from bson.objectid import ObjectId
from swagger_server.controllers import pois

import werkzeug
import requests
import base64
import json

CLIENT_ID = "f80fa92a3bfe9b0"

def post_image(poiId, upfile1, upfile2=None, upfile3=None, note=None): 
    """Uploads an image

    :param poiId: ID of POI to update
    :type poiId: str
    :param upfile1: Image to upload
    :type upfile1: werkzeug.datastructures.FileStorage
    :param upfile2: 
    :type upfile2: werkzeug.datastructures.FileStorage
    :param upfile3: 
    :type upfile3: werkzeug.datastructures.FileStorage
    :param note: Description of file contents
    :type note: str

    :rtype: ApiResponse
    """

    if connexion.request.files['upfile1']:
        file1 = upload_imgur(imagefile=connexion.request.files['upfile1'].read())

    pois.update({'_id': poiId}, {"$set": {'photos': file1}})

    return ApiResponse(code=200, type=None, message="Image uploaded")

def post_tag(poiId, tag): 
    """Uploads an tag to describe POI

    :param poiId: ID of POI to upload tag
    :type poiId: str
    :param tag: tag to describe poi
    :type tag: str

    :rtype: ApiResponse
    """

    pois.update({{'_id': poiId}, {"$set": {'tags': tag}}})

    return ApiResponse(code=200, type=None, message="Tag posted")

def upload_imgur(imagefile):
    url = 'https://api.imgur.com/3/image'

    payload = {
        'image': base64.standard_b64encode(imagefile)}
    files = {}
    headers = {
        'Authorization': 'Client-ID {}'.format(CLIENT_ID)
    }
    response = requests.request(
        'POST', url, headers=headers, data=payload, files=files, allow_redirects=False)
    pprint(response)
    return json.loads(response.text)['data']['link']
