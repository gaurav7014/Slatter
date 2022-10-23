from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name="getroutes"),
    path('rooms/', views.getRooms,name="getrooms"),
    path('rooms/<str:pk>/', views.getRoom,name="getroom"),
]
