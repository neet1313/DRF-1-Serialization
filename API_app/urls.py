from django.urls import path
from API_app import views

urlpatterns = [
    path('', views.student_details),
    path('<slug:slug>', views.student)
]

