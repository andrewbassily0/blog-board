from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Boards


# Create your views here.

def home (request):
    boards = Boards.objects.all()
    return render(request,'board.html',{'boards':boards})

    
def boards_topics(request , boards_id):
    try:
     board = Boards.objects.get(pk=boards_id)
    except Boards.DoesNotExist:
     raise Http404
    return render (request,'topics.html' , {'board':board})


def about (request):
    return HttpResponse('My name is Andrew ')
   
