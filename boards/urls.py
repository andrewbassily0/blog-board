from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about' , views.about, name='about'),
    path('boards/<int:boards_id>', views.boards_topics, name='boards'),
]