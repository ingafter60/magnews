from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

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

	# Retrieve data from db
	news = News.objects.all()

	return render(request, 'back/news_list.html', {'news':news})	

def news_add(request):

	if request.method == 'POST':

		newstitle = request.POST.get('newstitle')
		newscat = request.POST.get('newscat')
		newstxtshort = request.POST.get('newstxtshort')
		newstxt = request.POST.get('newstxt')


		if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "" :
			
			error = "All Fields Required ...."
			return render(request, 'back/error.html', {'error':error})	

		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		url = fs.url(filename)	

		b = News(
			name		  = newstitle,
			short_text = newstxtshort,
			body_text  = newstxt,
			date 		  = "2020",
			picname 	  = filename,
			picurl 	  = url,
			writer 	  = "-",
			catname 	  = newscat,
			catid 	  = 0,
			show 		  = 0
		)	

		b.save()
		return redirect('news_list')

	return render(request, 'back/news_add.html', {})	

