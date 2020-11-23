'''
    For the provided image apply the following steps:
    a. Apply Laplacian mask (or any isotropic mask) to obtain Laplacian image
    b. Apply unsharp masking and high boost filtering to obtain sharp image
    c. Apply Sobel mask
    d. Apply Prewitt mask
    e. Apply canny edge detection for extracting edges. 
'''

import cv2
import os.path

ddepth = cv2.CV_16S
kernel_size = 3
scale = 1
delta = 0
ratio = 3
low_threshold = 0
max_lowThreshold = 100
    
#Applying laplacian mask
def LAPLACIAN(fileName):
    if(os.path.isfile(fileName)):
        Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)                   #Reading the image
        GaussianFrame = cv2.GaussianBlur(Frame, (3, 3), 0)              #Removing noise using Gaussian filter
        GrayFrame = cv2.cvtColor(GaussianFrame, cv2.COLOR_BGR2GRAY)     #Converting to greyscale image
        LapFrame = cv2.Laplacian(GrayFrame, ddepth, ksize=kernel_size)  #Applying laplacian frame
        AbsFrame = cv2.convertScaleAbs(LapFrame)                        #Converting back to uint8
        cv2.imwrite('laplacian_'+fileName,AbsFrame);
    else:
        print('File not found.')
    
#Applying sobel mask
def SOBEL(fileName):
    if(os.path.isfile(fileName)):
        Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)                   #Reading the image
        GaussianFrame = cv2.GaussianBlur(Frame, (3, 3), 0)              #Removing noise using Gaussian filter
        GrayFrame = cv2.cvtColor(GaussianFrame, cv2.COLOR_BGR2GRAY)     #Converting to greyscale image
        grad_x = cv2.Sobel(GrayFrame, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
        grad_y = cv2.Sobel(GrayFrame, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)                        #Converting back to uint8
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
        cv2.imwrite('sobel_'+fileName,grad);
    else:
        print('File not found.')

#Applying sobel mask
def CANNY(fileName):
    if(os.path.isfile(fileName)):
        Frame = cv2.imread(fileName,cv2.IMREAD_COLOR)                   #Reading the image
        GrayFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)             #Converting to greyscale image
        BlurFrame = cv2.blur(GrayFrame, (3,3))                          #Removing noise
        DetectedEdges = cv2.Canny(BlurFrame, low_threshold, low_threshold*ratio, kernel_size)
        mask = DetectedEdges != 0
        dst = Frame * (mask[:,:,None].astype(Frame.dtype))
        cv2.imwrite('canny_'+fileName,dst)
    else:
        print('File not found')

LAPLACIAN('q5.png')
SOBEL('q5.png')
CANNY('q5.png')