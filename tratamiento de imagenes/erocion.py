
import cv2
import numpy as np

imagen = cv2.imread(r'C:\Users\DELL\Pictures\cuevas\circulos.jpeg',0)

cv2.imshow('Original', imagen)
kernel = np.ones((5,5),np.uint8)

imagen_erosionada = cv2.erode(imagen, kernel, iterations = 3)

resultado = cv2.subtract(imagen,imagen_erosionada)

cv2.imshow('resultado',resultado)



cv2.waitKey(0)
cv2.destroyAllWindows()
