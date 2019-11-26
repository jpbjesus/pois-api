# coding: utf-8
import json

from pymongo import MongoClient
from pprint import pprint

mongodb_uri = "mongodb+srv://jpbjesus:qfCZRh5GVfzTPiZs@cluster0-96wjv.gcp.mongodb.net/"
client = MongoClient(mongodb_uri, ssl=True)

# client = MongoClient('localhost', 27017)

db = client.pois_api
pois = db.pois

try:
    status = db.command("serverStatus")
    # pprint(status)
except Exception as e:
    pprint(e)

def build(cursor):
    """
    Builds a JSON response for a given cursor
    """
    response = json.loads('{}')
    response_to_append_to = response['results'] = []

    for idx, bp in enumerate(cursor):
        response_to_append_to.append(bp)

    return response
