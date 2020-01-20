from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
	list_of_dates = ["11/12", "01/03", "03/06"]
	return render(request, "index.html", {"dates": list_of_dates})
    #return HttpResponse("You're at the homepage index.")
