import cv2
import numpy as np


def edge_dec(image, k=0):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    blurred_img = cv2.GaussianBlur(img,(25,25),2)
    if(k==0):
        canny_edge_img = cv2.Canny(blurred_img,40,50)
    elif(k==0):
        canny_edge_img = cv2.Canny(blurred_img,65,85)
    cv2.imwrite('./static/'+image, canny_edge_img)
