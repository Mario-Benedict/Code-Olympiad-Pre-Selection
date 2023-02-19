from mariar.constant.core import AQI_BANNER
from mariar.constant.color import LIGHT_GREEN, END
import requests
from mariar.databases.mongo import mongo
from mariar.utils.cache import get_cache, set_cache
from mariar.api.aqi import get_aqi
from mariar.utils.helper import display_aqi

def get_current_aqi() -> None:
  mongo_collection = mongo['cities']

  print(AQI_BANNER)

  res = requests.get("https://ipinfo.io/json")

  if res.status_code > 299:
    print(f'{LIGHT_GREEN}Error while getting your location{END}')
    return

  user_city = res.json()['city']

  city = mongo_collection.find_one({ "name": user_city })

  if city is None:
    print(f'{LIGHT_GREEN}Location not found{END}')
    return

  location = city.get('location')
  country_id = city.get('country').get('objectId')

  mongo_collection = mongo['countries']
  country = country = mongo_collection.find_one({ "objectId": country_id })

  if get_cache(f'{user_city}, {country["name"]}') is not None:
    aqi = get_cache(f'{user_city}, {country["name"]}')
    display_aqi(aqi, f'{user_city}, {country["name"]}', aqi['list'][0]['main']['aqi'])
    return

  aqi = get_aqi(location.get('latitude'), location.get('longitude'))
  set_cache(f'{user_city}, {country["name"]}', str(aqi))
  display_aqi(aqi, f'{user_city}, {country["name"]}', aqi['list'][0]['main']['aqi'])
  return
