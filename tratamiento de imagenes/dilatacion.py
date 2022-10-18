
import cv2
import numpy as np

imagen = cv2.imread(r'C:\Users\DELL\Pictures\cuevas\huella.jpeg',0)

cv2.imshow('Original', imagen)
kernel = np.ones((5,5),np.uint8)

imagen_dilatada = cv2.erode(imagen, kernel, iterations = 2 )
imagen_dila = cv2.dilate (imagen_dilatada , kernel, iterations = 1)
cv2.imshow('Dilatada', imagen_dila)




cv2.waitKey(0)
cv2.destroyAllWindows()
