import connexion
import six
import json
import math

from pprint import pprint
from flask import jsonify

from swagger_server.models.poi import POI  
from swagger_server.controllers import pois
from swagger_server.controllers import build_cursor
from swagger_server import util
from swagger_server.models.poi_geocode import POIGeocode
import proximityhash
from bson.objectid import ObjectId
from pymongo.collation import Collation
import Geohash

import requests
from requests.exceptions import HTTPError
from swagger_server.controllers import redis_client

def get_id(name):
    """ Find ID by name

    Returns a single or an array of POIs
    
    :param name: Name of POI
    
    :rtype: POI
    """
    try:
        response = jsonify(build_cursor(pois.find({"name": {"$regex": name, "$options": 'i'}}))['results'][0]['_id'])
    except Exception as e:
        return "POI not found", 404
    return response, 200

def get_by_id(poiId):  
    """Find POI by ID

    Returns a single POI 

    : param poiId: ID of POI to return
    : type poiId: str

    : rtype: POI
    """
    try:
        response = pois.find_one({'_id': ObjectId(poiId)})
    except IndexError as e:
        return 'POI not found', 404
    return jsonify(response), 200


def get_by_geocode(lat, lng, radius=None): 
    """Returns an array of POIs

    : param name: name query of POI
    : type name: str
    : param lat: geocoded latitude of POI
    : type lat: str
    : param long: geocoded longitude of POI
    : type lng: str
    : param radius: max radius to search an POI
    : type radius: int

    : rtype: List[POI]
    """

    if radius is None:
        radius = 5000
    
    query = redis_client.georadius("geo", str(lng), str(lat), radius=radius, unit="m", withdist=True)
    pprint(query)
    response = json.loads('{}')
    response_to_append_to = response = []

    for k, v in enumerate(query):
        response_to_append_to.append(requests.get("https://poi-api-3aybx4hfgq-ew.a.run.app/poi_api/poi/{}".format(query[k][0])).json())
        response[k]['distance']=query[k][1]
    if response == []:
        return response, 404
    return response, 200


def get_type(type, lat=None, lng=None, radius=None): 
    """Find POIs by type

    Returns a single or an array of POIs 

    : param type: Types values that need to be considered for filter
    : type type: str
    : param lat: geocoded latitude of POI
    : type lat: float
    : param lng: geocoded longitude of POI
    : type lng: float
    : param radius: max radius to search an POI
    : type radius: int

    : rtype: List[POI]
    """
    pois_list = list()

    if radius is None:
        radius = 5000

    query = redis_client.georadius("geo", str(lng), str(lat), radius=radius, unit="m", withdist=True)
    response = json.loads('{}')
    response_to_append_to = response = []

    for k, v in enumerate(query):
        res = requests.get("https://poi-api-3aybx4hfgq-ew.a.run.app/poi_api/poi/{}".format(query[k][0])).json()
        response[k]['distance'] = query[k][1]
        if type in res['type']:
            response_to_append_to.append(res)
    if response == []:
        return response, 404
    return response, 200
