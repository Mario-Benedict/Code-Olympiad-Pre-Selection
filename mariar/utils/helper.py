from mariar.constant.core import END, UNDERLINE, AQI_BANNER
from typing import Dict
import sys

def exit_app() -> None:
  sys.exit(0)

def generate_input_text(text: str) -> str:
  return f'{UNDERLINE}{text}{END} > '

def display_aqi():
  print(AQI_BANNER)
