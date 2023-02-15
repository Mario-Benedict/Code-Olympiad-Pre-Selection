from pymongo import MongoClient
from mariar.config import config

mongo = MongoClient(config.config['MONGO_URL'])
mongo = mongo[config.config['MONGO_DB']]
