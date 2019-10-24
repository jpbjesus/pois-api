import connexion
import six

from pprint import pprint
from connexion.decorators.validation import *
from swagger_server.models.poi import POI  
from swagger_server.models.poi_geocode import POIGeocode
from swagger_server import util
from swagger_server.controllers import pois

def delete_poi(poiId, api_key=None):  
    """Deletes a POI

    :param poiId: POI id to delete
    :type poiId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    try:
        pois.remove({'id': poiId})
    except IndexError as e:
        pprint(e)
        return 'POI not found', 404

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
                                    'name': body.name,
                                    'opening_hours': body.opening_hours,
                                    'phone_number': body.phone_number,
                                    'price_level': body.price_level,
                                    'rating': body.rating,
                                    'type': body.type,
                                    'website': body.website})

    return 'OK! Succesful Operation; inserted with id: ' + str(inserted.inserted_id), 200


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

        pois.insert({'address': body.address,
                     'geocode': geocode,
                     'id': body.id,
                     'name': body.name,
                     'opening_hours': body.opening_hours,
                     'phone_number': body.phone_number,
                     'price_level': body.price_level,
                     'rating': body.rating,
                     'type': body.type,
                     'website': body.website})
    
    return 'OK! Succesful Operation', 200