from mariar.databases.redis import redis
from typing import Dict, Any, Union
from ast import literal_eval

def set_cache(key: str, value: Dict[str, Any]) -> None:
  redis.setex(key, 60 * 10, str(value))

def get_cache(key: str) -> Union[Dict[str, Any], None]:
  data: bytes = redis.get(key)

  if data is None:
    return None

  cache = literal_eval(data.decode('utf-8'))
  return cache
