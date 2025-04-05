from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter # this will trake care of urls of viewsets

router = DefaultRouter()
router.register('companies', views.companiesViewset, basename= 'companies') # registering views that we will be using

urlpatterns = [
    # student urls
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),
    
    # employee urls
    path('employees/', views.Employees.as_view()), # for class based view
    path('employees/<int:pk>/', views.EmployeesDetails.as_view()),
    
    # teacher urls
    # for mixins
    path('teachers/', views.teachers.as_view()),
    path('teachers/<int:pk>/', views.teachersDetails.as_view()),
    
    # books urls
    # for generics
    path('books/', views.books.as_view()),
    path('books/<int:pk>/', views.BooksDetails.as_view()),
    
    # companies urls
    # viewsets
    path('', include(router.urls)), 
    
    # Blogs
   path('blogs/', views.BlogsView.as_view()),
   path('comments/',views.CommentsView.as_view()),
    # urls for primary key based operations
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailsView.as_view()),

]
