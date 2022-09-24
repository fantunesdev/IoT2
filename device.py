import time

from hal import get_actual_weather
from my_conf import CLIENT_IDS
from repository import *

temperature, humidity = get_actual_weather()

clients = []

for client_id in CLIENT_IDS:
    client = connect(client_id)
    clients.append(client)

    client.on_message = handle_message
    client.subscribe(get_value_reciever_topic(client_id, 2))
    client.loop_start()

while True:
    for client in clients:
        client_id = client._client_id.decode('UTF-8')
        client.publish(get_value_sender_topic(client_id, 0), temperature)
        client.publish(get_value_sender_topic(client_id, 1), humidity)
    temperature, humidity = handle_temperature(temperature, humidity)
    time.sleep(3)

# client.disconnect()
