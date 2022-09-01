from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomerRegisterForm

# Create your views here.
def register(request):
    # check method
    if request.method=="POST":
        # create new form and send input as POST request
        register_form=CustomerRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created"))
            return redirect('register')
    else:
        register_form=CustomerRegisterForm()
    return render(request,'register.html',{'register_form':register_form})