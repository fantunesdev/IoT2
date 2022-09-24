import random
import time

import requests

from my_conf import CLIENT_IDS
from warmer import Warmer


def get_actual_weather():
    try:
        weather_url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=curitiba,parana'
        response = requests.get(weather_url).json()
        return response['main']['temp'], response['main']['humidity']
    except KeyError:
        return random.randrange(0, 40), random.randrange(0, 100)


def set_greenhouse_temperature():
    global weather_temperature, weather_humidity
    return weather_temperature + random.randrange(-5, 5), weather_humidity + random.randrange(-5, 5)


def get_temperature(client_id):
    global greenhouse1_temperature, greenhouse2_temperature
    if client_id == '232380f0-3b82-11ed-baf6-35fab7fd0ac8':
        return greenhouse1_temperature
    return greenhouse2_temperature


def get_humidity(client_id):
    global greenhouse1_humidity, greenhouse2_humidity
    if client_id == '232380f0-3b82-11ed-baf6-35fab7fd0ac8':
        return greenhouse1_humidity
    return greenhouse2_humidity


def raise_temperature(client_id):
    global greenhouse1_temperature, greenhouse2_temperature
    if client_id == '232380f0-3b82-11ed-baf6-35fab7fd0ac8':
        greenhouse1_temperature += 1
    else:
        greenhouse2_temperature += 1


def drop_temperature(client_id):
    global greenhouse1_temperature, greenhouse2_temperature, weather_temperature
    if client_id == '232380f0-3b82-11ed-baf6-35fab7fd0ac8':
        if greenhouse1_temperature > weather_temperature:
            greenhouse1_temperature -= 1
    else:
        if greenhouse1_temperature > weather_temperature:
            greenhouse2_temperature -= 1


def get_warmer(warmer_id: str):
    global warmers
    for warmer in warmers:
        if warmer.id == warmer_id:
            return warmer


def handle_warmer(warmer_id, status: bool):
    global warmers
    for warmer in warmers:
        if warmer.id == warmer_id:
            warmer.state = status


weather_temperature, weather_humidity = get_actual_weather()
greenhouse1_temperature, greenhouse1_humidity = set_greenhouse_temperature()
greenhouse2_temperature, greenhouse2_humidity = set_greenhouse_temperature()
warmers = []

for id in CLIENT_IDS:
    new_warmer = Warmer(id, True)
    warmers.append(new_warmer)
