import paho.mqtt.client as mqtt

from hal import handle_warmer, raise_temperature, drop_temperature
from my_conf import USER, PASSWORD, SERVER, PORT


def connect(client_id):
    client = mqtt.Client(client_id)
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
    client.publish(get_command_sender_topic(client._client_id.decode('UTF-8')), key)


def get_value_reciever_topic(client_id: str, channel: int):
    return f'v1/{USER}/things/{client_id}/cmd/{channel}'


def get_value_sender_topic(client_id: str, channel: int):
    return f'v1/{USER}/things/{client_id}/data/{channel}'


def get_command_sender_topic(client_id: str):
    return f'v1/{USER}/things/{client_id}/response'
