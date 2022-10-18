

min = 0
max = 8
bits = 10
p = (max-min)/ (pow(2, bits) -1)

a = (binario_a_decimal('0101010100') * p) + min
  # return a


#     x =math.radians(8)
#     math.cos(x)

# #ejemplos de uso
print(a)
print(binario_a_decimal('0101010100'))
print(binario_a_decimal('100011'))
print(binario_a_decimal('101011100011101'))



# y = 2( max*max)
# f=5(x)+y  
# print(f)




# for _ in range (int(pobl)):
#     binario = ""
#     bi = (int)(math.random())
#     print('poblacion ', random.choices(int(red)))
