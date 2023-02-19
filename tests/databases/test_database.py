from mariar.databases.mongo import mongo
from mariar.databases.redis import redis

def test_redis():
  assert redis is not None

def test_mongo():
  assert mongo is not None

def test_mongo_collection():
  assert mongo['cities'] is not None and mongo['countries'] is not None

def test_cities_collection_not_empty():
  cities_collection = mongo['cities']
  cities = cities_collection.find_one()

  assert len(list(cities)) > 0

def test_countries_collection_not_empty():
  countries_collection = mongo['countries']
  countries =  countries_collection.find_one()

  assert len(list(countries)) > 0
