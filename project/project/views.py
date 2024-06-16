from django.shortcuts import render
from django.conf import settings

def my_view(request):
    return render(request, 'about.html')