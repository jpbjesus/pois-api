from pprint import pprint
from pymongo import MongoClient

import json
import requests

from swagger_server.models import POI
from swagger_server.models import POIGeocode

import sys
import Geohash

lat = sys.argv[1]
lng = sys.argv[2]
radius = sys.argv[3]

API_KEY = 'AIzaSyBu5GK0P_4ojVWTyOjaXHBbUiY75M4abSw'

# client = MongoClient(
#     "mongodb+srv://jpbjesus:<password>@cluster0-96wjv.gcp.mongodb.net/", ssl=True)

# client = MongoClient('localhost', 27017)

# mongodb_uri = "mongodb+srv://jpbjesus:qfCZRh5GVfzTPiZs@cluster0-96wjv.gcp.mongodb.net/"
# client = MongoClient(mongodb_uri, ssl=True)


# db = client.pois_api
# pois = db.pois

# try:
#     status = db.command("serverStatus")
#     # pprint(status)
# except Exception as e:
#     pprint(e)

count = 0

for i in ['airport', 'amusement_park', 'aquarium', 'art_gallery', 'bar', 'bus_station', 'cafe', 'campground', 'casino', 'cemetery', 'church', 'hindu_temple', 'library', 'movie_theater', 'museum', 'night_club', 'restaurant', 'shopping_mall', 'spa', 'stadium', 'subway_station', 'tourist_attraction', 'train_station', 'university', 'zoo']:
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}".format(
        lat, lng, radius, i, API_KEY)

    response = requests.get(url)

    for result in response.json()["results"]:
        geocode = POIGeocode(result['geometry']['location']['lat'],
                            result['geometry']['location']['lng']).to_dict()
        
        url1 = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=name,formatted_address,rating,formatted_phone_number,website,opening_hours,photos&key={}".format(
            result['place_id'], API_KEY)

        response = requests.get(url1)
        res=response.json()

        poi = POI(name=res['result']['name'], type=i, address=res['result']['formatted_address'], phone_number=(res['result']['formatted_phone_number'] if "formatted_phone_number" in res['result'] else None),
                    geocode=geocode, price_level=(res['result']['price_level'] if "price_level" in res['result'] else None), opening_hours=(res['result']['opening_hours']['weekday_text'] if 'opening_hours' in res['result'] else None), rating=(res['result']['rating'] if 'rating' in res['result'] else 0.0),
                    website=(res['result']['website'] if "website" in res['result'] else None))
       
        if 'photos' in res['result']:
            for ref in res['result']['photos']:
                photo_reference = ref['photo_reference']
        else:
            photo_reference = None
        
        body = {'address': poi.address,
                'geocode': geocode,
                'geohash': Geohash.encode(float(geocode['latitude']), float(geocode['longitude']), precision=7),
                'name': poi.name,
                'opening_hours': poi.opening_hours,
                'phone_number': poi.phone_number,
                'price_level': poi.price_level,
                'type': poi.type,
                'website': poi.website,
                'photo_reference': photo_reference}

        for k, v in list(body.items()): 
            if v == None:
                try:
                    body.pop(k)
                except:
                    pass
        
        # pprint(json.loads(json.dumps(body)))

        if poi.rating is 0.0:
            pass
        else:
            pprint("/n")
            req = requests.post("https://poi-api-3aybx4hfgq-ew.a.run.app/poi_api/poi", json=body)
            pprint(req.json())

            # pprint("INSERTED... " + res['result']
            #     ['name'] + " (" + str(count) + ")")
            # count += 1

def get_photo(photo_reference):
    url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(photo_reference, API_KEY)
    response = requests.get(url1)
    res = response.json()
