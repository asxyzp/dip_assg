'''
    Program : readAndGreyscale.py
    Functionality : Reading image and converting the image into a greyscale image
    Author : Aashish Loknath Panigrahi (@asxyzp)
'''

import cv2
import os.path
import sys

fileName = input("Image file name (w/ file format)?\t")
if(os.path.isfile(fileName)):
    Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)
    rowlen = len(Frame)         #Stores length of the row
    collen = len(Frame[0])      #Stores length of the column
    for i in range(rowlen):
        for j in range(collen):
            #Using luma method for converting color image to grayscale
            grey = Frame[i][j][0]*0.3+Frame[i][j][1]*0.59+Frame[i][j][2]*0.11
            Frame[i][j][0]=grey
            Frame[i][j][1]=grey
            Frame[i][j][2]=grey
    cv2.imwrite("greyscale_"+fileName,Frame)