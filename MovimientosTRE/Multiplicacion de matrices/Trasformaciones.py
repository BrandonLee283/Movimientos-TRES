import numpy as np
import cv2
def  main():
    img = cv2.resize(cv2.imread(r'balon.jpg'),(400,500))
    imgMultiply = cv2.multiply(img,img)

    cv2.imshow('img', img)
    cv2.imshow('imgMultiply', imgMultiply)
    cv2.waitKey(0)
main()