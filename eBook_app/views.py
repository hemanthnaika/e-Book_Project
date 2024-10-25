from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Write response in this section
def home(request):
    return HttpResponse("Hello World")

def contact(request):
    return HttpResponse("Contact page")