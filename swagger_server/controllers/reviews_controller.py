import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util


def poi_poi_id_put(poiId, upOrDown, api_key=None):  # noqa: E501
    """Update rating from one POI

     # noqa: E501

    :param poiId: POI id to update
    :type poiId: int
    :param upOrDown: True mean upvote, False means downvote.
    :type upOrDown: bool
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def post_review(poiId, review):  # noqa: E501
    """Uploads an text review

     # noqa: E501

    :param poiId: ID of POI to update
    :type poiId: int
    :param review: text review to upload
    :type review: str

    :rtype: ApiResponse
    """
    return 'do some magic!'
