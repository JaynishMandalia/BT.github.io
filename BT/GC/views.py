from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def Login(request):
    return render(request, 'index.html')
