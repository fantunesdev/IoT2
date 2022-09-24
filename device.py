import time

from hal import get_actual_weather
from repository import connect, handle_temperature, handle_message, get_value_reciever_url, get_value_sender_url


temperature, humidity = get_actual_weather()

client = connect()

client.on_message = handle_message
client.subscribe(get_value_reciever_url(channel=2))
client.loop_start()


while True:
    client.publish(get_value_sender_url(channel=0), temperature)
    client.publish(get_value_sender_url(channel=1), humidity)
    temperature, humidity = handle_temperature(temperature, humidity)
    time.sleep(10)

# client.disconnect()
