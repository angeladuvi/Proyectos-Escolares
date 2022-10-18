from django.shortcuts import render
from home.models import tessiu
import numpy as np 
# Create your views here.


def generarGrafo(request):

    Lista =tessiu.objects.get_queryset()
    calcular (Lista)
    diccionario ={ }
    calcular (Lista)
    return render(request,'home/home.html', diccionario)

def calcular(L):
    n=np.array[1,2,23],
     return n