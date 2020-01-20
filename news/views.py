from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from main.models import Main
from .models import News

# Create your views here.

def news_detail(request,pk):

	pagetitle = Main.objects.get(pk=2)
	sosmed = Main.objects.get(pk=2)

	news = News.objects.filter(pk=pk)

	return render(request, 'front/news_detail.html', {
		'news':news,
		'pagetitle':pagetitle, 
		'sosmed':sosmed})