
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

def Auth(request,user,passw):
	
	user = authenticate(username=user, password=passw)
	if user is not None: 
		if user.is_active:
			#us = serializers.serialize('json', user)
			resp = HttpResponse("SI") # respuesta vacia
			resp["Access-Control-Allow-Origin"] = "*" # permitimos todos los dominios
			resp["Access-Control-Allow-Methods"] = "GET, OPTIONS" # metodos permitidos
			resp["Access-Control-Allow-Headers"] = "X-Requested-With" # importa
			return resp
		else:
			resp = HttpResponse("NOACTIVE") # respuesta vacia
			resp["Access-Control-Allow-Origin"] = "*" # permitimos todos los dominios
			resp["Access-Control-Allow-Methods"] = "GET, OPTIONS" # metodos permitidos
			resp["Access-Control-Allow-Headers"] = "X-Requested-With" # importa
			return resp
	else:
		resp = HttpResponse("NO") # respuesta vacia
		resp["Access-Control-Allow-Origin"] = "*" # permitimos todos los dominios
		resp["Access-Control-Allow-Methods"] = "GET, OPTIONS" # metodos permitidos
		resp["Access-Control-Allow-Headers"] = "X-Requested-With" # importa
		return resp
	

