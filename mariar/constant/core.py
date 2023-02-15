LOG_FILE: str = 'mariar.log'
LOG_MAX_BYTES: int = 1024 * 1024 * 5
LOG_BACKUP_COUNT: int = 5
END: str = '\033[0m'
UNDERLINE: str = '\033[4m'
API_URL: str =  'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'
AQI_BANNER = ''' ___________________________________________________________________
|                                                                   |
|                                                                   |
|                Air Quality Index Level Description!               |
|                                                                   |
|___________________________________________________________________|

 ___________________________________________________________________
|               |       |                                           |
| Quality Level | Index |      Pollutant concentration in µg/m\u00b3     |
|_______________|_______|___________________________________________|
|                       |          |          |          |          |
|                       |    NO\u2082   |    PM\u2081\u2080  |    O\u2083    |   PM\u2082\u2085   |
|_______________________|__________|__________|__________|__________|
|               |       |          |          |          |          |
| Good          |   1   |   0-50   |   0-25   |   0-60   |  0-15    |
|_______________|_______|__________|__________|__________|__________|
|               |       |          |          |          |          |
| Fair          |   2   |  50-100  |   25-50  |  60-120  |  15-30   |
|_______________|_______|__________|__________|__________|__________|
|               |       |          |          |          |          |
| Moderate      |   3   |  100-200 |   50-90  |  120-180 |  30-55   |
|_______________|_______|__________|__________|__________|__________|
|               |       |          |          |          |          |
| Poor          |   4   |  200-400 |   90-180 |  180-240 |  55-110  |
|_______________|_______|__________|__________|__________|__________|
|               |       |          |          |          |          |
| Very Poor     |   5   |   >400   |   >180   |   >240   |   >110   |
|_______________|_______|__________|__________|__________|__________|

 ___________________________________________________________________
|                                                                   |
|            https://openweathermap.org/api/air-pollution           |
|___________________________________________________________________|
'''

DISPLAY_AQI = f'''


'''
