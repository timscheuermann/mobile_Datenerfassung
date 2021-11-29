import grovepi
import math
import os
import time
import sys
from influxdb import InfluxDBClient
from numpy.core.arrayprint import DatetimeFormat
import paho.mqtt.publish as publish
from scipy.io import savemat

#Influx Config
dbhost = "127.0.0.1"
dbport = 8086
dbuser = "rpi-4"
dbpassword = "rpi-4"
dbname = "sensor_data"
dbinterval = 2.5
dbclient = InfluxDBClient(dbhost, dbport, dbuser, dbpassword, dbname)

#MQTT Config
TOPIC = '/topic/test' #ToDO: Topic variable wird nicht akzeptiert von publish single, Datentyp falsch??
BROKER_ADDRESS = "servertim"
PORT = 9876
QOS = 0

print("Verbunden mit MQTT Broker: " + BROKER_ADDRESS)
DATA = "Hello"

#publish.single('topic/test', "Hi", hostname="servertim", port=9876)

white = 1   # The White colored DHT sensor.
dht_pin = 4
piezo_pin = 2
location = "Büro Tim"
#def write_mat_file(filename, ):

while True:
    sendtime = int(time.time() * 1000000000)
    [temp,humidity] = grovepi.dht(dht_pin,white)
    infrared_temp = (grovepi.analogRead(16) - 32)/1.8000
    vibration = grovepi.analogRead(piezo_pin)
    
    if math.isnan(temp) == False and math.isnan(humidity) == False:
        print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
        #publish.single('topic/test', str( "temp = %.02f C humidity =%.02f%%"%(temp, humidity)), hostname="servertim", port=9876)
    
    print("ok")
    print("Infrared_Temp = %.02f"%infrared_temp)
    #publish.single('topic/test', str("Infrared_Temp = %.02f"%infrared_temp), hostname="servertim", port=9876)
    print("Piezo Vibration: " + str(vibration))
    #publish.single('topic/test', str("Piezo Vibration: " + str(vibration)), hostname="servertim", port=9876)
    data = [
    {
        "measurement": "dht",
            "tags": {
                "location": location,
            },
            "time": sendtime,
            "fields": {
                "temperature": temp,
                "humidity": humidity
            }
    }
    ]
    try:
        if(dbclient.write_points(data)):
            print("Gesendet am " + str(sendtime))
    except:
        print("DHT-Aussetzer aufgetreten!")
    time.sleep(dbinterval)