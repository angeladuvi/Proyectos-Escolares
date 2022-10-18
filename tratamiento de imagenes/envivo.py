#import numpy as np

import cv2


def frameModificado(imagen):
    #Convertir la imagen a escala de Grisees
    #gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    canny=cv2.Canny(imagen,100,200)
    # cv2.imshow('Cnny', canny)
    
    ret,thresh1= cv2.threshold(canny,127,255,cv2.THRESH_BINARY_INV)
     
    #contours, hierarchy = cv2.findContours( cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    return thresh1
   

#Inicializamos la webcam
captura = cv2.VideoCapture(0)

while True:
    #Para captura los frame 
    ret, frame = captura.read()
    cv2.imshow("En vivo", frameModificado(frame))
    if cv2.waitKey(1) == 13:
        break
   

captura.release()
cv2.destroyAllWindows()




cv2.waitKey(0) 