
import re
poema="Podrá nublarse el sol eternamente; \nPodrá secarse en un instante el mar; \nComo un débil cristal.\n¡todo sucederá! Podrá la muerte\nCubrirme con su fúnebre crespón; \nPero jamás en mí podrá apagarse \nLa llama de tu amor."
print(poema)
vocales ='[A,E,I,O,U,a,e,i,o,u,Á,É,Í,Ó,Ú,á,é,í,ó,ú]'
resultado= re.sub(vocales,"",poema)
print("\n TEXTO SIN VOCALES \n")
print(resultado)

