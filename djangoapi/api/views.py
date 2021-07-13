from django.shortcuts import render
from django.http import HttpResponse
from api.serializers import StudentSerializers
from rest_framework import viewsets
from api.models import Student

# Create your views here.


def Home(request):
    return HttpResponse("Thanks")


class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

