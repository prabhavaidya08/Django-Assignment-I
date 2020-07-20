from django.shortcuts import render, redirect
 
from django.views import generic
from blog.models import Post
 
def index(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'index.html', { 'post_list': post_list })
  
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def about(request):
    return render(request, 'about.html', {})

def post(request):
    return render(request, 'post.html', {})    
  
def contact(request):
    return render(request, 'contact.html', {})




    