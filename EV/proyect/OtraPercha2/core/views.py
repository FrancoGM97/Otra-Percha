from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request): 
    return render(request,"core/home.html") 

def ropa(request): 
    return render(request,"core/ropa.html") 

def entregas(request): 
    return render(request,"core/entregas.html")  

def contacto(request): 
    return render(request,"core/contacto.html")