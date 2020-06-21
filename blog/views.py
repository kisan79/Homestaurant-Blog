#blog View

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
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
        return redirect('blog:sitehome')


def blogHome(request):
    '''Showing All The Published Blog-Posts'''
    return render(request,'blog/blog.html',{'form':AdminLoginForm(),'published_blogs':Post.objects.filter(status='published')})


def detail_post(request,slug):
    '''Function For Detail read Post'''
    blog_post=get_object_or_404(Post,slug=slug)
    return render(request,'blog/blog_detail.html',{'form':AdminLoginForm(),'post':blog_post})


def delete_post(request,id):
    '''Function To Delete Particular Post'''
    get_object_or_404(Post,id=id).delete()

    return redirect('blog:viewPost')