from mariar.constant.core import END, UNDERLINE, AQI_BANNER, AQI_HEADERS
from typing import Dict, Any, List, Union
import sys
from tabulate import tabulate

def exit_app() -> None:
  sys.exit(0)

def generate_input_text(text: str) -> str:
  return f'{UNDERLINE}{text}{END} > '

def display_aqi(data: Dict[str, Any], location: str, level: int) -> None:
  print(AQI_BANNER)

  table_data: Dict[str, Any] =  data['list'][0]['components']
  table_data: List[Union[float, str, int]] = [[location, level, table_data['no2'], table_data['pm10'], table_data['o3'], table_data['pm2_5']]]

  print(tabulate(table_data, headers=AQI_HEADERS, tablefmt='simple_grid', numalign='center', stralign='center'))

def display_multiple_aqi(data: List[Dict[str, Any]]) -> None:
  print(AQI_BANNER)

  table_data: List[List[Union[float, str, int]]] = []
  for i in data:
    components = i['list'][0]['components']
    table_data.append([i['location'], i['list'][0]['main']['aqi'] ,components['no2'], components['pm10'], components['o3'], components['pm2_5']])

  print(tabulate(table_data, headers=AQI_HEADERS, tablefmt='simple_grid', numalign='center', stralign='center'))
