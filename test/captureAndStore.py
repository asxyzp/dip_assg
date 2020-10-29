'''
    Program : CaptureAndStore.py
    Functionality : Captures image from the device's integrated web cam & stores the image
    Author : Aashish Loknath Panigrahi
'''
import cv2                                                              #Imports OpenCV module
PhotoObj = cv2.VideoCapture(0)                                          #VideoCapture class allows to capture video, image sequences or images
                                                                        #Index no. (0/1) decides the camera type (primary/secondary) chosen
PhotoTuple = PhotoObj.read()                                            
if(PhotoTuple[0]):
    fileName = input("Image file name (w/o file format)?\t")+".jpeg"
    Frame = PhotoTuple[1]
    cv2.imwrite(fileName,Frame)
    PhotoObj.release()
else:
    print("Image frame not captured appropriately.")
    PhotoObj.release()