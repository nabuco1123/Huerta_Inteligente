import RPi.GPIO as GPIO
import Adafruit_DHT
import smtplib
from email.mime.text import MIMEText
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

sensor = Adafruit_DHT.DHT11
pin_temperatura = 23
correo_origen = 'xxxxxxxx@gmail.com'
contraseña = 'xxxxxxx'
correo_destino = 'xxxxxxxx@gmail.com'
temperatura_umbral = 20

def Enviar_correo(temperatura):

    msg = MIMEText(f"La temperatura esta demasiado alta.la temperatura es de: {temperatura:.2f}°c")
    msg['Subject'] = 'Monitoreo de Temperatura'
    msg['From'] = correo_origen
    msg['To'] = correo_destino
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(correo_origen,contraseña)
    server.sendmail(correo_origen,correo_destino,msg.as_string())
    print("Su Email ha sido enviado.")
    server.quit()

while True:

    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin_temperatura)

    if humedad is not None and temperatura is not None:
        print(f'Temperatura={temperatura:.2f}*c  Humedad={humedad:.2f}%')
    
    else:
        print('Fallo la lectura del sensor.Intentar de nuevo')

    if temperatura > temperatura_umbral:

        GPIO.output(24,True)
        GPIO.output(25,False)
        Enviar_correo(temperatura)
    
    else:

        GPIO.output(24,False)
        GPIO.output(25,True)
    

    time.sleep(5)