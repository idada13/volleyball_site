from django.db import models

# Create your models here.
#Each time adding/changing models need to run this:
#	python manage.py makemigrations 
#	python manage.py migrate


class Latest(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=False, null=True) # blank = False/True makes the field required or not
	blog_url 	= models.URLField(max_length=200)
	image	 	= models.TextField(blank=False)
	featured	= models.BooleanField()