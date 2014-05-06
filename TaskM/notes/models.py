from django.db import models

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=255)
	create  = models.DateTimeField(auto_now_add=True)
	text  =	models.TextField(blank=True)
	userId = models.CharField(max_length=50)