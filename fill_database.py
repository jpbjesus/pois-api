from pprint import pprint
from pymongo import MongoClient

import json
import requests

from swagger_server.models import POI
from swagger_server.models import POIGeocode

import sys
import Geohash
import base64

lat = sys.argv[1]
lng = sys.argv[2]
radius = sys.argv[3]

API_KEY = 'AIzaSyBu5GK0P_4ojVWTyOjaXHBbUiY75M4abSw'
CLIENT_ID = "f80fa92a3bfe9b0"

def get_photo(photo_reference):
    url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={}&key={}".format(
        photo_reference, API_KEY)
    response = requests.get(url)
    return upload_imgur(response.content)


def upload_imgur(imagefile):
    url = 'https://api.imgur.com/3/image'

    payload = {
        'image': base64.standard_b64encode(imagefile)
    }
    files = {}
    headers = {
        'Authorization': 'Client-ID {}'.format(CLIENT_ID)
    }
    response = requests.request(
        'POST', url, headers=headers, data=payload, files=files, allow_redirects=False)
    
    return json.loads(response.text)['data']['link']

if __name__ == "__main__":
    count = 0
    types = 'airport', 'amusement_park', 'aquarium', 'art_gallery', 'bar', 'bus_station', 'cafe', 'campground', 'casino', 'cemetery', 'church', 'hindu_temple', 'library', 'movie_theater', 'museum', 'night_club', 'restaurant', 'shopping_mall', 'spa', 'stadium', 'subway_station', 'tourist_attraction', 'train_station', 'university', 'zoo'
    for i in ['tourist_attraction' or 'point_of_interest']:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}".format(
            lat, lng, radius, i, API_KEY)

        response = requests.get(url)

        for result in response.json()["results"]:
            geocode = POIGeocode(result['geometry']['location']['lat'],
                                result['geometry']['location']['lng']).to_dict()
            
            url1 = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=name,formatted_address,formatted_phone_number,website,opening_hours,photos,types&key={}".format(
                result['place_id'], API_KEY)

            response = requests.get(url1)
            res=response.json()

            photos = []

            if 'photos' in res['result']:
                # for ref in res['result']['photos']:
                #     photos.append(get_photo(ref['photo_reference']))
                photos = None
            else:
                photos = None
            
            poi = POI(  name=res['result']['name'], 
                        type=res['result']['types'], 
                        address=res['result']['formatted_address'], 
                        phone_number=res['result']['formatted_phone_number'] if "formatted_phone_number" in res['result'] else None,
                        geocode=geocode, 
                        opening_hours=res['result']['opening_hours']['weekday_text'] if 'opening_hours' in res['result'] else None,
                        website=res['result']['website'] if "website" in res['result'] else None, 
                        photos=photos)

            website = poi.website[0] if not None else None
            
            body = {
                'address': poi.address,
                'geocode': geocode,
                'geohash': Geohash.encode(float(geocode['latitude']), float(geocode['longitude']), precision=7),
                'name': poi.name,
                'opening_hours': poi.opening_hours,
                'phone_number': poi.phone_number,
                'type': poi.type,
                'website': website,
                'photos': poi.photos
            }

            for k, v in list(body.items()): 
                if v == None:
                    try:
                        body.pop(k)
                    except:
                        pass
        
            req = requests.post("https://poi-api-3aybx4hfgq-ew.a.run.app/poi_api/poi", json=body)
            print(req.text)
