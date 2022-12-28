# filter2d filtration is used to  blur the pictures
import cv2
import numpy as np
img=cv2.imread("ks.jpg")
cv2.imshow("original img",img)
cv2.waitKey(0)
# creating a 3*3 kernel
kernel=np.ones((3*3),np.float32)/9
blur=cv2.filter2D(img,-1,kernel)
cv2.imshow("blur img",blur)
cv2.waitKey(0)
# creaeting 7*7 kernel

kernel1=np.ones((7*7),np.float32)/49
blur1=cv2.filter2D(img,-1,kernel1)
cv2.imshow("k 7*7 img",blur1)
cv2.waitKey(0)
