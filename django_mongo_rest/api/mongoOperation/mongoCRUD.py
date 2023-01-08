import pymongo
import json


def createDocument(dbConn, dbName, collectionName, document):
    dbHandler = dbConn[dbName]
    if collectionName in dbHandler.list_collection_names():
        collectionHandler = dbHandler[collectionName]
        collectionHandler.insert_one(document)
        return "created"
    else:
        return "collection is not existing"

def deleteAllDocument(dbConn, dbName, collectionName):
    dbHandler = dbConn[dbName]
    if collectionName in dbHandler.list_collection_names():
        collectionHandler = dbHandler[collectionName]
        x = collectionHandler.delete_many({})
        return f"{x.deleted_count} documents were(was) deleted"
    else:
        return "collection is not existing"
