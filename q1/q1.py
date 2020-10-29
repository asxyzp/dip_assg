'''
    Program : q1.py (Question 1.py)
    Author : Aashish Loknath Panigrahi (@asxyzp)
    Problem statement : 
    Take your passport size photograph and apply the following transformations :
    (a) Convert image into greyscale image
    (b) Convert image into binary image
    (c) Apply mean filter
    (d) Apply median filter
    (e) Apply max filter
    (f) Apply Gaussian filter
    (g) Apply Logarithmic transformation
    (h) Apply power law transformation
    NOTE : For problems, c, d, e, g & h, use greyscale images
'''
import cv2
import os.path
import numpy as np
import sys

#1
#Converting color image to greyscale image
def COLOR2GRAY(fileName):
    Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)       #Getting the color image frame
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame
    cv2.imwrite('gray_'+fileName,GrayFrame)             #Writing image
  
#2  
#Converting color image to binary image using simple image thresholding
def COLOR2BINARY(fileName):
    Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)       #Getting the color image frame
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame
    
    #Allowing the user to set the threshold
    threshold=-1
    while(threshold<0 or threshold>255):
        threshold = int(input("Enter threshold (t) : "))
        if(threshold<0 or threshold>255):
            print("Please enter appropriate threshold.")
    
    Ret,ThresholdFrame = cv2.threshold(GrayFrame,threshold,255,cv2.THRESH_BINARY)   #Using simple binary threshold
    cv2.imwrite('binary_'+fileName,ThresholdFrame)             #Writing image

#3    
#Applying mean filter on the greyscale image
def GRAYMEAN(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)       #Getting the color image frame
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame
    
    #Setting kernel size to odd number >0
    kernelSize = 0
    while (kernelSize%2!=1 or kernelSize<=1):
        kernelSize = int(input("Enter odd kernel size (e.g. 3,5): "))
        if(kernelSize%2!=1 or kernelSize<=1):
            print("Enter appropriate kernel size.")
    
    BlurFrame = cv2.blur(GrayFrame,(kernelSize,kernelSize))
    cv2.imwrite('meanBlur_'+filename,BlurFrame)
    
#4
#Apply median filter on greyscale image
def GRAYMEDIAN(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)       #Getting the color image frame
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame
    
    #Setting kernel size to odd number >0
    kernelSize = 0
    while (kernelSize%2!=1 or kernelSize<=1):
        kernelSize = int(input("Enter odd kernel size (e.g. 3,5): "))
        if(kernelSize%2!=1 or kernelSize<=1):
            print("Enter appropriate kernel size.")
    
    MedianBlurFrame = cv2.medianBlur(GrayFrame,kernelSize)
    cv2.imwrite('medianBlur_'+filename,MedianBlurFrame)

#5
#Applying Gaussian filter on the image
def GAUSS(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)       #Getting the color image frame
    
    #Setting kernel size to odd number >0
    kernelSize = 0
    while (kernelSize%2!=1 or kernelSize<=1):
        kernelSize = int(input("Enter odd kernel size (e.g. 3,5): "))
        if(kernelSize%2!=1 or kernelSize<=1):
            print("Enter appropriate kernel size.")
    
    GaussianFrame = cv2.GaussianBlur(Frame,(kernelSize,kernelSize),0)
    cv2.imwrite('gaussianBlur_'+filename,GaussianFrame)
    
#6
#Logarithmic transformation on greyscale image
def LOG(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)       #Getting the color image frame
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame

    # Apply log transformation method 
    c = 255 / np.log(1 + np.max(GrayFrame)) 
    LogFrame = c * (np.log(GrayFrame + 1)) 
    
    # Specify the data type so that 
    # float value will be converted to int 
    LogFrame = np.array(LogFrame, dtype = np.uint8) 
    cv2.imwrite('log_'+filename,LogFrame)
    
#7
#Power law transformation on greyscale image
def POWER(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)       #Getting the color image frame
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame

    gamma = float(input("Gamma value? "))
    GammaFrame = np.array(255*(GrayFrame / 255) ** gamma, dtype = 'uint8')
    cv2.imwrite('gamma_'+filename,GammaFrame) 
    
COLOR2GRAY('0.jpg')
COLOR2BINARY('0.jpg')
GRAYMEAN('0.jpg')
GRAYMEDIAN('0.jpg')
GAUSS('0.jpg')
LOG('0.jpg')
POWER('0.jpg')