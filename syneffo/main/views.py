from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(Request):
    return render(Request,'index.html')

def student(Request):
   
   std=student.object.all()
   return render(Request,'studentlist.html',{'std':std})
