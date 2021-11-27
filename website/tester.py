
from pymongo import MongoClient
#client = MongoClient()

client = MongoClient('localhost', 27017)
db = client.uncursedforge
collection = db.modsinfo

z = collection.find({"si": {'$exists': True}}).count()