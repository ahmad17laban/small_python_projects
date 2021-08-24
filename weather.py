import requests
from pprint import pprint

api_key ='be14f94465ac885e41d1d4c07fa2f3fa'

city = input('Enter the city name: ')

base_url= 'https://api.openweathermap.org/data/2.5/weather?appid='+ api_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)