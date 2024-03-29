from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .models import teacherlogin
from branch.models import subjects,branch_detail

def index(request):
    return render(request,'login.html')
    #return render_to_response('home.html')

# Create your views here.
#for login
from .models import teacherlogin

def login(request):
        if request.method == 'POST':
            username = request.POST.get('teacherid')
            password = request.POST.get('teacherpwd')
            try:
                user = teacherlogin.teach_obj.get(teacherid=username,teacherpwd=password)
                if user is not None:
                    return render(request, 'dash1.html', {})
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
                    return redirect('/')
            except Exception as identifier:
                return redirect('/teacher')
        else:
            return render(request,'login.html')
def logout(request):
    logout(request)

def tt(request):
    return render(request,'timetable.html')