from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html')