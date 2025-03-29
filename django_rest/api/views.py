from django.shortcuts import render
from django.http import JsonResponse, response



# Create your views here.
def students(request):
    students = {
        'id' : 1,
        'name' : 'abc',
        'branch' : 'ECE'
    }
    return JsonResponse(students)