import math
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


dir = './Vis-o-computacional/images/'

for arquivo in os.listdir(dir):
    if arquivo.endswith('.jpeg'):
        img = cv2.imread(dir + arquivo)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        a = img_gray.max()
        _, thresh = cv2.threshold(img_gray, a/2*1.7, a,cv2.THRESH_BINARY_INV)


        tamanhoKernel = 5
        kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)
        thresh_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        
        img_blur = cv2.blur(img_gray, ksize=(tamanhoKernel,tamanhoKernel))

        
        edges_gray = cv2.Canny(image=img_gray, threshold1=a/2, threshold2=a/2)
        
        edges_blur = cv2.Canny(image=img_blur, threshold1=a/2, threshold2=a/2)



        
        contours, hierarchy = cv2.findContours(
                                        image = thresh,
                                        mode = cv2.RETR_TREE,
                                        method = cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)
        img_copy = img.copy()
        final = cv2.drawContours(img_copy, contours, contourIdx = -1,
                                color = (255, 0, 0), thickness = 2)


       
        imagens = [img,img_blur,img_gray,edges_gray,edges_blur,thresh,thresh_open,final]
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