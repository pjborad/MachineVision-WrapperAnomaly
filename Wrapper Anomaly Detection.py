import cv2
import numpy as np

frame = cv2.imread('normal.jpg')
frame = cv2.resize(frame, (800,600))
cv2.imshow('original',frame)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#(thresh, binary) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
low = np.array([0,30,30])
high= np.array([18,255,255])
mask = cv2.inRange(hsv ,low, high)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
dilation = cv2.erode(mask, kernel, iterations=7)
erosion = cv2.dilate(dilation, kernel,iterations=7)
erosion = ~erosion
contours,d = cv2.findContours(erosion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
pts =  np.float32([[0,0],[700,0],[700,430],[0,430]])   
approx = np.float32([[x,y],[x+w,y],[x+w,y+h],[x,y+h]])
matrix = cv2.getPerspectiveTransform(approx,pts)
final = cv2.warpPerspective(frame,matrix,(700,430)) 
#cv2.imwrite('anomaly_register.jpg',final)
gray = cv2.cvtColor(final, cv2.COLOR_BGR2HSV)
low = np.array([80,70,70])
high= np.array([150,255,255])
mask = cv2.inRange(gray ,low, high)
mask = mask[0:430,0:175]
x=0
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if mask[i,j]==255:
            x=x+1
if x>9000:
    result = "PASS"
    cv2.putText(final,  result, (20,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
else:
    result = "FAIL"
    cv2.putText(final,  result, (20,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('final',final)
cv2.waitKey(0)