from django.shortcuts import render
from django.http import HttpResponse
from .models import tessiu
# Create your views here.

def micasa(request):
    Lista =tessiu.objects.get_queryset()

    ProcesaLista(Lista)
    template_name='home/home.html'
    diccionario ={'l':Lista,}
    return render(request, template_name, diccionario)
    
def ProcesaLista(L):
    for i in L:
        if i.color > 20:
            print(i.pk, i.color, 'tejido enfermo')
        else: 
            print(i.pk , i.color, 'tejido no enfermo')    

        # return HttpResponse('<h1>Hola mundo</h1>')
