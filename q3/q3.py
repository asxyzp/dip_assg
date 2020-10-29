'''
    Program : q3.py (Question 3.py)
    Author : Aashish Loknath Panigrahi (@asxyzp)
    Problem statement : 
    Create or take a binary image (from Google) of the initial letter of your name and perform following morphological operations on it. 
    a.  Erosion
    b. Dilation
    c. Opening
    d. Closing
    e. Thickening
    f. Thinning
    g. Skeletonization
    h. Boundary of an image
'''
import cv2
import sys
import numpy as np

Frame = cv2.imread('A.jpg',cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5),np.uint8)
iterationNo = 4

#For Erosion
erosion = cv2.erode(Frame,kernel,iterations = iterationNo)
cv2.imwrite('erosion.jpg',erosion)

#For Dilution
dilation = cv2.dilate(Frame,kernel,iterations = iterationNo)
cv2.imwrite('dilation.jpg',dilation)

#For opening
opening = cv2.morphologyEx(Frame, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opening.jpg',opening)

#For closing
closing = cv2.morphologyEx(Frame, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('closing.jpg',closing)