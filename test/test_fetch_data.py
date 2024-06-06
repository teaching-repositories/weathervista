from ..scripts.fetch_data import *

api_key = '377c31c283cd3ce3430e73063f15df4f'
location = 'Guangzhou'
data = fetch_weather_data(api_key, location)
print(data)