import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag

# Create your views here.

def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'myapp/index.html', context={
		'post_list': post_list,
		})

def detail(request, pk):
	post=get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body,['extra','codehilite','toc',])
	return render(request, 'myapp/detail.html',{'post':post})
