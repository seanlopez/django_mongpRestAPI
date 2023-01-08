from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_home),   # http://localhost:8000/api   home path
    path('getDB/', views.get_db_name),
    path('createDocument/', views.create_document),
    path('deleteDocument/', views.delete_all_document),
]