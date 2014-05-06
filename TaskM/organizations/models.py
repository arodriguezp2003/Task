from django.db import models

# Create your models here.

class Organization(models.Model):
	name = models.CharField(max_length=255)
	userId = models.CharField(max_length=50)

class OrganizationUser(models.Model):
	organization = models.CharField(max_length=255)
	userId = models.CharField(max_length=50)