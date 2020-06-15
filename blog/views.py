#blog View

from django.http import HttpResponse
from django.shortcuts import render,redirect
from myadmin.forms import AdminLoginForm
from myadmin.models import Admin
from django.contrib import messages
from .models import Post

# Create your views here.
def siteIndex(request):
    return render(request,'blog/index.html',{'form':AdminLoginForm()})


def admin_login_check(request):
    '''Admin Login Credentials Validation'''
    username=request.POST['username']
    password=request.POST['password']
    try:
        login_qs=Admin.objects.get(username=username,password=password)
        request.session['status'] = login_qs.mobile
        return redirect('adminHome')
    except Admin.DoesNotExist:
        messages.error(request,'Wrong Username or Password')
        return redirect('home')


def blogHome(request):
    '''Showing All The Published Blog-Posts'''
    return render(request,'blog/blog.html',{'published_blogs':Post.objects.all()})