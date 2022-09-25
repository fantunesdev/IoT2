import paho.mqtt.client
import paho.mqtt.client as mqtt

from hal import *
from my_conf import USER, PASSWORD, SERVER, PORT


def connect(client_id: str):
    """
    Conecta ao Cayenne usando o protocolo MQTT e retorna um objeto com a instância de conexão.

    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :return: Instância da conexão.
    """
    client = mqtt.Client(client_id)
    client.username_pw_set(USER, PASSWORD)
    client.connect(SERVER, PORT)
    return client


def handle_temperature(client_id: str):
    """
    Obtém a temperatura e a umidade das estufas, faz a validação dos dados e eleva ou subtrai a temperatura da estufa.

    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :return: retorna o valor da temperatura e o valor da umidade atual dentro da estufa.
    """
    greenhouse_temperature = get_greenhouse_temperature(client_id)
    greenhouse_humidity = get_greenhouse_humidity(client_id)
    greenhouse_warmer = get_warmer(client_id)
    if greenhouse_temperature < 30 and greenhouse_warmer.is_active():
        raise_greenhouse_temperature(client_id)
    else:
        drop_greenhouse_temperature(client_id)
    return greenhouse_temperature, greenhouse_humidity


def handle_message(client: paho.mqtt.client.Client, user, msg):
    """
    Recebe um cliente e uma mensagem. Trata-a para ligar ou desligar o aquecedor.

    :param client: instância do cliente logado no Cayenne.
    :param user:
    :param msg: instância da resposta enviada pelo Cayenne.
    """
    client_id = client._client_id.decode('UTF-8')
    key, status = msg.payload.decode().split(',')
    handle_warmer(client_id, True if status == '1' else False)
    client.publish(get_command_sender_topic(client_id), key)


def get_value_reciever_topic(client_id: str, channel: int):
    """
    Obtém o tópico para recebimento de valores.

    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :param channel: string que seleciona o canal do tópico.
    :return: retorna o tópico.
    """
    return f'v1/{USER}/things/{client_id}/cmd/{channel}'


def get_value_sender_topic(client_id: str, channel: int):
    """
    Obtém o tópico para envio de valores.

    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :param channel: string que seleciona o canal do tópico.
    :return: retorna o tópico.
    """
    return f'v1/{USER}/things/{client_id}/data/{channel}'


def get_command_sender_topic(client_id: str):
    """
    Obtém o tópico para envio de comandos.

    :param client_id: string que contém o client_id do dispositivo no Cayenne.
    :param channel: string que seleciona o canal do tópico.
    :return: retorna o tópico.
    """
    return f'v1/{USER}/things/{client_id}/response'
