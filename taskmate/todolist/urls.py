from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist,name='todolist'),
    path('contact', views.contact,name='contact'),
    path('about', views.about,name='about')
]