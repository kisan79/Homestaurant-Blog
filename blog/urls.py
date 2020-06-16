from django.urls import path

from blog import views

app_name='blog'

urlpatterns=[
    path('', views.siteIndex, name='sitehome'),
    path('admin_login_check/',views.admin_login_check,name='admin_login_check'),
    path('viewPost/', views.blogHome, name='viewPost'),
    path('<slug:slug>/',views.detail_post,name='detail_post'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post')
]