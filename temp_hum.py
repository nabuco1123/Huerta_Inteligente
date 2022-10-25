import Adafruit_DHT  
import time  
import sys
import requests


sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
pin = 4 #Pin en la raspberry donde conectamos el sensor


while True:
  
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    
    if humedad is not None and temperatura is not None:
        
        print(f'Temperatura={temperatura:.2f}*c    Humedad={humedad:.2f}%')
  
    else:
        print('Fallo la lectura del sensor.Intentar de nuevo')

    enviar = requests.get("https://api.thingspeak.com/update?api_key=KW10LQU2H48L4ZRV&field1="
                        +str(temperatura)+"&field2="+str(humedad))

time.sleep(5) 