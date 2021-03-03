from django.shortcuts import render
from .models import(#Chat,
 VoiceCall)

# Create your views here.
# def chat(request):
#     chats = Chat.objects.all()
#     context = {
#         'chats': chats
#     }
#     return render(request, 'conversations/chat.html', context)

def voice_call(request):
    voice_call = VoiceCall.objects.all()
    context = {
        'voice_calls': voice_call
    }
    return render(request, 'conversations/voice.html', context)

# def chat_detail(request):
#     return render(request, 'conversations/chat_deatil.html')