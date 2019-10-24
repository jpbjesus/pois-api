# coding: utf-8

from pymongo import MongoClient
from pprint import pprint

# client = MongoClient(
#     "mongodb+srv://jpbjesus:<password>@cluster0-96wjv.gcp.mongodb.net/", ssl=True)

client = MongoClient('localhost', 27017)

db = client.pymongo_test
pois = db.pois

try:
    status = db.command("serverStatus")
    # pprint(status)
except Exception as e:
    pprint(e)
