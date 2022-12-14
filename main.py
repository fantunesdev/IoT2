import time

from my_conf import CLIENT_IDS
from repository import *

# Instanciando todos os clientes

clients = []

for client_id in CLIENT_IDS:
    client = connect(client_id)
    clients.append(client)

    client.on_message = handle_message
    client.subscribe(get_value_reciever_topic(client_id, 2))
    client.loop_start()

# Obtendo a temperatura, a humidade de Curitiba e enviando para o Cayeene

actual_temperatrure = weather_temperature
clients[0].publish(get_value_sender_topic(CLIENT_IDS[0], 3), actual_temperatrure)

# Obtendo e enviando os dados das estufas para o Cayenne. Validando as ações das estufas.

while True:
    for client in clients:
        client_id = client._client_id.decode('UTF-8')
        temperature, humidity = handle_temperature(client_id)
        client.publish(get_value_sender_topic(client_id, 0), temperature)
        client.publish(get_value_sender_topic(client_id, 1), humidity)
    time.sleep(2)

# client.disconnect()
