import time

import requests


def get_actual_weather():
    weather_url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=curitiba,parana'
    response = requests.get(weather_url).json()
    return response['main']['temp'], response['main']['humidity']


def raise_temperature(temperature):
    return temperature + 1


def drop_temperature(temperatura):
    return temperatura - 1


def handle_warmer(state: str):
    if state == 'on':
        print('Ligando o aquecedor.')
        time.sleep(1)
        print('Aquecedor LIGADO')
    else:
        print('Desligando o aquecedor.')
        time.sleep(1)
        print('Aquecedor DESLIGADO')
