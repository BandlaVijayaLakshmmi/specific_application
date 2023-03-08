from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def life(request):
    return HttpResponse('<h1><marquee>focus on making yourself better,not on thinking that you are better.</marquee></h1>')
def abd(request):
    return HttpResponse('hii!!!')