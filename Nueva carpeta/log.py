import math
import random

#binarioa decimal
print("********BINARIO A DECIMAL *******\n")
print("por favor ingresa el numero binario \n")
binario  = str(input())
binario("1 1 0 1 0 1 1 1 1 1
"1 1 1 1 1 1 1 0 0 1"
"0 0 1 1 1 0 0 1 0 0"
1 0 1 0 1 1 0 0 0 0"
0 0 1 1 1 0 1 0 0 1"
1 1 1 1 0 1 0 0 0 0"
1 1 0 0 1 0 0 1 1 0"
1 1 1 0 1 0 1 0 1 1
0 1 0 0 0 1 1 1 1 1
1 0 1 1 0 0 0 1 1 1
0 1 0 1 1 0 1 1 1 0
1 0 0 0 1 1 1 1 1 1
0 1 0 0 0 1 1 1 1 0
0 1 1 0 1 1 0 1 1 0
1 0 1 1 1 0 0 1 1 0
0 1 0 1 1 1 1 0 1 0
1 1 0 1 1 0 1 0 0 1
0 1 1 0 0 0 0 0 1 1
0 0 0 1 0 0 1 0 0 0
0 1 1 1 0 0 1 1 1 1
0 0 1 1 0 0 0 1 0 1
1 0 0 0 1 0 1 0 0 1
1 0 0 1 1 0 0 1 1 0
1 1 1 1 0 0 0 1 1 0
0 1 0 1 0 0 1 0 1 0")
res = 0
for i in range(len(binario)):
    res += int(binario[i]) * 2 **(len(binario) - i - 1)
print("el valor decimal es:\n" )
print(res)

#valor real 
print("********VALOR REAL********\n")
print("por favor ingresa el numero min del rango\n")
min = input()
print("por favor ingresa el numero max del rango\n")
max = input()
bits = 10

real= int(min) + int(res) * ((int(max)-int(min))/( pow(2,int(bits)) -1))
print("El valor real es:\n" )    
print(real)                  
                       
# #valor adaptado
print("********VALOR ADAPTADO********\n ")
gra=math.radians(res)

f=(5*math.cos(float(gra)) )+ 2*(pow(float(gra),2))
print("el valor adaptado es:\n")
print(f)



#poblacion 
print("********POBLACION******** \n")

min = 0
max = 20
print("por favor ingresa la precision:\n")
prec = input()
#haciendo la funcion de log base 2 
a= 1 + (max-min)/ float(prec)
numerator = math.log(a)
denominator = math.log(2)
f = numerator / denominator
print(f)
red = math.ceil(f)
print("valor dedondeado\n")
print(red)
print("1  0 1 1 1 0 1 0 0 1 0 95.95 ")
#generando la poblacion 
print("por favor ingresar el numero de la poblacion\n ")
pobl =input()
valores= 0,1
binario = ""
for _ in range (int(pobl)):
    
    bi =[str(pobl)for pobl in random.choices((0,1),k=10)]
   
    print(" ".join(bi))
# ordenando de mayor a menor 01

#     binario  = bi
#     res = 0
# for i in range(len(binario)):
#     res += int(binario[i]) * 2 **(len(binario) - i - 1)
# print("el valor decimal es:\n" )
# print(res)








def selec4ruleta(ristras, decimales, reales, adaptados):
    porc = 50
    cant = round((len(ristras)/100)*porc)
    ruleta = []
    adapOrden = sorted(adaptados, reverse=True)
    # print(adapOrden)
    orden = []
    for i in range(len(adapOrden)):
        for j in range(len(adaptados)):
            if (adapOrden[i]==adaptados[j]):
              orden.append(j)
    print(orden)
    
    for i in range(cant):
        ruleta.append(ristras[random.randint(0,len(ristras))])
    print(ruleta)