from .models import Organization, OrganizationUser
from .serializer import OrganizationSerializer, OrganizationUserSerializer
from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

class OrganizationViewSet(viewsets.ModelViewSet):
	model = Organization
	serializer_class = OrganizationSerializer
	filter_backends = (filters.DjangoFilterBackend,)

class OrganizationUserViewSet(viewsets.ModelViewSet):
	model = OrganizationUser
	serializer_class = OrganizationUserSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	#filter_fields =('userId',)
 