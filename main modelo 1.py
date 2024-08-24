from wifi_lib import conecta
import urequests
import time
from umqttsimple import MQTTClient
from broker import *
from machine import Pin 

LED = Pin(5, Pin.OUT)

def recebi(topico, msg):
    if msg.decode() == "LIGA":
        LED.on()
    else:
        LED.off()

#teste de conexão
print("Conectando...")
station = conecta ("Wokwi-GUEST","")
if not station.isconnected():
    print("Falha na conexão")
else:
    print("Conectado")
    print("Conectando Broker MQTT")
    client = MQTTClient(mqtt_client_id,
        mqtt_server,
        mqtt_port, 
        mqtt_user,
        mqtt_password)
    client.connect()
    client.set_callback(recebi)
    client.subscribe("pucpr/iotmc/msg_esp32")

    print("Aguardando mensagem...")
    client.sleep(60)
    #for i in range(60):
    #    client.check_msg()
    #    time.sleep(1)
     
    #publicar mensagens
    #client.publish("pucpr/iotmc/","12,37")
    
    #time.sleep(1)   #aguarda envio da informação 

    client.disconnect()
    station.disconnect()