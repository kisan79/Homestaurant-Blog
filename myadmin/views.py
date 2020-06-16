# myadmin view

from django.shortcuts import render,redirect
from .forms import AdminRegisterForm
from .models import Admin
from django.contrib import messages
from blog.forms import PostForm
from django.http import HttpResponse

# Create your views here.

def adminHome(request):
    '''This fn checks whether there is session or not and redirects accordingly'''
    session = request.session['status']
    if session:
        qs=Admin.objects.get(mobile=session)
        return render(request, 'myadmin/adminHome.html', {'form': AdminRegisterForm(), 'qs': qs})
    return render(request, 'myadmin/adminHome.html')


def adminLogout(request):
    '''Function For Admin Logout'''
    request.session['status']= False
    return redirect('blog:sitehome')

def save_admin(request):
    '''Function For Registering New Admins and Save To Admin Model'''
    arf=AdminRegisterForm(request.POST,request.FILES)
    if arf.is_valid():
        arf.save()
        messages.success(request,'Registered Successfully')
        return redirect('adminHome')
    messages.error(request,'Something Went Wrong...Please Try Again')
    return render(request,'myadmin/adminHome.html',{'form':arf})


def create_post(request):
    '''function To Create A Blog-Post'''
    #If Session is There then send Users data to template if not the time-out
    session=request.session['status']
    if session:
        return render(request,'myadmin/create_post.html',{'form':PostForm(),'qs':Admin.objects.get(mobile=session)})
    return render(request,'myadmin/create_post.html')


def save_post(request):
    '''Function For Saving Blog-Post'''
    pf=PostForm(request.POST,request.FILES)
    if pf.is_valid():
        save_ref=pf.save()
        save_ref.save()
        if pf.cleaned_data['status'] == 'published':
            messages.success(request,'Post Is Published!!!You can See in Blogs...')
        else:
            messages.info(request,'Post Is Saved As Draft!!!You Can Publish it later...')
        return redirect('create_post')
    return render(request,'myadmin/create_post.html',{'form':pf})