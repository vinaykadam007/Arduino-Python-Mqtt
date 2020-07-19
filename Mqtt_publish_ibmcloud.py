from __future__ import print_function
from time import sleep
import paho.mqtt.client as mqtt
import serial
import random
import json
# serialPort = serial.Serial(port = "COM5", baudrate=9600,
#                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

# serialString = ""   




ORG = ""
DEVICE_TYPE = "" 
TOKEN = ""
DEVICE_ID = ""


server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/status1/fmt/json";
# pubTopic2 = "iot-2/evt/status2/fmt/json";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;
 


mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

while True:
    #  if(serialPort.in_waiting > 0):
        
    #     # Read data out of the buffer until a carraige return / new line is found
    #     serialString = serialPort.readline()

    #     # Print the contents of the serial data
    #     print(serialString.decode('Ascii'))
    #     # build the payload string

    #     tPayload = int(serialString.decode('Ascii'))
    tPayload = random.randint(1, 100) #{'d':{'temperature':random.randint(1, 50)}}#random.randint(1, 50)

    print(tPayload)
    mqttc.publish(pubTopic1, tPayload)
    # mqttc.publish(pubTopic2, humidity)
    print ("Published")
    sleep(5);


mqttc.loop_forever()

