import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util


def post_image(poiId, upfile1, upfile2=None, upfile3=None, note=None):  # noqa: E501
    """Uploads an image

     # noqa: E501

    :param poiId: ID of POI to update
    :type poiId: int
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


def post_tag(poiId, tag):  # noqa: E501
    """Uploads an tag to describe POI

     # noqa: E501

    :param poiId: ID of POI to upload tag
    :type poiId: int
    :param tag: tag to describe poi
    :type tag: str

    :rtype: ApiResponse
    """
    return 'do some magic!'
