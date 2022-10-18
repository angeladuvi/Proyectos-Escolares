# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:07:19 2021

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
print("La Frecuencia del Unigrama es:\n[" + textoBuscar+"]" , result)


#bigrama

textoBuscar1=input("ingresa el monograma a buscar del texto ")
resultado=re.findall(textoBuscar1, filetex)
resultado = len(resultado)
print("\nLa Frecuencia del  Bigrama es:\n["+ textoBuscar1+"]" , resultado )

# print("\nLa Frecuencia del  Bigrama y monograma es:\n[" + textoBuscar+"]" , result,"\n["+ textoBuscar1+"]" , resultado )


#TRIGRAMAS


textoBuscar11=input("ingresa el monograma a buscar del texto ")
resultados=re.findall(textoBuscar11, filetex)
resultados = len(resultados)
print("\nLa Frecuencia del  Bigrama es:\n["+ textoBuscar11+"]" , resultados )

# #print("\nLa Frecuencia del  Bigrama y monograma y tes:\n[" + textoBuscar+"]" , result,"\n["+ textoBuscar1+"]" , resultado )
# a=result
# b=resultado
# c=a/b
# print("\nLa Probabilidad Relativa es:")
# print("[", resultado,"/",result ,"] =",c)