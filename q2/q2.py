'''
    Program : q2.py (Question 2.py)
    Author : Aashish Loknath Panigrahi (@asxyzp)
    Problem statement : 
    For the provided image apply the following steps:
    a. Obtain histogram of the image
    b. Convert image into gray scale and obtain histogram of the image
    c. Convert image into binary and obtain histogram of the image
'''
import cv2
import sys
import numpy
from matplotlib import pyplot as plt 

#Plotting histogram of color image
def hist(filename):
    img = cv2.imread(filename,cv2.IMREAD_COLOR) 
    
    # calculate frequency of pixels in range 0-255 
    bhist = cv2.calcHist([img],[0],None,[256],[0,256])      #Frequency of blue histogram
    ghist = cv2.calcHist([img],[1],None,[256],[0,256])      #Frequency of green histogram
    rhist = cv2.calcHist([img],[2],None,[256],[0,256])      #Frequency of red histogram
    
    plt.plot(bhist,'b',label="Frequency of blue pixels")
    plt.title("Plot of frequency of blue pixels")
    plt.legend()
    plt.ylabel("Frequency")                     #Labels Y-axis
    plt.xlabel("Intensity (0-255)")             #Labels X-axis
    plt.grid()  
    plt.show()
    
    plt.plot(ghist,'g',label="Frequency of green pixels")
    plt.title("Plot of frequency of green pixels")
    plt.legend()
    plt.ylabel("Frequency")                     #Labels Y-axis
    plt.xlabel("Intensity (0-255)")             #Labels X-axis
    plt.grid()
    plt.show()
    
    plt.plot(rhist,'r',label="Frequency of red pixels") 
    plt.title("Plot of frequency of red pixels")
    plt.legend()
    plt.ylabel("Frequency")                     #Labels Y-axis
    plt.xlabel("Intensity (0-255)")             #Labels X-axis
    plt.grid()
    plt.show() 
 
#Plotting histogram of greyscale converted image
def greyhist(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('g'+filename,GrayFrame)
    
    # calculate frequency of pixels in range 0-255 
    hist = cv2.calcHist([GrayFrame],[0],None,[256],[0,256])      #Frequency of pixels
    
    plt.plot(hist,'k',label="Frequency of pixel intensity for greyscale image")
    plt.title("Plot of frequency of pixel intensity for greyscale image")
    plt.legend()
    plt.ylabel("Frequency")                     #Labels Y-axis
    plt.xlabel("Intensity (0-255)")             #Labels X-axis
    plt.grid()  
    plt.show()

#Plotting histogram of binary converted image
def binhist(filename):
    Frame = cv2.imread(filename,cv2.IMREAD_COLOR)
    GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    
    #Allowing the user to set the threshold
    threshold=-1
    while(threshold<0 or threshold>255):
        threshold = int(input("Enter threshold (t) : "))
        if(threshold<0 or threshold>255):
            print("Please enter appropriate threshold.")
    
    Ret,BinFrame = cv2.threshold(GrayFrame,threshold,255,cv2.THRESH_BINARY)   #Using simple binary threshold
    cv2.imwrite('b'+filename,BinFrame)             #Writing image
    
    # calculate frequency of pixels in range 0-255 
    hist = cv2.calcHist([BinFrame],[0],None,[256],[0,256])      #Frequency of pixels
    
    plt.plot(hist,'k',label="Frequency of pixel intensity for binary image")
    plt.title("Plot of frequency of pixel intensity for binary image w/ threshold "+str(threshold))
    plt.legend()
    plt.ylabel("Frequency")                     #Labels Y-axis
    plt.xlabel("Intensity (0-255)")             #Labels X-axis
    plt.grid()  
    plt.show()
    
    
#hist('img.png')
#greyhist('img.png')
#binhist('img.png')