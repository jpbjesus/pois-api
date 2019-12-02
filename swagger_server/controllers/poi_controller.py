import connexion
import six

from connexion.decorators.validation import *
from swagger_server.models.poi import POI  
from swagger_server.models.poi_geocode import POIGeocode
from swagger_server import util
from swagger_server.controllers import pois
from swagger_server.controllers import redis_client

import Geohash
import proximityhash

from pprint import pprint
from bson.objectid import ObjectId

def delete_poi(poiId, api_key=None):  
    """Deletes a POI

    :param poiId: POI id to delete
    :type poiId: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    try:
        pois.remove({'_id': ObjectId(poiId)})
    except IndexError as e:
        pprint(e)
        return 'POI not found', 404
    
    redis_client.zrem("geo", str(poiId))

    return 'OK! Succesful Operation', 200

def post_poi(body):  
    """Add a new POI to the database

    :param body: POI object that needs to be added to the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = POI.from_dict(connexion.request.get_json())  
        
        dikt = POIGeocode.to_dict(body.geocode)
        geocode = POIGeocode(dikt['latitude'], dikt['longitude']).to_dict()
        
        inserted = pois.insert_one({'address': body.address,
                                    'geocode': geocode, 
                                    'geohash': Geohash.encode(float(geocode['latitude']), float(geocode['longitude']), precision=7),
                                    'name': body.name,
                                    'opening_hours': body.opening_hours,
                                    'phone_number': body.phone_number,
                                    'type': body.type,
                                    'website': body.website,
                                    'photos': body.photos})
        
        redis_client.geoadd("geo", geocode['longitude'], geocode['latitude'], ObjectId(inserted.inserted_id).__str__())
        redis_client.geohash("geo", ObjectId(inserted.inserted_id).__str__())

    return 'OK! Succesful Operation; inserted with id: ' + ObjectId(inserted.inserted_id).__str__(), 200


def put_poi(body):  
    """Update an existing POI

    :param body: POI object that needs to be updated in the database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = POI.from_dict(connexion.request.get_json())  

        dikt = POIGeocode.to_dict(body.geocode)
        geocode = POIGeocode(dikt['latitude'], dikt['longitude']).to_dict()

        inserted = pois.insert({'address': body.address,
                     'geocode': geocode,
                     'geohash': Geohash.encode(float(geocode['latitude']), float(geocode['longitude']), precision=7),
                     'name': body.name,
                     'opening_hours': body.opening_hours,
                     'phone_number': body.phone_number,
                     'type': body.type,
                     'website': body.website,
                     'photos': body.photos})
    
    # redis_client.zrem("geo", ObjectId(inserted.inserted_id).__str__())
    # redis_client.geoadd("geo", geocode['longitude'], geocode['latitude'], ObjectId(inserted.inserted_id).__str__())
    # redis_client.geohash("key", ObjectId(inserted.inserted_id).__str__())

    return 'OK! Succesful Operation', 200
