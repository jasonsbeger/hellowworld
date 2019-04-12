#-*- coding：utf-8 -*-
#author:zhiwei
import cv2
import numpy as np
'''
i=cv2.imread("F:/ceshi.png")
cv2.imshow("image",i)
cv2.namedWindow("Image")
cv2.imshow("Image",i)
cv2.waitKey(0)
'''

def main():
    cap = cv2.VideoCapture("E:/Video@2019_0326_132104.wmv")
    while(cap.isOpened()):
        ret,img = cap.read()
        skinMask = HSVBin(img)
        contours = getContours(skinMask)
        if np.size(contours)>10:
            print("can transform socket")
            #socket编译
        else:
            print("no aim")
        cv2.drawContours(img,contours,-1,(0,255,0),2)
        cv2.imshow('capture',img)
        k = cv2.waitKey(10)
        if k == 27:
            break

def getContours(img):
    kernel = np.ones((5,5),np.uint8)
    closed = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
    closed = cv2.morphologyEx(closed,cv2.MORPH_CLOSE,kernel)
    _,contours,h = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    vaildContours = []
    for cont in contours:
        if cv2.contourArea(cont)>9000:
            #x,y,w,h = cv2.boundingRect(cont)
            #if h/w >0.75:
            #filter face failed
            vaildContours.append(cv2.convexHull(cont))
            print(vaildContours)
            #rect = cv2.minAreaRect(cont)
            #box = cv2.cv.BoxPoint(rect)
            #vaildContours.append(np.int0(box))
    return  vaildContours

def HSVBin(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    lower_skin = np.array([100,50,0])
    upper_skin = np.array([125,255,255])
    mask = cv2.inRange(hsv,lower_skin,upper_skin)
    #res = cv2.bitwise_and(img,img,mask=mask)
    return mask

if __name__ =='__main__':
    main()
