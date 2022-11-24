import cv2
import numpy as np


def kernel_sharpening(image, k=0):
    img = cv2.imread(image)
    if(k==0): 
        kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
        sharpended = cv2.filter2D(img,-1,kernel_sharpening)
    elif(k==1):
        smoothed = cv2.GaussianBlur(img, (25, 25), 2)
        sharpended = cv2.addWeighted(img, 1.5, smoothed, -0.5, 0)
    cv2.imwrite('./static/'+image, sharpended)
