import cv2
import numpy as np


def sincos(image, k=0):
    l = 20      # ����(wave length)
    amp = 15    # ����(amplitude)
    img = cv2.imread(image)
    rows, cols = img.shape[:2]
    mapy, mapx = np.indices((rows, cols),dtype=np.float32)
    sinx = mapx + amp * np.sin(mapy/l)  
    cosy = mapy + amp * np.cos(mapx/l)
    if(k==0):
        img_lens=cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE) 
    elif(k==1):
        img_lens=cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE)
    else:
        img_lens=cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE) 
    cv2.imwrite('./static/'+image,img_lens)

        
        

