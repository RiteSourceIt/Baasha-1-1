from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader,RequestContext



def index(request):
	template=loader.get_template("Baasha/index.html")
	rc=RequestContext(request)
	return HttpResponse(template.render(rc))

def language(request):
	template=loader.get_template("Baasha/language.html")
	rc=RequestContext(request)
	return HttpResponse(template.render(rc))