from pymongo import MongoClient
from typing import Dict, Any, List
from mariar.config import config

class Mongo:
  def __init__(self, mongo_url: str = config.config['MONGO_URL'] ,db: str = 'test', collection: str = 'test') -> None:
    self.mongo_url: str = mongo_url
    self.db: str = db
    self.collection: str = collection
    self.client: MongoClient = MongoClient(self.mongo_url)
    self.db = self.client[self.db]
    self.collection = self.db[self.collection]

  def find(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return self.collection.find(data)

  def change_collection(self, collection: str = 'test') -> None:
    self.collection = self.db[collection]
