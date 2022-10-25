import Adafruit_DHT  
import time  
import sys


sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
pin = 4 #Pin en la raspberry donde conectamos el sensor


while True:
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

  print ( 'Temperatura = {0:0.1f}   Humedad = {1:0.1f}%'.format(temperatura, humedad ))
 
  time.sleep(5) 