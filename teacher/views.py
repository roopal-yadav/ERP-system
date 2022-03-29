from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    d={'insert':"hello buddy"}
    return render(request,'login.html')
    #return render_to_response('home.html')

# Create your views here.
