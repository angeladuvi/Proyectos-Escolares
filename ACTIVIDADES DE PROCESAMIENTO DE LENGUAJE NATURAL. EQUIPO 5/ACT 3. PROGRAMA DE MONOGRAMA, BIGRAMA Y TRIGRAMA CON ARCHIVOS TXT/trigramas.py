# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:45:43 2021

@author: DELL
"""

import re
tex = open('reconocimiento_voz.txt','r')
filetex= tex.read()
tex.close()
print ("BIENVENIDO A MONOGRAMAS, BIGRAMAS, TRIGRAMAS ")
#monograma

textoBuscar=input("ingresa el  primer unigrama a buscar del texto ")
result=re.findall(textoBuscar, filetex)
result = len(result)
print("El Unigrama es:\n[" + textoBuscar+"]" , result)


#bigrama

textoBuscar1=input("ingresa el monograma a buscar del texto ")
resultado=re.findall(textoBuscar1, filetex)
resultado = len(resultado)
print("El Bigrama es:\n[" + textoBuscar+"]" , result,"\n["+ textoBuscar1+"]" , resultado )

#trigrama


textoBuscar2=input("ingresa el trigrama a buscar del texto ")
resultados=re.findall(textoBuscar2, filetex)
resultados = len(resultados)
print("El Trigrama es:\n[" + textoBuscar+"]" , result,"\n["+ textoBuscar1+"]" , resultado ,"\n[" + textoBuscar2+"]" , resultados)
    