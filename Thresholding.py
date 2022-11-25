import cv2
import numpy as np


def Local_Thresholding(img,k=0, mask_size=3, C=0.9):
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    if(k==1):
        mask = np.zeros((mask_size,mask_size))
        halfx = mask_size//2
        halfy = mask_size//2
        padded = np.zeros((image.shape[0]+halfx*2, image.shape[1]+halfy*2), dtype = np.uint8)
        padded[halfx:padded.shape[0]-halfx,halfy:padded.shape[1]-halfy] = image
        result = np.zeros((image.shape[0],image.shape[1]), dtype=np.float64)
        Threshold = np.zeros((image.shape[0],image.shape[1]), dtype=np.float64)
        for y in np.arange(image.shape[1]):
            for x in np.arange(image.shape[0]):
                threshold = 0
                threshold = C*padded[x:x+mask.shape[0], y: y+mask.shape[1]].mean()
                Threshold[x,y] = threshold
                if padded[x,y] > threshold:
                    result[x,y] = 255
                else:
                    result[x,y] = 0  
        result = result.astype('uint8')
    elif(k==0):
        result= cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)
    image_name = img[8:]
    cv2.imwrite('./static/'+image_name, result)
