from django.http import HttpResponse

def Home(request):
    return HttpResponse('<h1 style="text-align: center""> You have successfully created your simple django application.</h1>')