import random

import requests

from entities.greenhouse import GreenHouse
from my_conf import CLIENT_IDS
from entities.warmer import Warmer


def get_actual_weather():
    try:
        weather_url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=curitiba,parana'
        response = requests.get(weather_url).json()
        return response['main']['temp'], response['main']['humidity']
    except KeyError:
        return random.randrange(0, 20), random.randrange(0, 100)


def set_greenhouse_temperature():
    global weather_temperature, weather_humidity
    return weather_temperature + random.randrange(-5, 5), weather_humidity + random.randrange(-5, 5)


def get_temperature(client_id: str):
    global greenhouses
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            return greenhouse.temperature


def get_humidity(client_id: str):
    global greenhouses
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            return greenhouse.humidity


def raise_temperature(client_id: str):
    global greenhouses
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            greenhouse.temperature += 1


def drop_temperature(client_id: str):
    global greenhouses, weather_temperature
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            if greenhouse.temperature > weather_temperature:
                greenhouse.temperature -= 1


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
warmers = []
greenhouses = []

for index, client_id in enumerate(CLIENT_IDS):
    index += 1
    new_warmer = Warmer(client_id, f'Device{index}', True)
    new_greenwhouse = GreenHouse(
        client_id=client_id,
        name=f'GreenHouse{index}',
        temperature=set_greenhouse_temperature()[0],
        humidity=set_greenhouse_temperature()[1]
    )
    warmers.append(new_warmer)
    greenhouses.append(new_greenwhouse)
