# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:55:29 2021

@author: DELL
"""

import cv2
import numpy as np

image = cv2.imread('huella.jpeg')
cv2.imshow('Original', image)

#Crear el kernel para aplicar la convolución
kernel = np.array([[1,1,1],
                  [1,1,1],
                  [1,1,1]])
  
kernel_3x3 = np.ones((3,3), np.float32) / 9

resultado = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('Imagen con filtro', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()