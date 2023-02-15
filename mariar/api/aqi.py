from mariar.config import config
from mariar.constant.core import API_URL
import requests

def get_aqi(lat: float, lon: float) -> dict:
  api_key: str = config.config['API_KEY']
  url: str = API_URL.format(lat=lat, lon=lon, api_key=api_key)
  return requests.get(url).json()
