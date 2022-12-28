# how to detect the edge of a picture.
import cv2
from cv2 import bitwise_or
import numpy as np
img=cv2.imread("D:/MY PICTURE/sa.jpg")
cv2.imshow("original img",img)
cv2.waitKey(0)
#Extract the slope edges.
sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow("sobel_x",sobel_x)
cv2.waitKey(0)
cv2.imshow("sobel_y",sobel_y)
cv2.waitKey(0)
# now add slobe x and slobe y through or bitwise operation
Or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("or img",Or)
cv2.waitKey(0)
# Laplacian filter:
laplac=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("laplacian img",laplac)
cv2.waitKey(0)
# cany edge detection.
cany=cv2.Canny(img,20,170)
cv2.imshow("canny img",cany)
cv2.waitKey(0)
cv2.destroyAllWindows()