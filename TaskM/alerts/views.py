from django.shortcuts import render
from .models import Alert
from rest_framework import viewsets
from .serializer import AlertSerializer
class AlertViewSet(viewsets.ModelViewSet):
	model = Alert
	serializer_class = AlertSerializer
