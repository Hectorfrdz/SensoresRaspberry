import json
import os

from pymongo import MongoClient


class MongoDB:

    def __init__(self):
        self.client = ""
        self.conexion = "mongodb+srv://hector:4789108flores@cluster0.xcrymub.mongodb.net/?retryWrites=true&w=majority"
        self.db=None

    def conectarBD(self):
        try:
           client = MongoClient(self.conexion)
           client.server_info()
           self.client=client["CRUD"]
           print("Hay Conexion a Internet")
           return True
        except Exception:
            print("No hay Conexion")
            return False

    def insertarMuchos(self,data=[]):
        if len(data)>0:
            collection_name=self.client["Productos"]
            for item in data:
                collection_name.insert_one(item)
        else:
            pass

    def insertarUno(self,data={}):
        collection_name=self.client["Productos"]
        collection_name.insert_one(data)

    def insert_one(self, collection, data):
        coll = self.db[collection]
        coll.insert_one(data)
        if self.find_one(collection,data):
            return True
        else:
            return False

    def find_one(self, collection, query={}):
        coll = self.db[collection]
        return coll.find_one(query)
