import json

class Json:
    def __init__(self,ruta):
        self.ruta = ruta

    def leerArchivos(self):
        with open(self.ruta,'r') as archivo:
            datos = json.load(archivo)
            return datos

    def archivo(self):
        with open(self.ruta, 'r') as archivo:
            datos = json.load(archivo)
            return datos
            
    
    def crearArchivos(self,datos):
        with open(self.ruta, 'w') as archivo_nuevo:
            json.dump(datos, archivo_nuevo,indent=4)
