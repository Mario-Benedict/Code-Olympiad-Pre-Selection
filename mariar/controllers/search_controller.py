from mariar.utils.helper import generate_input_text
from typing import List, Dict, Any, Optional
from mariar.constant import color
from mariar.api.aqi import get_aqi
from mariar.databases.mongo import mongo
from mariar.utils.helper import exit_app, display_aqi
from mariar.utils.cache import get_cache, set_cache
from ast import literal_eval

def display_search(data: List[Dict[str, Any]]):
  for i, v in enumerate(data):
    country: str = v['name']
    print(f'{color.LIGHT_GREEN}[{i+1}]\t {color.LIGHT_CYAN}{country} {color.END}')

def search_location():
  mongo_collection = mongo['countries']

  countries: List[Dict[str, Any]] = list(mongo_collection.find({}))

  display_search(countries)

  while True:
    try:
      counties_len: int = len(countries)
      data_input = input(generate_input_text('Search Location'))

      if data_input.lower() == 'exit' or data_input.lower() == 'quit':
        exit_app()
      elif data_input.lower() == 'back':
        break
      elif data_input.isnumeric() and  counties_len >= int(data_input) >= 1:
        search_aqi(countries[int(data_input)-1]['objectId'])
      elif data_input.isalpha():
        countries = list(mongo_collection.find({ "name": { "$regex": data_input, "$options": "i" } }))
        display_search(countries)
      else:
        pass
    except KeyboardInterrupt:
      exit_app()

def search_aqi(id: str):
  mongo_collection = mongo['cities']

  cities: List[Dict[str, Any]] = list(mongo_collection.find({ "country.objectId": id }))

  display_search(cities)

  while True:
    try:
      cities_len = len(cities)
      data_input = input(generate_input_text('Search City'))

      if data_input.lower() == 'exit' or data_input.lower() == 'quit':
        exit_app()
      elif data_input.lower() == 'back':
        break
      elif data_input.isnumeric() and cities_len >= int(data_input) >= 1:
        res = cities[int(data_input)-1]
        location = res.get('location')
        country_id = res.get('country').get('objectId')

        mongo_collection = mongo['countries']
        country = mongo_collection.find_one({ "objectId": country_id })

        if not location:
          print('Location not found')
          continue

        if get_cache(res['name']) is not None:
          aqi = get_cache(res['name'])
          display_aqi(aqi, f'{res["name"]}, {country["name"]}', aqi['list'][0]['main']['aqi'])
          break

        aqi = get_aqi(location.get('latitude'), location.get('longitude'))
        set_cache(res['name'], str(aqi))
        display_aqi(aqi, f'{res["name"]}, {country["name"]}', aqi['list'][0]['main']['aqi'])
        break
      elif data_input.isalpha():
        cities = list(mongo_collection.find({ "name": { "$regex": data_input, "$options": "i" }, "country.objectId": id }))
        display_search(cities)
      else:
        pass
    except KeyboardInterrupt:
      exit_app()
