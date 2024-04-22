from django.shortcuts import render
from django.http import HttpResponse
from foodapp.models import details
from foodapp.models import data
# Create your views here.
def fun(request):
    return HttpResponse('hello from django response')
def wellcome_messege(request):
    return HttpResponse('wellcome to kodnest.....!!')
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method==('POST'):
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        register=details(email=email,phone=phone)
        register.save()
    return render(request,'registration.html')
def web2(request):
    if request.method==('POST'):
        name2=request.POST.get('name2')
        email2=request.POST.get('email2')
        phone2=request.POST.get('phone2')
        web2=data(name2=name2,email2=email2,phone2=phone2)
        web2.save()
    return render(request,'web2.html')

    
    