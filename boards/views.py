from django.shortcuts import render
from django.http import HttpResponse ,Http404
from .models import Boards


# Create your views here.

def home (request):
    board = Boards.objects.all()
    return render(request,'board.html',{'board':board})


def boards_topics(request , boards_id):
    try:
     board =Boards.objects.get(pk=boards_id)
    except Boards.DoesNotExist: 
     raise Http404
    return render (request,'topics.html' , {'boards':board})


def about (request):
    return HttpResponse('My name is Andrew ')
   
