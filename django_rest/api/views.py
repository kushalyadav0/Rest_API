# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView # to handle class based views
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics


# Create your views here.
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all data from the student table 
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True) # initializing serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data) # initializing serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # finding operation
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    # editing operation 
    elif request.method == 'PUT': # editing existing data
        # trying to update data
        serializer = StudentSerializer(student, data = request.data) # accepting incoming data, and prepopulating existing data 
        # data will create new data, and using sutdent with this will update this specific student
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # deleting operation
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # bcz there will be no content after deleting the student
    
class Employees(APIView): # In CBVs we create member functions for CRUD operations
    # instance method 
    def get(self, request): # member function of the parent class
        # fetching employess very similar to FBVs
        employees = Employee.objects.all()
        serializer = EmpSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Create new employee
    def post(self, request):
        serializer = EmpSerializer(data = request.data) # accepting data coming from request
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
    
class EmployeesDetails(APIView):
    def get_object(self, pk): # custom method to retrieve objects
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        employee = self.get_object(pk) # calling method to retrieve the object
        serializer = EmpSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmpSerializer(employee, data = request.data) # because we are acceptung data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Mixins
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    pass 