from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://138.197.205.128:27017/')

db = client.whitebird

orgs = db.organizations

pprint.pprint(orgs.find_one())