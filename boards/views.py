from django.shortcuts import render
from django.http import HttpResponse
from .models import Boards

# Create your views here.

def home (request):
    board = Boards.objects.all()
    return render(request,'board.html',{'board':board})
   
