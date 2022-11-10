import email
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from Geri import models

# Create your views here.
def index(request):
    #return HttpResponse("This is the ICOPE Screening Tool HomePage for Geri Care Hospital ")
    context= { 'Test' : ' ICOPE '} 
    return render(request, 'geri.html', context)

def test(request):
    if request.method=="POST":
        email=request.POST['email']
        phone=request.POST['phone']
        firstname=request.POST['firstname']
        secondname=request.POST['secondname']
        medhistory=request.POST['medhistory']
        concerns=request.POST['concerns']
        print(email, phone, firstname, secondname, medhistory, concerns)
        ins = models.test(firstname=firstname , secondname=secondname, email=email, phone=phone, medhistory= medhistory, concerns=concerns )
        ins.save()
        print("The data has been written to the db")

    #return HttpResponse("This is a software engineering project developed by Team Pythons.")
    return render(request, 'test.html')
    
def about(request):
    return render(request, 'about.html')

def MiniCog(request):
    return render(request, 'MiniCog.html')

def Mns(request):
    return render(request, 'Mns.html')

def Gds(request):
    return render(request, 'Gds.html')