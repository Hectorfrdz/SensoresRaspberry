from ultrasonico import UltrasonicSensor
from temperatura import Temperatura
from led import Led
import time
import datetime
from lista import Lista
import os
import json

class Sensor:
    def __init__(self,path="",pin=[],nombre=""):
        self.path=path
        self.pin=pin
        self.nombre=nombre
        if nombre == "":
            self.nombre = self.path
        if self.path == "led":
            self.led1 = Led(self.pin[0])
        self.sensorArreglo = []

    def tipoSensor(self):
        valores=[]
        self.tipo=""

        if self.path == "ultrasonico":
            self.tipo="Ultrasonico"
            sensorUlt = UltrasonicSensor(trigger_pin=self.pin[0], echo_pin=self.pin[1])
            distancia = sensorUlt.medirDistancia()
            valores.append(distancia)

        elif self.path=="humedad":
            self.tipo="Humedad"
            sensor = Temperatura(self.pin[0])
            hum = sensor.lecturaHum()
            if hum is not None and temp is not None:
                valores.append(hum)
        
        elif self.path=="temperatura":
            self.tipo="Temperatura"
            sensor = Temperatura(self.pin[0])
            temp = sensor.lecturaTemp()
            if hum is not None and temp is not None:
                valores.append(temp)


        elif self.path=="led":
            self.tipo="Led"
            stat = self.led1.prenderApagar()
            valores.append(stat)
        return valores

    def lectura(self):
        arreglo = self.tipoSensor()
        timestamp = time.time()
        fecha_hora = datetime.datetime.fromtimestamp(timestamp)
        cadena_fecha_hora = fecha_hora.strftime('%H:%M:%S')

        data={
            "nombre":self.nombre,
            "tipo":self.tipo,
            "valores":arreglo,
            "fecha":cadena_fecha_hora,
            "pines":self.pin
        }
        jsonS=json.dumps(data)
        return jsonS
