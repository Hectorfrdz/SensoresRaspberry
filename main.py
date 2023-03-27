import time
from sensores import sensor
import json
from aJson import Sensores
import threading
from MongoDB import MongoDB
class main:
    def __init__(self):
        self.conexion = MongoDB()
        self.sensores = Sensores()
        self.bandera = 0
        self.dispositivo = ""
        self.tiempoEspera = 120  # tiempo en segundos
        self.timer_count = 0  # contador de tiempo para borrar historial local
        self.veces = 2
        self.colecion = "Sensores"
        self.bandera2 = 0

    def contador(self, tiempo):
        for i in range(tiempo, -1, -1):
            time.sleep(1)
        return True
    def main(self):
        opcion = ""
        while opcion != "5":
            opcion = self.menu()
            if opcion == "1":
                self.sensoresLectura()
            # if opcion == "2":
            #     interBD().mainBd()
            # elif opcion == "7":
            #     self.juntos()
            elif opcion == "2":
                # Salir
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")

    def sensoresLectura(self):
        if self.conexion.conectarBD():
            self.bandera2 = 1 
        temp = sensor("tmp", [5], "Temperatura/Humedad")
        ult = sensor("ult",[23,24],"Ultrasonico")
        led = sensor("led",[27],"Led")
        sensores=[temp,led, ult]
        # sensores=[temp]
        z=0
        if self.bandera2 == 1:  # si esta en conexion
            lista = self.sensores.mostrar()
            if len(lista) >= 1:  # si la lista de sensores tiene objetos, debe ingresarlos a la bd antes de los otros
                for x in lista:
                    if self.conexion.find_one(self.colecion, x):
                        pass
                    else:
                        self.conexion.insert_one(self.colecion, x)
                self.sensores.borrarInfo("Sensores.json")
            self.hiloBorrarPTiempo()
        while True:
            for sens in sensores:
                z=z+1
                # print(sens.lectura())
                data=json.loads(sens.lectura())
                if len(data)>=1:
                    for i in data:
                        # print(i)
                        # i es el json
                        if len(i["pines"]) == 1:
                            # print(i["nombre"])
                            # print(i["tipo"])
                            # print(i["valores"])
                            # print(i["dato"])
                            # print(i["fecha"])
                            # print(i["pines"][0])
                            print("|{:<3} | {:<20} | {:<25} | {:<7}{:<4} | {:<10} | {:<10} | {:<5}|".format(z, i["nombre"],i["tipo"],i["valores"],i["unidad"],i["fecha"],i["hora"],i["pines"][0]))
                        elif len(i["pines"]) == 2:
                            print("|{:<3} | {:<20} | {:<25} | {:<7}{:<4} | {:<10} | {:<2} {:<2}|".format(z,i["nombre"],i["tipo"],i["valores"],i["unidad"],i["fecha"],i["hora"],i["pines"][0],i["pines"][1]))
                        self.sensores.agregar(i)
                        if self.bandera2==1:
                            # self.guardar(i)
                            self.conexion.insert_one(self.colecion,i)

    def menu(self):
        print("----------------------------------------------")
        self.conexion.conectarBD() 
        print("------------Menu------------")
        print("1. Sensores")
        print("2. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion

    def ultimaLectura(self):
        sensores = self.sensores.from_json()
        print("|{:<25} {:<5}|".format("Sensor", "Valor"))
        for sens in sensores:
            print("|{:<25} {:<5}|".format(sens.nombre, sens.valor))

    def hiloBorrarPTiempo(self):
        timer = threading.Timer(self.tiempoEspera, self.hiloBorrarPTiempo)
        timer.start()

        if self.bandera2 == 1:  # si esta en conexion
            self.timer_count += 1  # incrementa el contador de tiempo
            if self.timer_count >= self.tiempoEspera / 60:  # verifica si han pasado 15 minutos
                self.sensores.borrarInfo("Sensores.json")
                print("Se borro historial local")
                print("---------------------------------------------------------------")
                self.timer_count = 0  # resetea el contador de tiempo
        else:
            print("Se reinicio el contador")
            self.timer_count = 0

if __name__ == "__main__":
    main().main()
    
