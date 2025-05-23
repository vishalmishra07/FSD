from django.urls import path 
from app.views import * 
from .views import StudentListView, StudentDetailView 
urlpatterns = [ 
    path('mainpage/', home1, name='home1'), 
    path('studentlist/', studentlist, name='studentlist'), 
    path('courselist/', courselist, name='courselist'), 
    path('register/', register, name='register'), 
    path('enrolledlist/', enrolledStudents, name='enrolledStudents'), 
]