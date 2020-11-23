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
size = 0
while(size<1 or size%2==0):
    size = int(input('Enter kernel size (e.g. 3,5):\t'))
    if(size<1):
        print('Please enter an appropriate kernel size (>=1).')
    if(size%2==0):
        print('Kernel size must be odd. Enter an odd no.')
kernel = np.ones((size,size),np.uint8)
iterationNo = 1

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

#For thickening
print("For thickening : ")
while (iterationNo<2):
    iterationNo = int(input('Enter the number of iterations : '))
    if (iterationNo<2):
        print('Please enter an appropriate iteration number.')
thickening = cv2.dilate(Frame,kernel,iterations = iterationNo)
cv2.imwrite('thickening.jpg',thickening)

#For Thinning
print("For thinning : ")
iterationNo = 1
while (iterationNo<2):
    iterationNo = int(input('Enter the number of iterations : '))
    if (iterationNo<2):
        print('Please enter an appropriate iteration number.')
thinning = cv2.erode(Frame,kernel,iterations = iterationNo)
cv2.imwrite('thinning.jpg',thinning)