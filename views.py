from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserSignup
from .forms import UsForm, Uslogin

from django.contrib import messages
# Create your views here.
def home(request):

      return render(request, 'authentication/index.html')


def signup(request):

    if request.method == "POST":
        form = UsForm(request.POST)
        if form.is_valid():
            form.save()

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # usersignup = UserSignup(username='username', fname='fname',lname='lname',email='email',pass1='pass1')
        # usersignup.save()

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.pass2 = pass2

        myuser.save()
        messages.success(request, 'your account has been succesfuly created.')
        return redirect('signin')


    return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == "POST":
        form = Uslogin(request.POST)
        if form.is_valid():
            form.save()


        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"authentication/index.html",{'fname': fname})

        else:
            messages.error(request,"bad credentials")
            return redirect('home')



    return render(request, 'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request,"you are successfully loggedout")
    return redirect('home')
    # return render(request, 'authentication/signout.html')
