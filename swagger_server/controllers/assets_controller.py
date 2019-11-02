import connexion
import six

from swagger_server.models.api_response import ApiResponse 
from swagger_server import util

from pprint import pprint
from bson.objectid import ObjectId
from swagger_server.controllers import pois

from werkzeug.datastructures import FileStorage

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

    return 'do some magic!'


def post_tag(poiId, tag): 
    """Uploads an tag to describe POI

    :param poiId: ID of POI to upload tag
    :type poiId: str
    :param tag: tag to describe poi
    :type tag: str

    :rtype: ApiResponse
    """

    pois.update({{'_id': poiId}, {"$set": {'tags': tag}}})

    return 'do some magic!'
