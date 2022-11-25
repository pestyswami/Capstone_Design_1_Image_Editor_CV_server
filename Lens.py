import cv2
import numpy as np


def lens(image, k=0):
    img = cv2.imread(image)
    if(k==0):
        exp = 2
        scale = 1
    elif(k==1):
        exp =0.5
        scale = 1
    rows, cols = img.shape[:2]
    mapy, mapx = np.indices((rows, cols),dtype=np.float32)

    mapx = 2*mapx/(cols-1)-1
    mapy = 2*mapy/(rows-1)-1

    r, theta = cv2.cartToPolar(mapx, mapy)
    r[r< scale] = r[r<scale] **exp  
    mapx, mapy = cv2.polarToCart(r, theta)

    mapx = ((mapx + 1)*cols-1)/2
    mapy = ((mapy + 1)*rows-1)/2
    nimg = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
    image_name = image[8:]
    cv2.imwrite('./static/'+image_name, nimg)
