from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post


#def index(request):
#    return HttpResponse("You're at the gallery index.")

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'gallery/post_list.html', {'posts':posts})
