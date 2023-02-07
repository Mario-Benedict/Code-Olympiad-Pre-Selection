import sys
import os
import logging.handlers
from mariar.constant import core
from mariar.intrepeter import MariarIntrepeter
from mariar.databases import redis, mongo
from mariar.constant.color import LIGHT_CYAN, END
from mariar.utils.type import RedisType, MongoType

if sys.version_info.major < 3:
    print('This application requires Python 3. Please install Python 3 and try again.')
    exit(0)

log_handler = logging.handlers.RotatingFileHandler(filename=core.LOG_FILE, maxBytes=core.LOG_MAX_BYTES, backupCount=core.LOG_BACKUP_COUNT)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(log_handler)

def mariar() -> None:
  redis_db: RedisType = redis.Redis()
  mongo_db: MongoType = mongo.Mongo(db='aqi')

  app = MariarIntrepeter(redis_db, mongo_db)

  app.start()

if __name__ == "__main__":
  try:
    mariar()
  except (KeyboardInterrupt, SystemExit):
    LOGGER.info('Exiting application...')
    print(f'\n{LIGHT_CYAN}Exiting application...{END}')
    exit(0)
