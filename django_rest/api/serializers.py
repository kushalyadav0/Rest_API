from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from teachers.models import Teachers
from books.models import Books
from companies.models import Companies

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'
        
class EmpSerializer(serializers.ModelSerializer):
    class Meta():
        model = Employee
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta():
        model = Teachers
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Books
        fields = '__all__'
        
class companiesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Companies
        fields = '__all__'