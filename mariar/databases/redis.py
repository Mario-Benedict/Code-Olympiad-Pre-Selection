import redis
from mariar.config import config
from typing import Union, Awaitable, Any

class Redis:
  def __init__(self, host: str = config.config['REDIS_HOST'], port: Union[str, int]=config.config['REDIS_PORT'], db: str= config.config['REDIS_DB'], password: str=config.config['REDIS_PASSWORD']) -> None:
    self.redis = redis.Redis(
      host=host,
      port=port,
      db=db,
      password=password
    )

  def set(self, key: str, data: str) -> None:
    self.redis.setex(key, 60*10, data)

  def get(self, key: str) -> Union[Awaitable, Any]:
    return self.redis.get(key)
