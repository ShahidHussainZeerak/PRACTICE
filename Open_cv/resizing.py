# how to resize image using open cv
import cv2
import numpy as np
img=cv2.imread("d.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)
# Linear interpoltation: Reduce size of image.
img_scaled=cv2.resize(img,None,fx=0.50,fy=0.50)
cv2.imshow("linear img",img_scaled)
cv2.waitKey(0)
# interpoltation_cubic: to double the size of the image.
img_scale=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("cubic",img_scale)
cv2.waitKey()
#interpoltation Area:increase or decrease area  of image
img_skewd=cv2.resize(img,(900,500),interpolation=cv2.INTER_AREA)
cv2.imshow("Skewed image",img_skewd)
cv2.waitKey(0)
cv2.destroyAllWindows()