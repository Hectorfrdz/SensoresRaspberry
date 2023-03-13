import time
from sensores import Sensor
import json
from aJson import Sensores
class main:

    def __init__(self):
        self.sensores = Sensores()
        self.bandera = 0
        self.dispositivo = ""
        self.tiempoEspera = 120  # tiempo en segundos
        self.timer_count = 0  # contador de tiempo para borrar historial local
        self.veces = 2
        self.colecion = "Sensores"

    def main(self):
        opcion = ""
        while opcion != "2":
            opcion = self.menu()
            if opcion == "1":
                self.juntos()
            elif opcion == "2":
                # Salir
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")

    def lectura2(self):            
        print("|{:<3} | {:<20} | {:<25} | {:<11} | {:<10} | {:<10} | {:<5}|".format("#", "Nombre", "Tipo", "Valores",
                                                                                    "Fecha", "Hora", "Pines"))
        while True:  # tiempo en segundos
            # aux = self.sensores.mostrar()
            # if len(aux) >= 1:
            #     ubi = len(aux) - 1
            #     if self.obj.find_one(self.colecion, aux[ubi]):
            #         pass
            #     else:
            #         self.obj.insert_one(self.colecion, aux[ubi])

            i = self.juntos()
            self.sensores.agregar(i)

    def juntos(self):
        temp = Sensor("tmp", [5], "temperatura")
        ult = Sensor("ult",[23,24],"ultrasonico")
        led = Sensor("led",[27],"led")
        sensores=[led]
        # sensores=[temp]
        i=0
        for sens in sensores:
            i=i+1
            # print(sens.lectura())
            data=json.loads(sens.lectura())
            if len(data["valores"]) == 1:
                if len(data["pines"]) == 1:
                    print("|{:<3} | {:<20} | {:<25} | {:<10} | {:<10} | {:<5}|".format(i,data["nombre"], data["tipo"],
                                                                                    data["valores"][0],
                                                                                    data["fecha"],
                                                                                    data["pines"][0]))
                elif len(data["pines"]) == 2:
                    print(
                        "|{:<3} | {:<20} | {:<25} | {:<10} | {:<10} | {:<2} {:<2}|".format(i,data["nombre"],
                                                                                        data["tipo"],
                                                                                        data["valores"][0],
                                                                                        data["fecha"],
                                                                                        data["pines"][0],
                                                                                        data["pines"][1]))
            elif len(data["valores"]) == 2:
                if len(data["pines"]) == 1:
                    print("|{:<3} | {:<20} | {:<25} | {:<4} {:<5} | {:<10} | {:<5}|".format(i,data["nombre"], data["tipo"], data["valores"][0],
                                                                    data["valores"][1],
                                                                    data["fecha"], data["pines"][0]))
                elif len(data["pines"]) == 2:
                    print(
                        "|{:<3} | {:<20} | {:<25} | {:<4} {:<5} | {:<10} | {:<2} {:<2}|".format(i,data["nombre"], data["tipo"], data["valores"][0],
                                                                    data["valores"][1],
                                                                    data["fecha"], data["pines"][0],data["pines"][1]))

    def menu(self):
        print("------------Menu------------")
        print("1. Leer Sensores")
        print("2. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion


if __name__ == "__main__":
    main().main()
