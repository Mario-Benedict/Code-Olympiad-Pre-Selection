from mariar.utils.type import RedisType

def set_cache(key: str, value: str, db: RedisType):
  db.set(key, str(value))

def get_cache(key: str, db: RedisType):
  return db.get(key)
