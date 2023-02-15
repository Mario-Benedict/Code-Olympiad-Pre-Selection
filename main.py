import sys
import os

if sys.version_info.major < 3:
    print('This application requires Python 3. Please install Python 3 and try again.')
    exit(0)

import logging.handlers
from mariar.constant import core
from mariar.interpreter import MariarInterpreter
from mariar.constant.color import LIGHT_CYAN, END

log_handler = logging.handlers.RotatingFileHandler(filename=core.LOG_FILE, maxBytes=core.LOG_MAX_BYTES, backupCount=core.LOG_BACKUP_COUNT)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(log_handler)

def mariar() -> None:
  app = MariarInterpreter()

  app.start()

if __name__ == "__main__":
  try:
    mariar()
  except (KeyboardInterrupt, SystemExit):
    LOGGER.info('Exiting application...')
    print(f'\n{LIGHT_CYAN}Exiting application...{END}')
    sys.exit(0)
