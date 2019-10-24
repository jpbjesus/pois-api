import connexion
import six
import json


from pprint import pprint
from flask import jsonify

from swagger_server.models.poi import POI  
from swagger_server.controllers import pois
from swagger_server import util


def get_by_id(poiId):  
    """Find POI by ID

    Returns a single POI 

    :param poiId: ID of POI to return
    :type poiId: int

    :rtype: POI
    """
    try:
        response = pois.find({'id': poiId})[0]
        del response['_id']
    except IndexError as e:
        pprint(e)
        return 'POI not found', 404

    return response, 200


def get_by_name_or_geocode(name=None, lat=None, longi=None, radius=None):  
    """Returns an array of POIs

    :param name: name query of POI
    :type name: str
    :param lat: geocoded latitude of POI
    :type lat: str
    :param long: geocoded longitude of POI
    :type long: str
    :param radius: max radius to search an POI
    :type radius: int

    :rtype: List[POI]
    """

    if name!=None:
        try:
            response = pois.find(
                 {"name": {"$regex": name, "$options": 'i'}})[0]
            del response['_id']
        except IndexError as e:
            pprint(e)
            return 'POI not found', 404
    elif lat!=None and longi!=None:
        if radius==None:
            radius=5000
        response = pois.find({"lat": lat, "long":longi})[0]
        del response['_id']
    
    return response, 200


def get_type(type, lat=None, long=None, radius=None):  
    """Find POIs by type

    Returns a single or an array of POIs 

    :param type: Types values that need to be considered for filter
    :type type: str
    :param lat: geocoded latitude of POI
    :type lat: str
    :param long: geocoded longitude of POI
    :type long: str
    :param radius: max radius to search an POI
    :type radius: int

    :rtype: List[POI]
    """

    # pois.find({"type": type})


    return 'do some magic!'
