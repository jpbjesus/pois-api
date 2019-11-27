# coding: utf-8
import os
import json
import redis
from bson.objectid import ObjectId
from pymongo import MongoClient
from pprint import pprint

mongodb_uri = "mongodb+srv://jpbjesus:qfCZRh5GVfzTPiZs@cluster0-96wjv.gcp.mongodb.net/"
client = MongoClient(mongodb_uri, ssl=True)

redis_host = os.environ.get(
    'REDISHOST', '34.77.211.58')
redis_port = int(os.environ.get('REDISPORT', 6379))
key = "geo"

# client = MongoClient('localhost', 27017)

db = client.pois_api
pois = db.pois

# try:
#     status = db.command("serverStatus")
#     pprint(status)
# except Exception as e:
#     pprint(e)

try:
    # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
    # using the default encoding utf-8.  This is client specific.
    redis_client = redis.StrictRedis(
        host=redis_host, port=redis_port, decode_responses=True)
        
    for poi in build_cursor(pois.find({})):
        redis_client.geoadd(key, poi['geocode']['longitude'], poi['geocode']['latitude'], ObjectId(poi["_id"]).__str__())
        redis_client.geohash(key, ObjectId(poi["_id"]).__str__())

except Exception as e:
    pprint(e)

def build_cursor(cursor):
    """
    Builds a JSON response for a given cursor
    """
    response = json.loads('{}')
    response_to_append_to = response['results'] = []

    for idx, bp in enumerate(cursor):
        response_to_append_to.append(bp)
    return response
