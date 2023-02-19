from mariar.databases.redis import redis
from typing import Dict, Any, Union, List
from ast import literal_eval

def set_cache(key: str, value: Dict[str, Any]) -> None:
  redis.setex(key, 60 * 10, str(value))

def get_cache(key: str) -> Union[Dict[str, Any], None]:
  data: bytes = redis.get(key)

  if data is None:
    return None

  cache = literal_eval(data.decode('utf-8'))
  return cache

def get_all_cache() -> Union[List[Dict[str, Any]], None]:
  keys: List[str] = redis.keys('*')

  if len(keys) == 0:
    return None

  cache = [{ **get_cache(key), "location": key.decode('utf-8')} for key in keys]

  return cache
