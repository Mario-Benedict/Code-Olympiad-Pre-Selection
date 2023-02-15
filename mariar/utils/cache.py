from mariar.databases.redis import redis

def set_cache(key: str, value: str):
  redis.setex(key, 60 * 10, value)

def get_cache(key: str):
  return redis.get(key)
