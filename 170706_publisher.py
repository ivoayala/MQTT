#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time #import time module
# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
while client.loop()==0:
	client.publish("topic/test", "Hello world!");
	time.sleep(1) #sleep for 10 secs before next call

client.disconnect();
