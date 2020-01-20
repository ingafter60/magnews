from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from main.models import Main
from .models import News

# Create your views here.

def news_detail(request,word):

	pagetitle = Main.objects.get(pk=2)
	sosmed = Main.objects.get(pk=2)

	news = News.objects.filter(name=word)

	return render(request, 'front/news_detail.html', {
		'news':news,
		'pagetitle':pagetitle, 
		'sosmed':sosmed})

def news_list(request):

	return render(request, 'back/news_list.html', {})	