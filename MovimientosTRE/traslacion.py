import cv2
import numpy as np

from PIL import Image
from numpy import asarray


image = cv2.imread('balon.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Traslación
M = np.float32([[1,0,100],[0,1,150]])
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen de entrada',image)

numpydata = asarray(image)
print(numpydata)

cv2.imshow('Imagen de salida',imageOut)

numpydata = asarray(imageOut)
print(numpydata)

imgMultiply = cv2.multiply(imageOut,1.5)

cv2.imshow('imgMultiply', imgMultiply)

cv2.waitKey(0)
cv2.destroyAllWindows()