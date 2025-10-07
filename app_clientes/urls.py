from django.urls import path #añadido todo el documento

from . import views 

urlpatterns = [
    path('', views.index, name='index')
]