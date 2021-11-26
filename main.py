import grovepi
import math
import os
from numpy.core.arrayprint import DatetimeFormat
import paho.mqtt.publish as publish
from scipy.io import savemat

TOPIC = '/topic/test'
BROKER_ADDRESS = "servertim"
PORT = 9876
QOS = 0

print("Verbunden mit MQTT Broker: " + BROKER_ADDRESS)
DATA = "Hello"

publish.single('topic/test', "Hi", hostname="servertim", port=9876)

white = 1   # The White colored DHT sensor.
dht_pin = 4
piezo_pin = 2

#def write_mat_file(filename, ):

def send_to_mqtt():
    print(" ")
def read_sensors():
    print(" ")
while True:
    try:
        [temp,humidity] = grovepi.dht(dht_pin,white)
        infrared_temp = (grovepi.analogRead(16) - 32)/1.8000
        vibration = grovepi.analogRead(piezo_pin)

        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
        #    publish.single('topic/test', str( "temp = %.02f C humidity =%.02f%%"%(temp, humidity)), hostname="servertim", port=9876)
        
        
        print("Infrared_Temp = %.02f"%infrared_temp)
        #publish.single('topic/test', str("Infrared_Temp = %.02f"%infrared_temp), hostname="servertim", port=9876)
        print("Piezo Vibration: " + str(vibration))
        publish.single('topic/test', str("Piezo Vibration: " + str(vibration)), hostname="servertim", port=9876)

    except IOError:
        print("Error")
