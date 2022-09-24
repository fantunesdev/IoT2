import paho.mqtt.client as mqtt

from hal import handle_warmer, raise_temperature, drop_temperature
from my_conf import CLIENT_ID, USER, PASSWORD, SERVER, PORT

COMMAND_SENDER_URL = f'v1/{USER}/things/{CLIENT_ID}/response'


def connect():
    client = mqtt.Client(CLIENT_ID)
    client.username_pw_set(USER, PASSWORD)
    client.connect(SERVER, PORT)
    return client


def handle_temperature(temperature: int, humidity: int):
    if temperature <= 30:
        temperature = raise_temperature(temperature)
    else:
        temperature = drop_temperature(temperature)
    return temperature, humidity


def handle_message(client, user, msg):
    key, status = msg.payload.decode().split(',')
    handle_warmer('on' if status == '1' else 'off')
    client.publish(COMMAND_SENDER_URL, key)


def get_value_reciever_url(channel: int):
    return f'v1/{USER}/things/{CLIENT_ID}/cmd/{channel}'


def get_value_sender_url(channel: int):
    return f'v1/{USER}/things/{CLIENT_ID}/data/{channel}'
