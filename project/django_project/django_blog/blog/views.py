from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
	{
		'author': 'John',
		'title': 'Blog 1',
		'content': 'First Blog Content',
		'date_posted': 'August 29, 2023'
	},
	{
		'author': 'Tom',
		'title': 'Blog 2',
		'content': 'Second Blog Content',
		'date_posted': 'August 30, 2023'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})