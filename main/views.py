from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .models import Main

# Create your views here.

def home(request):

	# pagetitle = 'Home | MAGNews'
	pagetitle = Main.objects.get(pk=2)
	sosmed = Main.objects.get(pk=2)

	return render(request, 'front/home.html', {'pagetitle':pagetitle, 'sosmed':sosmed})

def about(request):

	# pagetitle = 'About | MAGNews'
	pagetitle = Main.objects.get(pk=2)
	sosmed = Main.objects.get(pk=2)

	return render(request, 'front/about.html', {'pagetitle':pagetitle, 'sosmed':sosmed})