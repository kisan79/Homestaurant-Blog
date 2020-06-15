from django.urls import path

from blog import views

urlpatterns=[
    path('',views.siteIndex,name='home'),
    path('admin_login_check/',views.admin_login_check,name='admin_login_check'),
    path('blog/',views.blogHome,name='blog')
]