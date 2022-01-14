from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student


class StudentApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer