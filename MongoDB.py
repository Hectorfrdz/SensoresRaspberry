import json
import os

from pymongo import MongoClient


class MongoDB:

    def __init__(self):
        self.client = ""
        self.conexion = "mongodb+srv://Hector:4789108flores@cluster0.hojniek.mongodb.net/?retryWrites=true&w=majority"
        self.db=None

    def conectarBD(self):
        try:
           client = MongoClient(self.conexion)
           client.server_info()
           self.client=client["RaspSensores"]
           print("Hay Conexion a Internet")
           return True
        except Exception:
            print("No hay Conexion")
            return False

    def insertarMuchos(self,data=[]):
        if len(data)>0:
            collection_name=self.client["Sensores"]
            for item in data:
                collection_name.insert_one(item)
        else:
            pass

    def insertarUno(self,data={}):
        collection_name=self.client["Sensores"]
        collection_name.insert_one(data)

    def insert_one(self, collection, data):
        coll = self.db[collection]
        coll.insert_one(data)
        if self.find_one(collection,data):
            return True
        else:
            return False

    def find_one(self, collection, query={}):
        coll =self.client["Sensores"]
        return coll.find_one(query)
    
    def insert_one(self, collection, data):
        coll =self.client["Sensores"]
        coll.insert_one(data)
        if self.find_one(collection,data):
            return True
        else:
            return False
