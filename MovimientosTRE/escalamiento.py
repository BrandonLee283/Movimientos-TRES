import cv2
from PIL import Image
from numpy import asarray

image = cv2.imread('balon.jpg')

# Escalando una imagen
imageOut = cv2.resize(image,(400,300), interpolation=cv2.INTER_CUBIC)

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