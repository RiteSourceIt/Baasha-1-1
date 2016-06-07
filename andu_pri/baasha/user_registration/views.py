from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

class LoginForm(forms.Form):
    username=forms.EmailField(label="Email")
    password=forms.CharField(widget=forms.PasswordInput(),label="Password")
    
class SignUpForm(forms.Form):
    first_name=forms.CharField(max_length=30,error_messages={'required':'Please enter your  first name'})
    last_name=forms.CharField(max_length=30,error_messages={'required':'Please enter your  last name'})
    username=forms.EmailField(error_messages={'required':'Please enter your  email'})
    password=forms.CharField(widget=forms.PasswordInput())
    
# Create your views here.
def index(request):
    
    if request.method=="POST":
        
        form=LoginForm(request.POST)
        if form.is_valid():
            username,pwd=request.POST.get("username",None),request.POST.get("password")
            if not username or not pwd:
                return HttpResponse("Username or password not present")
            try:
                user=User.objects.get(username=username)
            except ObjectDoesNotExist,ex:
                return redirect("signmeup")
            if user:
                user=authenticate(username=username,password=pwd)
            else:
                return redirect("signmeup")
                 
            login(request,user)           
            return redirect("dashboard")
        else:
            template=loader.get_template("index.html")
            context = {'form':form}
            return HttpResponse(template.render(context,request))    
    else:
        template=loader.get_template("index.html")
        context = {'form':LoginForm()}
        return HttpResponse(template.render(context,request))

@login_required(login_url="/register/index/")
def dashboard(request):
    user= request.user
    template=loader.get_template("dashboard.html")
    context = {'user':user}
    return HttpResponse(template.render(context,request))

def signmeup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            first_name,last_name,username,pwd=request.POST.get("first_name",None),request.POST.get("last_name",None),request.POST.get("username",None),request.POST.get("password")
            #if not first_name or not last_name or not username or not pwd:
                #return HttpResponse("Username or password not present")
            user=User.objects.create_user(username,username,pwd)
            user.last_name=last_name
            user.first_name=first_name
            user.save()
            user=authenticate(username=username,password=pwd)
            login(request,user)
            #return redirect("index")
            return redirect("dashboard")        
           
        else:
            template=loader.get_template("signmeup.html")
            context = {'form':form}
            return HttpResponse(template.render(context,request))    
    else:
        template=loader.get_template("signmeup.html")
        context = {'form':SignUpForm()}
        return HttpResponse(template.render(context,request))
    
def dologout(request):
    logout(request)
    return redirect("index")
        