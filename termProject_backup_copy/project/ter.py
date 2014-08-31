#tracking the boject
import cv
import cv2
import cv2.cv as cv
import numpy as np
from matplotlib import pyplot as plt

class TrackObject(object):
    def init(self):
        self.pictureDotList=[];
        self.posX=0
        self.posY=0
        self.cap = cv2.VideoCapture(0)
       # set the frame to be with the same size of the present 
        self.cap.set(3,900)
        self.cap.set(4,500)
    def main(self): 
        
        while(1):
        # take each frame
            _, frame = cap.read()
            print "successfullly read"
            hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            # define range of blue color in HSV
            lower_blue = np.array([110,50,50])
            upper_blue = np.array([130,255,255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            cv2.imshow('mask',mask)
            lastX,lastY,pX,pY=self.trackDot(mask);
          # draw the circle for tracking the dot
            cv2.circle(frame,(int(pX),int(pY)),20,(0,0,255))
            #cv2.imshow('frame',frame)
        
        
    def getImage(self,cap):
        #cap = cv2.VideoCapture(0)
        _, frame = cap.read()
        print "successfullly read"
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        lastX,lastY,pX,pY=self.trackDot(mask);
        #print lastX,lastY,pX,pY
        cv2.circle(frame,(int(pX),int(pY)),20,(0,0,255))

        # img=frame
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,
        #                     param1=50,param2=30,minRadius=0,maxRadius=0)

        # circles = np.uint16(np.around(circles))
        # for i in circles[0,:]:
        #     # draw the outer circle
        #     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        #     # draw the center of the circle
        #     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

        # cv2.imshow('detected circles',cimg)
        cv2.imshow('frame',frame)
        return lastX, lastY

    def trackDot(self,image):
        cvMoments = cv2.moments(image)
        #print cvMoments
        
        moment10=cvMoments['m10']
        moment01=cvMoments['m01']
        area    =cvMoments['m00']
        
        lastX=self.posX
        lastY=self.posY
        if (area!=0):
            self.posX=moment10/area;
            self.posY=moment01/area;
        self.pictureDotList.append((lastX,lastY))
        
        # loop through the mask frame to find the dot inside it
        (row,col)=(len(image),len(image[0]))
        
        return (lastX,lastY,self.posX,self.posY)
        

#track=TrackObject()
#track.init()
#track.main()
        