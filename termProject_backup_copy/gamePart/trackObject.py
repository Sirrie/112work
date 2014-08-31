#tracking the boject
import cv
import cv2
import numpy as np
from matplotlib import pyplot as plt

class TrackObject(object):
    def init(self):
        self.pictureDotList=[];
        self.posX=0
        self.posY=0
        
    def main(self): 
        cap = cv2.VideoCapture(0)
      
        while(1):
        # take each frame
            _, frame = cap.read()
            print "successfullly read"
            
            img = frame;
            img = cv2.medianBlur(img,5)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
            #cimg=frame;
            
            circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,
                                        param1=50,param2=30,minRadius=0,maxRadius=0)
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            
            cv2.imshow('detected circles',cimg)
            
          #  hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
          #  # define range of blue color in HSV
          #  lower_blue = np.array([110,50,50])
          #  upper_blue = np.array([130,255,255])
          #  mask = cv2.inRange(hsv, lower_blue, upper_blue)
          #  #cv2.imshow('frame',frame)
          #  cv2.imshow('mask',mask)
          # # print "read"
          #  lastX,lastY,pX,pY=self.trackDot(mask);
          #  #print lastX,lastY,pX,pY
          #  cv2.circle(frame,(int(pX),int(pY)),20,(0,0,255))
          # # self.drawLine(frame)
          # # cv2.imshow('frame',frame)
          #  s_img=cv2.imread("/Users/Sirrie/Desktop/15112/termProject/gamePart/1.jpg")
          #  #print s_img,"sdfsdf"
          # # print len(s_img),len(s_img[0])
          #  x_offset=int(pX)
          #  y_offset=int(pY)
          #  # resize the image
          #  #print s_img.shape[1],"ttt",x_offset,y_offset
          #  
          #  (newx,newy)=s_img.shape[1]/20,s_img.shape[0]/20
          #  small = cv2.resize(s_img, (newx,newy)) 
          ##  print small
          # # print s_img.shape,"ttt",small.shape
          #  threadHold1=s_img.shape[0]
          #  threadHold2=s_img.shape[1]
          #  if y_offset<frame.shape[0]-threadHold1 and x_offset<frame.shape[1]-threadHold2:
          #      print "hereis my time"
          #      frame[y_offset:y_offset+small.shape[0], x_offset:x_offset+small.shape[1]] = small
          #  #self.drawLine(frame)
          #  cv2.imshow('frame',frame)
          # # list.add(cx,cy)
        
        
        
        
        
    def trackDot(self,image):
       # print "herere"
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
        
        
        
        #for x in xrange(row):
        #    for y in xrange(col):
        #        
        #        
        
        return (lastX,lastY,self.posX,self.posY)
        
    def drawLine(self,imgScribble):
        print "here3"
        ##if(self.posX>0 and self.posY>0):
        #    
        #    cv2.line(imgScribble,(int(pX),int(pY)),(int(lastX),int(lastY)),(0,250,0))
        #return imgScribble
        if len(self.pictureDotList)>2:
            for i in xrange(len(self.pictureDotList)-1):
                lastX,lastY=self.pictureDotList[i]
                posX,posY  =self.pictureDotList[i+1]
                cv2.line(imgScribble,(int(lastX),int(lastY)),(int(posX),int(posY)),(0,250,0))


track=TrackObject()
print "a"
track.init()
track.main()
        