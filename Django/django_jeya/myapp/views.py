from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

def welcome(request):
    result=os.path.join(BASE_DIR, "template")
    print(result)
    return render(request,'welcome.html')
def product(request):
    mobile=int(request.GET["mobile"])
    keyboard =int( request.GET["keyboard"])
    monitor = int(request.GET["monitor"])
    price=mobile+keyboard+monitor
    return render(request,'result.html',{"name":price})