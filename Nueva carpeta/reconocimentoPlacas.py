import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
#from sklearn.metrics import confusion_matrix
#from sklearn.svm import SVC
from sklearn.manifold import TSNE
#from scipy import ndimage
from sklearn.linear_model import Perceptron

# from perceptronSiple import simple

def get_hog():
	winSize = (20,20)
	blockSize = (8,8)
	blockStride = (4,4)
	cellSize = (8,8)
	deriveAperture = 1
	gammaCorrection = 1
	nbins = 9
	winSigma = 2
	nlevels = 64
	signedGradient = True
	histogramType = 0
	L2HysThreshold = 0.2
	hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins, deriveAperture, winSigma, histogramType, L2HysThreshold, gammaCorrection, nlevels, signedGradient)
	return hog

def redimensionar(img, m, n):
	if m > n:
		imgNueva = np.uint8(255 * np.ones((m, round((m-n)/2),3)))
		imgEscalada = np.concatenate((np.concatenate((imgNueva, img), axis=1), imgNueva), axis=1)
	else:
		imgNueva = np.uint8(255 * np.ones((round((n-m)/2),n,3)))
		imgEscalada = np.concatenate((np.concatenate((imgNueva, img), axis=0), imgNueva), axis=0)

	img = cv2.resize(imgEscalada,(20,20))
	return img

def obtenerDatos():
	datos = []
	etiquetas = []
	posiblesEtiquetas = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']

	for i in range (1,26):
		for j in posiblesEtiquetas:
			img = cv2.imread("reconocimientoPlacas/" + j + '-' + str(i) + ".jpg")
			if img is not None:
				m,n,_ = img.shape
				if m != 20 or n != 20:
					img = redimensionar(img, m, n)
				etiquetas.append(np.where(np.array(posiblesEtiquetas)==j)[0][0])
				hog = get_hog()
				datos.append(np.array(hog.compute(img)))

	datos = np.array(datos)[:,:,0]
	etiquetas = np.array(etiquetas)
	return datos, etiquetas

def clasificadorCaracteres():
    datos, etiquetas = obtenerDatos()
    knn = KNeighborsClassifier(n_neighbors = 1)
    #knn.fit(datos, etiquetas)
    SVM = svm.SVC(kernel = "linear", probability = True, random_state = 0, gamma = "auto")
    #SVM.fit(datos, etiquetas)
    PCT = Perceptron(alpha=0.2)
    PCT.fit(datos,etiquetas)
    return knn, SVM, PCT
    
datos, etiquetas = obtenerDatos()

print("datos",len(datos))
print("etiquetas",len(etiquetas))

X_train, X_test, Y_train, Y_test = train_test_split(datos,etiquetas,test_size=0.2, random_state = np.random)
'''
#Evaluación de clasificador KNN
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, Y_train)
errorEntrenamientoKnn = (1-knn.score(X_train, Y_train))*100
print("Error de entrenamiento del Knn es: " + str(round(errorEntrenamientoKnn,2))+"%")

errorPruebaKnn = (1-knn.score(X_test, Y_test))*100
print("Error de prueba del Knn es: " + str(round(errorPruebaKnn,2))+"%")

#Cross Validation
errorKnn = 100 * (1 - cross_val_score(knn,datos,etiquetas,cv=10))
print("Knn cross val: " + str(round(errorKnn.mean(),2)) + "+-" + str(round(errorKnn.std(),2)))

#Crear la matriz de confusión
#X_test contiene los datos de prueba sin la clase
#Y_test contiene las clases de esos datos de prueba
prediccionKnn = knn.predict(X_test)
plt.imshow(confusion_matrix(Y_test, prediccionKnn), interpolation = "nearest")
plt.title("Matriz de confusión KNN")
plt.xlabel("Predicción")
plt.ylabel("Etiquetas verdaderas")

#Implementar el clasificador SVM
SVM = svm.SVC(kernel = 'linear', probability = True, random_state = 0, gamma = 'auto')
SVM.fit(X_train, Y_train)
errorSVM = 100 * (1 - cross_val_score(SVM,datos,etiquetas,cv=10))
print("SVM cross val: " + str(round(errorSVM.mean(),2)) + "+-" + str(round(errorSVM.std(),2)))
'''
#implementar la nuerona perceptron
PCT = Perceptron(alpha=1.02)
PCT.fit(X_train, Y_train)
errorPCT = 100 * (1 - cross_val_score(PCT,datos,etiquetas,cv=10))
print("Perceptron: " + str(round(errorPCT.mean(),2)) + "+-" + str(round(errorPCT.std(),2)))
 
#Visualizar datos de alta dimensionalidad
X = TSNE(n_components = 2).fit_transform(datos)
posiblesEtiquetas2 = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
x_min, x_max = np.min(X,0),np.max(X,0)
X = (X-x_min)/(x_max-x_min)

for i in range(0,len(X)):
    plt.text(X[i,0], X[i,1], str(posiblesEtiquetas2[etiquetas[i]]), color = plt.cm.Set1(3*float(etiquetas[i])/99))