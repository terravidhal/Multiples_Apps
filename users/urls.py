from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('',views.root, name='root'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('users/new', views.register, name='register'),
    path('users', views.show, name='show'),
]