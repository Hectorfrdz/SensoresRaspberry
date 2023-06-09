import json
import os

class Json:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def guardar_a_json(self, datos):
        with open(self.nombre_archivo, 'w') as archivo_json:
            json.dump(datos, archivo_json,indent=4)

    def leer_de_json(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo_json:
                datos = json.load(archivo_json)
            return datos
        except FileNotFoundError:
            with open(self.nombre_archivo, 'w') as archivo_json:
                json.dump([], archivo_json)
            return []


    def clear_all_files(self):
        """
        Función para vaciar todos los archivos JSON
        """
        for file in os.listdir():
            if file.endswith(".json"):
                os.remove(file)

    def clearFille(self,archivo):
        os.remove(archivo)
