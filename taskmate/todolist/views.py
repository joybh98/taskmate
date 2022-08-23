#from http.client import HTTPResponse
from asyncio import all_tasks
from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages

# Create your views here.

def todolist(request):
    # if post request, post user input to database
    if request.method == "POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
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

def delete_task(request,task_id):
    # connect to db i.e select task
    task=TaskList.objects.get(pk=task_id)
    # delete selected task
    task.delete()
    # return todolist page
    return redirect('todolist')

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

def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done= True
    task.save()

    return redirect('todolist')

def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done= False
    task.save()
    
    return redirect('todolist')