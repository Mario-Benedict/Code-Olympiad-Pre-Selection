from mariar.constant.core import AQI_BANNER
from mariar.utils.cache import get_all_cache
from mariar.constant.color import LIGHT_GREEN, END
from mariar.utils.helper import display_multiple_aqi

def get_previous_search() -> None:
  data = get_all_cache()

  if data is None:
    print(f'{LIGHT_GREEN}No previous search found{END}')
    return

  print(AQI_BANNER)
  display_multiple_aqi(data)
