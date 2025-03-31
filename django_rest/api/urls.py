from django.urls import path, include
from . import views

urlpatterns = [
    # student urls
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    # employee urls
    path('employees/', views.Employees.as_view()), # for class based view
    path('employees/<int:pk>/', views.EmployeesDetails.as_view()),
    
]
