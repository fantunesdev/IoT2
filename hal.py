import random
import time

import requests


def get_actual_weather():
    try:
        weather_url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=curitiba,parana'
        response = requests.get(weather_url).json()
        return response['main']['temp'], response['main']['humidity']
    except KeyError:
        return random.randrange(0, 40), random.randrange(0, 100)


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
    global greenhouse1_temperature, greenhouse2_temperature
    if client_id == '232380f0-3b82-11ed-baf6-35fab7fd0ac8':
        greenhouse1_temperature -= 1
    else:
        greenhouse2_temperature -= 1


def handle_warmer(state: str):
    if state == 'on':
        print('Ligando o aquecedor.')
        time.sleep(1)
        print('Aquecedor LIGADO')
    else:
        print('Desligando o aquecedor.')
        time.sleep(1)
        print('Aquecedor DESLIGADO')


greenhouse1_temperature, greenhouse1_humidity = get_actual_weather()
greenhouse2_temperature, greenhouse2_humidity = get_actual_weather()
