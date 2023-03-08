from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Life1(request):
    return HttpResponse('<marquee><h2>I WANT OUR RELATIONSHIP TO BE LIKE TOM & JERRY , NO MATTER HOW  MANY TIMES WE FIGHT, WE WONT BE APART....</h2></marquee>')
def life2(request):
    return HttpResponse('<h3>if we do not  stop fighting we will never get anywhere</h3>')