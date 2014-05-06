from django.shortcuts import render
from .models import Note
from rest_framework import viewsets

class NoteViewSet(viewsets.ModelViewSet):
	model = Note
