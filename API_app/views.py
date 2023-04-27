from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse

# Create your views here.

# Single student data
def student(request, slug):
    student_data = Student.objects.get(id=slug)
    serializer = StudentSerializer(student_data)
    return JsonResponse(serializer.data)


# Queryset - All student data
def student_details(request):
    student_data = Student.objects.all()
    serializer = StudentSerializer(student_data, many=True)
    # For queriesets -> many=True in serializer
    # For dictionary safe=True and for non-dict safe=False in JSONResponse()
    return JsonResponse(serializer.data, safe=False)
