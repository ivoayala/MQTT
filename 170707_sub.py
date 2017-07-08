#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
#  if msg.payload.decode() == "Hello world!":
#	print(str(msg.payload))	#print message sent    
	print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload)) #	
#	print("Yes!")
#    	client.disconnect()

#--------main program------------------------------    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("localhost",1883,60) #local server
client.connect("broker.mqttdashboard.com",1883)

client.subscribe("topic/test")


client.loop_forever()


