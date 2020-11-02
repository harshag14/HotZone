from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginView(request):
    return render(request, 'login.html')
