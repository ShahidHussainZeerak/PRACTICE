import cv2
import numpy as np
device=cv2.VideoCapture(0)
while True:
    ret,frame=device.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# define range for blue color.
    lower_range=np.array([110,50,50])
    upper_range=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower_range,upper_range)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("show",mask)
    cv2.imshow("show1",frame)
    cv2.imshow("result",result)
    if cv2.waitKey(1)==13:
        break
    device.release()    
    device.destroyAllwindows()