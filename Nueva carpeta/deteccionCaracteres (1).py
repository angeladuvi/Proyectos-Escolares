

import cv2
import numpy as np
from scipy import ndimage
from deteccionPlaca import detectarPlaca
from reconocimentoPlacas import clasificadorCaracteres, get_hog, redimensionar

img = cv2.imread('reconocimientoPlacas/placa1.jpg')

#cargando video
cap = cv2.VideoCapture(r'reconocimientoPlacas\video12.mp4')
    
while(cap.isOpened()):
    ret, frame =  cap.read()
    if ret == True:
        
        placa = detectarPlaca(frame)
        img = cv2.resize(frame,(400,400))
        cv2.imshow("video", img)
        if cv2.waitKey(1) == ord('s'):
            break
    else: break
    
# src = cv2.imread('foto2.jpg')


placaGris = cv2.cvtColor(placa, cv2.COLOR_BGR2GRAY)
umbral, _ = cv2.threshold(placaGris, 0, 255, cv2.THRESH_OTSU)

mascara = np.uint8(255*(placaGris<umbral))
output = cv2.connectedComponentsWithStats(mascara, 4, cv2.CV_32S)
cantidadObjetos = output[0]
etiquetas = output[1]
stats = output[2]

for i in range(1, cantidadObjetos):
    if stats[i,4] < stats[:,4].mean()/10:
        etiquetas = etiquetas - i*(etiquetas == i)
        
mascara = np.uint8(255*(etiquetas > 0))

#Dilatación de caracteres de la placa
kernel = np.ones((3,3), np.uint8)
mascara = np.uint8(255 * ndimage.binary_fill_holes(cv2.dilate(mascara, kernel)))

#Separar las letras de la placa con Bounding Rect
contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
caracteres = []
orden = []
placaCopia = placa.copy()
for cnt in contornos:
    x,y,w,h = cv2.boundingRect(cnt)
    caracteres.append(placa[y:y+h, x:x+w, :])
    orden.append(x)
    cv2.rectangle(placaCopia,(x,y), (x+w, y+h), (0,0,255), 1)
caracteresOrdenados = [x for _,x in sorted(zip(orden, caracteres))]


#Fase de clasificacion
palabrasKnn = ""
palabrasSVM = ""
palabrasPCT = ""
hog = get_hog()
knn, SVM, PCT = clasificadorCaracteres()
posiblesEtiquetas = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
posiblesEtiquetas = np.array(posiblesEtiquetas)
#caracteresPlaca = []

for i in caracteresOrdenados:
    m,n,_ = i.shape
    imagenEscalada = redimensionar(i,m,n)
    #caracteresPlaca.append(imagenEscalada)
    caracteristicasImagen = np.array(hog.compute(imagenEscalada))
    # palabrasKnn += posiblesEtiquetas[knn.predict(caracteristicasImagen.T)][0][0]
    # palabrasSVM += posiblesEtiquetas[SVM.predict(caracteristicasImagen.T)][0][0]
    palabrasPCT += posiblesEtiquetas[PCT.predict(caracteristicasImagen.T)][0][0]
    
print("El clasificador knn da como resultado: " + palabrasKnn)
print("El clasificador SVM da como resultado: " + palabrasSVM)
print("El clasificador PCT da como resultado: " + palabrasPCT)
    
cv2.putText(img, "La placa es: " + palabrasPCT, (10,300), cv2.FONT_HERSHEY_DUPLEX,0.8,(0,255,255),1 )

cv2.imshow("carro", img)
cv2.imshow("placa original", placa)
#cv2.imshow("imagen", caracteresPlaca[1])
cv2.waitKey(0)