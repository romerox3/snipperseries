# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from utils import extractor
from forms import search

# Create your views here.

def index(request):
	lista_imagenes = []
	if request.method == "GET":
		form = search()
	if request.method == "POST":
		data = request.POST
		palabra = data.get('your_name')
		form = search(data)

		lista_imagenes = extractor(palabra)
	
	context = {"lista_imagenes": lista_imagenes, "form": form}
	return render(request, 'Searcher/index.html', context)