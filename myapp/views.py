from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.

def index(request):
    profile=Profile.objects.get()
   

    return render(request, 'index.html',{'profile':profile})
 
# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html',{'count':amount_of_words})