import os, sys
import json
import redis
import requests
from bson.objectid import ObjectId
from pprint import pprint
from pymongo import MongoClient

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))

mongodb_uri = "mongodb+srv://jpbjesus:qfCZRh5GVfzTPiZs@cluster0-96wjv.gcp.mongodb.net/"
client = MongoClient(mongodb_uri, ssl=True)

db = client.pois_api
pois = db.pois

key = "geo"

city = sys.argv[1]
radius = sys.argv[2]

def build_cursor(cursor):
    """
    Builds a JSON response for a given cursor
    """
    response = json.loads('{}')
    response_to_append_to = response = []

    for idx, bp in enumerate(cursor):
        response_to_append_to.append(bp)
    return response

def hello_redis():
    """
        r.geoadd("geo", lng, lat, _id) # key longitude latitude member [longitude latitude member ...]
        r.geohash("geo", _id)
        r.georadius("geo", lng, lat, radius, unit="km", withcoord=True, withdist=True) # key longitude latitude radius m|km|ft|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]
    """
    try:
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

        geocoding_url = "https://api.opencagedata.com/geocode/v1/json?q={}&key=e463adfff05c42ab97cffecba4856bca".format(city)
        req = requests.get(geocoding_url)
        geometry = req.json()['results'][0]['geometry']

        # for poi in build_cursor(pois.find({})):
        #     r.geoadd(key, poi['geocode']['longitude'], poi['geocode']['latitude'], ObjectId(poi["_id"]).__str__())
        #     r.geohash(key, ObjectId(poi["_id"]).__str__())
        query = r.georadius(key, str(geometry['lng']), str(geometry['lat']), radius=radius, unit="km", withcoord=False, withdist=True)
  
        for k, v in enumerate(query):
            response=requests.get("https://poi-api-3aybx4hfgq-ew.a.run.app/poi_api/poi/{}".format(query[k][0]))
            pprint(response.json()['name'])

    except Exception as e:
        pprint(e)

if __name__ == '__main__':
    hello_redis()
    
