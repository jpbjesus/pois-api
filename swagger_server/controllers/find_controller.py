import connexion
import six
import json
import math

from pprint import pprint
from flask import jsonify

from swagger_server.models.poi import POI  
from swagger_server.controllers import pois
from swagger_server.controllers import build_JSON_cursor
from swagger_server import util
from swagger_server.models.poi_geocode import POIGeocode
import proximityhash
from bson.objectid import ObjectId

import Geohash

import requests
from requests.exceptions import HTTPError

def get_id(name):
    """ Find ID by name

    Returns a single or an array of POIs
    
    :param name: Name of POI
    
    :rtype: POI
    """
    
    return jsonify(build_JSON_cursor(pois.find({"name": {"$regex": name, "$options": 'i'}}))['results'][0]['_id'])

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
        pprint(e)
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
    pois_list = list()

    if radius is None:
        radius = 5000

    geohash = proximityhash.create_geohash(latitude=float(lat), longitude=float(lng), radius=radius, precision=7)
    set_proximity = geohash.replace("'","").split(",")

    for elem in set_proximity:
       try:
            ghash = pois.find({'geohash': elem})
            pois_list.append(ghash[0])
       except IndexError as e:
           pass

    return jsonify(pois_list), 200


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

    geohash = proximityhash.create_geohash(latitude=float(lat), longitude=float(lng), radius=radius, precision=7)
    set_proximity = geohash.replace("'", "").split(",")

    for elem in set_proximity:
       try:
            ghash = pois.find({'geohash': elem})
            if type in ghash[0]['type']:
                pois_list.append(ghash[0])
                pprint("distance: " + str(CoordDistance(float(lat), float(lng), float(ghash[0]['geocode']['latitude']), float(ghash[0]['geocode']['longitude']))))
       except IndexError as e:
           pass

    return jsonify(pois_list), 200

def CoordDistance(lat1, lng1, lat2, lng2):
    return 6371 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lng2 - lng1))
