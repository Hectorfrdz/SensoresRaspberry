from jsonTest import Json 
import os

class Lista:
    def __init__(self,ruta):
        self.json = Json(ruta)
        self.listas = []

    def agregar(self, datos):
        self.listas.append(datos)
        self.json.crearArchivos(self.listas)

    def mostrar(self):
        return self.json.archivo()

    def actualizar(self,cli,datos):
        if self.listas:
            self.listas[int(cli)] = datos
            self.json.crearArchivos(self.listas)

    def eliminar(self,cli):
        self.listas.pop(int(cli))
        self.json.crearArchivos(self.listas)

    def buscarProds(self,productos):
        datos=self.listas
        productos = productos.split(",")
        productos = [
            int(x) for x in productos
            ]
        productos = [
            datos[x] for x in productos
            ]
        return productos

    def leer(self):
        return self.listas

    def buscar(self,cli):
        return self.listas[int(cli)]

    def buscar2(self,cli):
            return self.listas[int(cli)],0

    def buscarTodo(self, clave, valor):
        filtered_list = [item for item in self.listas if item[clave] == valor]
        if filtered_list:
            id = self.listas.index(filtered_list[0])
            return filtered_list, id
        else:
            return None

    def filter(self, key, value):
        filtered_list = [item for item in self.listas if item[key] == value]
        if filtered_list:
            id = self.listas.index(filtered_list[0])
            return filtered_list, id
        else:
            return None
