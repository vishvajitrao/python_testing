from django.http import HttpResponse
from django.http import JsonResponse


def Home(request):
    return HttpResponse("<h1> Good Job! </h1>")


students = [
  {
    "address": "Noida",
    "student_id": 1,
    "student_name": "Vishvajit"
  },
  {
    "address": "Delhi",
    "student_id": 2,
    "student_name": "Shivam"
  },
  {
    "address": "Pune",
    "student_id": 3,
    "student_name": "Kumar"
  },
  {
    "address": "USA",
    "student_id": 4,
    "student_name": "John"
  }
]


def all_students(request):
    return JsonResponse(data=students, safe=False)