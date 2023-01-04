# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('produto/<int:pk>', views.ver_produto, name='ver_produto'),

]