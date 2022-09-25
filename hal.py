import random

import requests

from entities.greenhouse import GreenHouse
from my_conf import CLIENT_IDS
from entities.warmer import Warmer


def get_actual_weather():
    """
    Obtém a temperatura e a umidade atual da região onde estão as estufas.
    :return: retorna a temperatura e a umidade da região onde estão as estufas.
    """
    try:
        weather_url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=curitiba,parana'
        response = requests.get(weather_url).json()
        return response['main']['temp'], response['main']['humidity']
    except KeyError:
        return random.randrange(0, 20), random.randrange(0, 100)


def set_greenhouse_temperature():
    """
    Atribui um valor randômico à estufa que varia de -5 a +5 graus em relação à temperatura do ambiente.
    :return: retorna o valor da temperatura e da humidade da estufa.
    """
    global weather_temperature, weather_humidity
    return weather_temperature + random.randrange(-5, 5), weather_humidity + random.randrange(-5, 5)


def get_greenhouse_temperature(client_id: str):
    """
    Obtém a temperatura da estufa vinculada ao dispositivo no Cayenne.
    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :return: retorna a temperatura da estufa.
    """
    global greenhouses
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            return greenhouse.temperature


def get_greenhouse_humidity(client_id: str):
    """
    Obtém a umidade da estufa vinculada ao dispositivo no Cayenne.
    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :return: retorna a umidade da estufa.
    """
    global greenhouses
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            return greenhouse.humidity


def raise_greenhouse_temperature(client_id: str):
    """
    Eleva a temperatura da estufa.
    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    """
    global greenhouses
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            greenhouse.raise_temperature()


def drop_greenhouse_temperature(client_id: str):
    """
    Diminui a temperatura da estufa.
    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    """
    global greenhouses, weather_temperature
    for greenhouse in greenhouses:
        if greenhouse.client_id == client_id:
            if greenhouse.temperature > weather_temperature:
                greenhouse.drop_temperature()


def get_warmer(warmer_id: str):
    """
    Obtem o aquecedor vinculado ao dispositivo no Cayenne.
    :param warmer_id: string que contém o client_id do dispositivo no Cayenne.
    :return: retorna a instância do aquecedor selecionado.
    """
    global warmers
    for warmer in warmers:
        if warmer.id == warmer_id:
            return warmer


def handle_warmer(warmer_id, status: bool):
    """
    Liga e desliga o aquecedor
    :param warmer_id: string que contém o client_id do dispositivo no Cayenne.
    :param status: booleano com o status do botão do Cayenne.
    """
    global warmers
    for warmer in warmers:
        if warmer.id == warmer_id:
            warmer.state = status


# Instanciando as estufas, os motores e setando todos os valores iniciais.

weather_temperature, weather_humidity = get_actual_weather()
warmers = []
greenhouses = []

for index, client_id in enumerate(CLIENT_IDS):
    index += 1
    new_warmer = Warmer(
        id=client_id,
        name=f'Device{index}',
        state=True
    )
    new_greenwhouse = GreenHouse(
        client_id=client_id,
        name=f'GreenHouse{index}',
        temperature=set_greenhouse_temperature()[0],
        humidity=set_greenhouse_temperature()[1]
    )
    warmers.append(new_warmer)
    greenhouses.append(new_greenwhouse)
