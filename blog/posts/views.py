from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Posts

# Create your views here.
def home(request):
	#DO the processing on request object
	#aaj hum khatam kar denge
	posts = Posts.objects.all()
	context = { 'p': posts }
	return render(request , 'posts/home.html', context)

def test(request):
	return HttpResponse("hello")