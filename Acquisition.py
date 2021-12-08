from tkinter.constants import TRUE
from skimage import exposure as ex
from skimage.color import rgb2gray as con
from matplotlib import pyplot as plt
import imutils
import cv2
import numpy as np


def Acquisition_Lesion(strvar):
    print("[PROCESSING] Analyzing MRI-scan...")
    frame =  cv2.imread(strvar)
    gray = con(frame)
    frame = imutils.resize(frame, width=256,height=256)
    gray = imutils.resize(gray, width=256,height=256)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height = gray.shape[0]
    width = gray.shape[1]
    
    
    frame = frame.astype(np.uint8)
    img_out = frame.copy()
    for i in np.arange(3, height-3):
        for j in np.arange(3, width-3):
            neighbors = []
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = img_out.item(i+k, j+l)
                    neighbors.append(a)
            neighbors.sort()
            median = neighbors[24]
            b = median
            img_out.itemset((i,j), b)
    outImg = ex.equalize_hist(img_out[:,:])*255
    outImg[outImg>255] = 255
    outImg[outImg<0] = 0
    outImg = outImg.astype(np.uint8)
    equ = cv2.equalizeHist(img_out)   
    
    (T, thresh) = cv2.threshold(img_out, 50, 255,cv2.THRESH_BINARY)
    (T, thresh_f) = cv2.threshold(img_out, 120, 255,cv2.THRESH_BINARY)
    
    img = cv2.addWeighted(thresh, 0.3, thresh_f, 0.7, 0)
    
    detected_edges = cv2.Canny(equ, 120, 50, 5)

    #ALL 6 FIGURES
    original = plt.figure(1)
    plt.subplot(1,1,1),plt.imshow(gray,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    original.show()

    THRESHOLD = plt.figure(2)
    plt.subplot(1,1,1),plt.imshow(thresh,cmap = 'gray')
    plt.title('White and Gray'), plt.xticks([]), plt.yticks([])
    THRESHOLD.show()

    FUZZY = plt.figure(3)
    plt.subplot(1,1,1),plt.imshow(thresh_f,cmap = 'gray')
    plt.title('Lesion'), plt.xticks([]), plt.yticks([])
    FUZZY.show()

    Segmeted = plt.figure(4)
    plt.subplot(1,1,1),plt.imshow(img,cmap = 'gray')
    plt.title('Segmeted'), plt.xticks([]), plt.yticks([])
    Segmeted.show()

    Edges = plt.figure(5)
    plt.subplot(1,1,1),plt.imshow(detected_edges,cmap = 'gray')
    plt.title('Edges'), plt.xticks([]), plt.yticks([])
    Edges.show()

    colored = plt.figure(6)
    plt.subplot(1,1,1),plt.imshow(img,cmap = 'RdYlGn')
    plt.title('Colored'), plt.xticks([]), plt.yticks([])
    colored.show()
