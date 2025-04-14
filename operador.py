import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

dir = './Vis-o-computacional/images/'

for arquivo in os.listdir(dir):
    if arquivo.endswith('.jpeg'):
        img = cv2.imread(dir + arquivo)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

       
        img_blur = cv2.blur(img,(5,5))
        img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
        a = img_gray.max()
        _, thresh = cv2.threshold(img_gray, a/2+100, a,cv2.THRESH_BINARY_INV)
        kernel = np.ones((12,12), np.uint8)
        img_dilate = cv2.dilate(thresh,kernel,iterations = 1)
        img_erode = cv2.erode(thresh,kernel,iterations = 1)
        img_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        img_close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        img_grad = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
        img_tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernel)
        img_blackhat = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernel)

        
        imagens = [img, img_blur,  img_gray,thresh,img_erode,img_dilate, img_open, img_close, img_grad,
                img_tophat, img_blackhat]

        formatoX = math.ceil(len(imagens)**.5)
        if (formatoX**2-len(imagens))>formatoX:
            formatoY = formatoX-1
        else:
            formatoY = formatoX

        for i in range(len(imagens)):
            plt.subplot(formatoY, formatoX, i + 1)
            plt.imshow(imagens[i],'gray')
            plt.xticks([]),plt.yticks([])
        plt.show()