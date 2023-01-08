from pymongo import MongoClient
import urllib.parse
import json


class mongoConnection(object):
    def __init__(self):
        connection_info_file = open("./static/mongoInfo.json", "r")
        self.connection_info = json.loads(connection_info_file.read())
        connection_info_file.close()
        self.username = urllib.parse.quote_plus(self.connection_info["username"])
        self.password = urllib.parse.quote_plus(self.connection_info["password"])
        self.ipaddress = self.connection_info["mongo_address"]
        self.port = self.connection_info["mongo_port"]
        self.dbName = self.connection_info["dbName"]

    def mongoConn(self):
        mongoDB = MongoClient(f'mongodb://{self.username}:{self.password}@{self.ipaddress}:{self.port}')
        return mongoDB

    def getDBName(self):
        return self.dbName


