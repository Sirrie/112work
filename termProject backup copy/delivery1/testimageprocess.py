#test
import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
      
#while(1):
# take each frame
_, frame = cap.read()
print "successfullly read"
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
print "read"
print len(frame),len(frame[0])
print frame,mask
k = cv2.waitKey(5) & 0xFF
size=len(frame)/20
for i in xrange(len(frame),size):
    for j in xrange(len(frame[0])):
        print frame[i][j],
    print i,j
    
img=mask
img = cv2.medianBlur(img,5)
print img
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print cimg
circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=5,maxRadius=20)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle

cv2.imshow('detected circles',cimg)