from django.db import models

# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length=100) 
	author = models.CharField(max_length=100)
	created_on = models.DateTimeField(auto_now_add=True)
	content = models.TextField(max_length=10000)


		