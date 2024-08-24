from wifi_lib import conecta
import urequests
from umqttsimple import MQTTClient
import time
from defs import *
from machine import Pin
from servo import Servo

LED = Pin(5, Pin.OUT)
braco = Servo(4)

def recebi(topico, msg):
    braco.set_angle(int(msg.decode()))

print("Conectando...")
station = conecta("Wokwi-GUEST","")
if not station.isconnected():
    print("Falha na conexão")
else:
    print("Conectado wifi")
    print("Conectando Broker MQTT")
    client = MQTTClient(mqtt_client_id,
        mqtt_server,
        mqtt_port,
        mqtt_user,
        mqtt_password)
    client.connect()
    client.set_callback(recebi)
    client.subscribe("pucpr/ioe/botao/afonso")

    for i in range(3*60):
        client.publish("pucpr/ioe/msg_esp32/afonso",f"{i}")
        client.sleep(1)

    client.disconnect()
    station.disconnect()
