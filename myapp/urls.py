from django.urls import path
from . import views

urlpatterns=[
    path('page1/',views.fun1,name='page1'),
    path('myhome/',views.home,name="home"),
    path('profile/',views.profile,name='profile'),
]