from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   text = """<h1>Hi Rashmi ....simple home page</h1>"""
   return HttpResponse(text)
