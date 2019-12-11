from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
	return render(request, "index.html", {})
    #return HttpResponse("You're at the homepage index.")
