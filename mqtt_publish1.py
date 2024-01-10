import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "0.0.0.0"
client = mqtt.Client("depth-inside")
client.connect(mqttBroker, 1820, 60)
client.loop_start()

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    #print(type(randNumber))
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(0.1) 
