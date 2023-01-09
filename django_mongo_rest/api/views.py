from django.shortcuts import render
from django.http import JsonResponse
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mongoOperation import mongoConnection, mongoCRUD

# Connect to Mongo
mongoDB_class = mongoConnection.mongoConnection()
mongoDB = mongoDB_class.mongoConn()

# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    print(request.GET)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data["content-type"] = request.headers["Content-Type"]
    data["param"] = request.GET
    print(request.headers)
    return Response(data)

@api_view(['GET'])
def get_db_name(request, *args, **kwargs):
    try:
        return Response({"db_names": mongoDB.list_database_names()})
    except Exception as e:
        return Response({"error": str(e)})

@api_view(['POST'])
def create_document(request, *args, **kwargs):
    try:
        # receive the post body from the request
        document = json.loads(request.body)

        # print(document)

        # receive the collection name from headers
        headers = request.headers
        collectionName = headers["collectionname"]

        # add the document into the target collection of DB
        documentCreate = mongoCRUD.createDocument(mongoDB, mongoDB_class.getDBName(), collectionName, document)

        return Response({"status": documentCreate})
    except Exception as e:
        return Response({"error": str(e)})

@api_view(['POST'])
def delete_all_document(request, *args, **kwargs):
    try:
        # receive the collection name from headers
        headers = request.headers
        collectionName = headers["collectionname"]

        # add the document into the target collection of DB
        documentDelete = mongoCRUD.deleteAllDocument(mongoDB, mongoDB_class.getDBName(), collectionName)

        return Response({"status": documentDelete})
    except Exception as e:
        return Response({"error": str(e)})

