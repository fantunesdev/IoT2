import time

from hal import get_actual_weather
from my_conf import CLIENT_ID1, CLIENT_ID2
from repository import *


temperature, humidity = get_actual_weather()

client1 = connect(CLIENT_ID1)
client2 = connect(CLIENT_ID2)


client1.on_message = handle_message
client1.subscribe(get_value_reciever_topic(CLIENT_ID1, 2))
client1.loop_start()


client2.on_message = handle_message
client2.subscribe(get_value_reciever_topic(CLIENT_ID2, 2))
client2.loop_start()

while True:
    client1.publish(get_value_sender_topic(CLIENT_ID1, 0), temperature)
    client1.publish(get_value_sender_topic(CLIENT_ID1, 1), humidity)
    client2.publish(get_value_sender_topic(CLIENT_ID2, 0), temperature)
    client2.publish(get_value_sender_topic(CLIENT_ID2, 1), humidity)
    temperature, humidity = handle_temperature(temperature, humidity)
    time.sleep(10)

# client.disconnect()
