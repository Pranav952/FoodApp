from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import decorators
# 

# Create your views here.

def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username},You are currently loggedin')
            form.save()
            return redirect('login')
        
    else:   
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

@decorators.login_required
def profliepage(request):
    return render(request,'users/profile.html')