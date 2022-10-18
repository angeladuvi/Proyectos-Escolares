#from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):

    resultado = mifuncion(request)
    template_name='about/about.html'
    return render(request, template_name, )

def mifuncion(args):
     return ''





    