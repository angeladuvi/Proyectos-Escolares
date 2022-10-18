import cv2
import numpy as np
import imutils


img = cv2.imread(r'C:\Users\DELL\Pictures\cuevas\uaemex.jpg', 0)
img= imutils.resize(img, width=400)


_,binari=cv2.threshold(img,10,0,cv2.THRESH_BINARY)
_,binariInv=cv2.threshold(img,210,255,cv2.THRESH_BINARY_INV)
_,Trunc=cv2.threshold(img,20,255,cv2.THRESH_TRUNC)
_,Toz=cv2.threshold(img,120,255,cv2.THRESH_TOZERO)

cv2.imshow('original', img)
cv2.imshow('Tipos: Binari  -  Binary  Inv',np.hstack([binari,binariInv]))
cv2.imshow('Tipos Trunc ',Trunc)
cv2.imshow('Tipos Tozero',Toz)
cv2.waitKey(0)
cv2.destroyAllWindows()




