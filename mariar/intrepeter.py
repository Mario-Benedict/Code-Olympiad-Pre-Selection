from mariar.constant import color
import os
import sys
from mariar.utils.type import RedisType, MongoType
from mariar.utils.helper import generate_input_text
from typing import Dict, Any

class MariarIntrepeter:
  def __init__(self, db_redis: RedisType = None, db_mongo: MongoType = None) -> None:
    self.db_redis: RedisType = db_redis
    self.db_mongo: MongoType = db_mongo

    self.command_options: Dict[str, Any] = {
      'clear': lambda: self.clear(),
      'exit': lambda: self.exit(),
      'quit': lambda: self.exit(),
      '1': lambda: print('option 1'),
      '2': lambda: print('option 2'),
      '3': lambda: print('option 3')
    }

    self.print_banner()
    self.print_options()

  def print_banner(self) -> None:
    self.clear()

    banner = f''' {color.LIGHT_GREEN}_   __            _
|  \/  |          (_)
| \  / | __ _ _ __ _  __ _ _ __
| |\/| |/ _` | '__| |/ _` | '__|
| |  | | (_| | |  | | (_| | |
|_|  |_|\__,_|_|  |_|\__,_|_|{color.END}
  '''
    banner += f'''
{color.LIGHT_CYAN}[*] Created By     : {color.WHITE}Mario Benedict
 {color.LIGHT_CYAN}|---> Github      : {color.WHITE}https://github.com/Mario-Benedict
{color.LIGHT_CYAN}[*] Credit         :
 {color.LIGHT_CYAN}|---> Back4app    : {color.WHITE}https://www.back4app.com
 {color.LIGHT_CYAN}|---> OpenWeather : {color.WHITE}https://openweathermap.org
{color.LIGHT_CYAN}[*] Version        : {color.WHITE}0.0.1
  '''

    print(banner)

  @staticmethod
  def print_options() -> None:
    options = f'''{color.LIGHT_YELLOW}[!] Select an option:{color.END}

{color.LIGHT_GREEN}[1] {color.LIGHT_CYAN}Search Location
{color.LIGHT_GREEN}[2] {color.LIGHT_CYAN}Previous Search
{color.LIGHT_GREEN}[3] {color.LIGHT_CYAN}Current Location{color.END}
  '''

    print(options)

  @staticmethod
  def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    MariarIntrepeter.print_options()

  @staticmethod
  def exit() -> None:
    sys.exit(0)

  def start(self) -> None:
    while True:
      try:
        command: str = input(generate_input_text('Mariar'))

        if command in self.command_options:
          self.command_options[command]()
        else:
          print(f'{color.LIGHT_YELLOW}Option not found !!{color.END}')

      except (KeyboardInterrupt, SystemExit):
        MariarIntrepeter.exit()
