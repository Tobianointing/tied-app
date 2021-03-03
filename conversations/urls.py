from django.urls import path
from . import views

urlpatterns = [
    # path('chat/', views.chat, name='chat'),
    path('voice/', views.voice_call, name='voice'),
    # path('chat_detail/', views.chat_detail, name='chat-detail'),
    
]