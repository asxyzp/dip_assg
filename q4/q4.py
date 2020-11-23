'''
    For the provided image apply the following steps :
    a. Make image gray
    b. Apply OTSU model to convert image into binary image
'''

import cv2
import os.path

#1
#Converting color image to greyscale image
def COLOR2GRAY(fileName):
    if(os.path.isfile(fileName)):
        Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)       #Getting the color image frame
        GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame
        cv2.imwrite('gray_'+fileName,GrayFrame)             #Writing image
        print('COLOR TO GREYSCALE CONVERSION IS DONE!')
    else:
        print('File not found.')

#2
#Otsu's binarization
def OTSU(fileName):
    if(os.path.isfile(fileName)):
        Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)       #Getting the color image frame
        GrayFrame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)  #Converting the color image frame to grayscale image frame
        ret,th = cv2.threshold(GrayFrame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imwrite('otsu_'+fileName,th)
        print("OTSU'S BINARIZATION IS DONE!")
    else:
        print('File not found.')        
        
COLOR2GRAY('q4.png')
OTSU('q4.png')