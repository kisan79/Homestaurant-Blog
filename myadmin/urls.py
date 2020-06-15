#Admin URL Configuration

from django.urls import path

from myadmin import views


urlpatterns=[
    path('',views.adminHome,name='adminHome'),
    path('adminLogout/',views.adminLogout,name='adminLogout'),
    path('save_admin/',views.save_admin,name='save_admin'),
    path('create_post/',views.create_post,name='create_post'),
    path('save_post/',views.save_post,name='save_post')
]
