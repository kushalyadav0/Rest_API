from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmpSerializer, TeacherSerializer, BookSerializer, companiesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView # to handle class based views
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from teachers.models import Teachers
from books.models import Books
from companies.models import Companies

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

"""
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    pass 
"""

class teachers(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): # we want to list down the teachers and we want to create new teachers
     queryset = Teachers.objects.all()
     serializer_class = TeacherSerializer
     
     def get(self, request):
         return self.list(request) # using list method of mixins to get objects
     
     def post(self,request):
         return self.create(request) # to create new teacher object
     
    
class teachersDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
     queryset = Teachers.objects.all()
     serializer_class = TeacherSerializer
     
     # primary key based operations 
     def get(self, request, pk): # to get a single objest using primary key
         return self.retrieve(request, pk)
     
     def put(self, request, pk):
         return self.update(request, pk)
     
     def delete(self, request, pk):
         return self.destroy(request, pk)

# Generics
class books(generics.ListAPIView, generics.CreateAPIView): # this class will accept two attributes which are queryset and serializer_class
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BooksDetails(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    
# Viewsets
"""
class companiesViewset(viewsets.ViewSet): # extending viewset class

    def list(self, request):
        queryset = Companies.objects.all()
        serializer = companiesSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = companiesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk= None):
        companies = get_object_or_404(Companies, pk= pk)
        serializer = companiesSerializer(companies)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk= None):
        company = Companies.objects.get(pk = pk)
        serializer = companiesSerializer(company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        company = get_object_or_404(Companies, pk= pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
# using modelViewSets
class companiesViewset(viewsets.ModelViewSet): # when using model viewset we just need to give queryset and serializer_class ans bangg!!! it's done 
    queryset = Companies.objects.all()
    serializer_class = companiesSerializer
    