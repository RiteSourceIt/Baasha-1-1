from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'Baasha/index.html')
    #return HttpResponse('Baasha/index.html',render)