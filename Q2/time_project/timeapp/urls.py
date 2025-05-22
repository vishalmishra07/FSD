from django.urls import path
from . import views

urlpatterns = [
    path('hours/<int:offset>/', views.hours, name='hours'),
]