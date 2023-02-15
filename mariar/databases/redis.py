import redis
from mariar.config import config
from typing import Union, Awaitable, Any

redis = redis.Redis(
  host=config.config['REDIS_HOST'],
  port=config.config['REDIS_PORT'],
  db=config.config['REDIS_DB'],
  password=config.config['REDIS_PASSWORD']
)
