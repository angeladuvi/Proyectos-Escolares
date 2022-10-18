# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:34:45 2021

@author: DELL
"""
#Carmen Ramirez Leal

import re

tex="El cielo es azul y los oceanos, y amarillo son los girÁsoles "
print(tex)
# tex = open('voz.txt','r',encoding="utf8")
# filetex= tex.read()
# print(filetex,2)
# tex.close()
print ("FRECUENCIA DE LAS LETRAS MAYUSCULAS ")

mayusculas='[A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,W,X,Y,Z,Á,É,Ó,Ú,Í,]'

result=re.findall(mayusculas, tex)
result = len(result)
print("La Frecuencia del Unigrama es:\n[" + mayusculas+"] =" , result)
