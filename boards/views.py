from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Boards
from django.contrib.auth.models import User
from .models import Topic,Post
from .form import add_new_topic
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

def new (request , boards_id):
    board = get_object_or_404(Boards, pk= boards_id)
    form = add_new_topic()
    user = User.objects.first()
    if request.method == "post":
       form =add_new_topic(request.post)
    if form.is_valid():
        topic= form.save(commit=False)
        Topic.board = board
        Topic.created_by = user
        Topic.save()

        post = Post.objects.create (
           message = form.cleaned_data.get('message'),
             created_by = User,
             topic = Topic
        )
        return redirect('board_topic' , board_id= board.pk)

    return render (request , 'new.html' , {'board':board , 'form':form})


    
   
