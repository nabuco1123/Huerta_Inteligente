import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
channel = 4

GPIO.setup(channel, GPIO.IN)

def medirHumedad():
    valor = GPIO.input(4)
    if  valor == 0:
        print("Humedo")
        guardarInfoSensor("0")
    else:
        print("Seco")
        guardarInfoSensor("1")

def crearArchivoCSV():
    filename = "registroHumedadDigital.csv"
    csv = open(filename, 'w')
    csv.write("Timestamp,Humedad\n")
    csv.close

def guardarInfoSensor(valor):
    filename = "registroHumedadDigital.csv"
    humedad = valor
    fecha = str(datetime.datetime.now())
    dato = fecha + "," + humedad + "\n"
    csv = open(filename, "a")
    csv.write(dato)
    csv.close

print("Sensando humedad")
crearArchivoCSV()

while True:
    medirHumedad()
    time.sleep(2)
