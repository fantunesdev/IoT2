import paho.mqtt.client as mqtt

from hal import *
from my_conf import USER, PASSWORD, SERVER, PORT


def connect(client_id):
    client = mqtt.Client(client_id)
    client.username_pw_set(USER, PASSWORD)
    client.connect(SERVER, PORT)
    return client


def handle_temperature(client_id):
    temperature = get_temperature(client_id)
    humidity = get_humidity(client_id)
    warmer = get_warmer(client_id)
    if temperature <= 30 and warmer.state:
        raise_temperature(client_id)
    else:
        drop_temperature(client_id)
    return temperature, humidity


def handle_message(client, user, msg):
    client_id = client._client_id.decode('UTF-8')
    key, status = msg.payload.decode().split(',')
    handle_warmer(client_id, True if status == '1' else False)
    client.publish(get_command_sender_topic(client_id), key)


def get_value_reciever_topic(client_id: str, channel: int):
    return f'v1/{USER}/things/{client_id}/cmd/{channel}'


def get_value_sender_topic(client_id: str, channel: int):
    return f'v1/{USER}/things/{client_id}/data/{channel}'


def get_command_sender_topic(client_id: str):
    return f'v1/{USER}/things/{client_id}/response'
