from __future__ import print_function
import paho.mqtt.publish as publish

import serial

serialPort = serial.Serial(port = "COM5", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""                           # Used to hold data coming over UART

channelID = ""

apiKey = ""

useUnsecuredTCP = True

useUnsecuredWebsockets = True

useSSLWebsockets = False

mqttHost = "mqtt.thingspeak.com"

if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443
        
top = "home/mqtt/"
topic = "channels/" + channelID + "/publish/" + apiKey
topic1 = "channels/" + channelID + "/publish/" + apiKey

while(True):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        print(serialString.decode('Ascii'))
        serialstr = str(serialString.decode('Ascii'))
        # serialstr.split(",")
        tPayload = "field1=" + str(serialstr)
        
        # tPayload1 = "field2=" + str(2)

        # attempt to publish this data to the topic 
        try:
            publish.single(top, payload=tPayload, hostname=mqttHost, port=tPort, transport=tTransport)
            # publish.single(topic1, payload=tPayload1, hostname=mqttHost, port=tPort, transport=tTransport)

        except (KeyboardInterrupt):
            break

        # except:
        #     print ("There was an error while publishing the data.")