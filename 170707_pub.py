#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time #import time module
# This is the Publisher

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = mqtt.Client()
client.on_publish = on_publish
#client.connect("localhost",1883,60)
client.connect("broker.mqttdashboard.com",1883)
client.loop_start()

count = 0
while count < 40:
#while True:
#	client.publish("topic/test", "Hello world!")
	client.publish("topic/test", str(count))
	count +=1
	time.sleep(1) #sleep for 10 secs before next call

client.loop_stop()
client.disconnect();
