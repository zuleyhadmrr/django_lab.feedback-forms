from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_create, name='feedback_create'),
    path('success/', views.feedback_success, name='feedback_success'),
]