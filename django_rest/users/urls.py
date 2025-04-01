from django.contrib import admin
from django.urls import path
from . import views
from .views import SignUp
urlpatterns = [
    path('Login/', views.LogIn, name='LogIn'),
    path('Signup/', views.SignUp, name='SignUp')
    # path('signup/', SignUp.as_view(), name = 'Signup'),   
]