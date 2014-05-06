from .models import Note
from .serializer import NoteSerializer
from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
	model = Note
	serializer_class = NoteSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields =('userId',)
 