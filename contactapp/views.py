from django.shortcuts import render
from contactapp.forms import complaint
from django.conf import settings
import openai

def contact(request):
    return render(request,"contactapp/contact.html")


# --------------------------------------------------------------------------------------------------------------------

def email(request):
    form=complaint
    return render(request,"contactapp/email.html",{"form":form})

def chatbot_view(request):
    return render(request,"contactapp/chatbot.html")









