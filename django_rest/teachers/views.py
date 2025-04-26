from django.shortcuts import render
from django.http import response, HttpResponse
from api.views import Teachers

# Create your views here.
def te(request):

    te = Teachers.objects.all()
    return(response)