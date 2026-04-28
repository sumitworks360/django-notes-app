from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_note, name='create_note'),
    path('', views.notes_list, name='notes_list'),
]
