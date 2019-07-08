#!/usr/bin/env python
#
# !!! Needs psutil (+ dependencies) installing:
#
#    $ sudo apt-get install python-dev
#    $ sudo pip install psutil
#

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageFont
import paho.mqtt.client as mqtt



oled = ssd1306(port=0, address=0x3C)

font = ImageFont.load_default()
font2 = ImageFont.truetype('C&C Red Alert [INET].ttf', 18)

 
MQTT_SERVER = "mqtt.aziot.org"
MQTT_PATH = "PRICE"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(MQTT_PATH)
        client.subscribe("NUMBERPLATE")        
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

        x = msg.payload.split(",")
        if(len(x)==2):
                with canvas(oled) as draw:
                        draw.text((0, 0), "Channel "+msg.topic , font=font2, fill=255)
                        draw.text((0, 22), "Item " +x[0], font=font2, fill=255)
                        draw.text((0, 40), "Price "+x[1], font=font2, fill=255)
                        #draw.text((0, 38), network('wlan0'), font=font2, fill=255)

        if(len(x)==1):
                with canvas(oled) as draw:
                        draw.text((0, 0), msg.topic , font=font2, fill=255)
                        draw.text((0, 22), x[0], font=font4, fill=255)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()



