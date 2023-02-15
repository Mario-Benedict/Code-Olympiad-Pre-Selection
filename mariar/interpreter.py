from mariar.constant import color
import os
import sys
from mariar.utils.helper import generate_input_text
from typing import Dict, Any
from mariar.controllers import controller

class MariarInterpreter:
  def __init__(self) -> None:
    self.command_options: Dict[str, Any] = {
      'exit': lambda: sys.exit(0),
      'quit': lambda: sys.exit(0),
      '1': lambda: controller.search_location(),
      '2': lambda: print('option 2'),
      '3': lambda: print('option 3')
    }

    self.print_banner()
    self.print_options()

  def print_banner(self) -> None:
    os.system('clear') if os.name == 'posix' else os.system('cls')

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

  def start(self) -> None:
    while True:
      try:
        command: str = input(generate_input_text('Mariar'))

        if command in self.command_options:
          self.command_options[command]()
        else:
          pass

      except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
