#from http.client import HTTPResponse
from asyncio import all_tasks
from cmath import log
import imp
from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    # if post request, post user input to database
    if request.method == "POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            # delay save option access manage field and save new value
            instance=form.save(commit=False)
            instance.manage=request.user
            instance.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
        # get all the objects of this class i.e tasks and done status
        all_tasks=TaskList.objects.filter(manage=request.user)
        #paginator logic
        #1. create paginator after each 5 objects
        paginator=Paginator(all_tasks, 5)
        # get pages to populate URL
        page=request.GET.get('pg')
        # get our tasks 
        all_tasks=paginator.get_page(page)
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

@login_required
def delete_task(request,task_id):
    # connect to db i.e select task
    task=TaskList.objects.get(pk=task_id)
    # check if the logged in user is the owner of the deleted tasks
    if task.manage == request.user:
        # delete selected task
        task.delete()
    else:
        messages.error("Not allowed to delete posts!")
    # return todolist page
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    # if post request, post user input to database
    if request.method == "POST":
        # select the task
        task_obj_edit=TaskList.objects.get(pk=task_id)
        # use the instance parameter to use the same task instance that we're using to query the selected task
        form=TaskForm(request.POST or None,instance=task_obj_edit)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited!"))
        return redirect('todolist')
    else:
        # get all the objects of this class i.e tasks and done status
        task_object=TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_object':task_object})

@login_required
def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    # check if the logged in user is the owner of the task
    if task.manage == request.user:
        task.done= True
        task.save()
    else:
        messages.error(request,("Access restricted, not allowed"))
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done= False
    task.save()
    
    return redirect('todolist')

@login_required
def index(request):
    context={
        'index_text':"Welcome Index page",
    }
    return render(request,'index.html',context)