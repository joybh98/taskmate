#from http.client import HTTPResponse
from asyncio import all_tasks
from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import TaskList
# Create your views here.

def todolist(request):
    # get all the objects of this class i.e tasks and done status
    all_tasks=TaskList.objects.all

    return render(request,'todolist.html',{'all_tasks':all_tasks})

def contact(request):
    context={
        'welcome_text':"Contact Page",
        }
    return render(request,'contact.html',context)

def about(request):
    context={
        'welcome_text':"About Us",
        }
    return render(request,'about.html',context)