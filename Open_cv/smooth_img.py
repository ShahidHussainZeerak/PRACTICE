# how to smooth the image.
#bilateral filter is best but it is heavy it will take more space in the memory.
import cv2
import numpy as np
img=cv2.imread("d.jpg")
cv2.imshow("original img",img)
cv2.waitKey(0)
# use of blur()/ box size filter to smooth  the picture.
blur=cv2.blur(img,(3,3))
cv2.imshow("blur img",blur)
cv2.waitKey(0)
#median filter.
median=cv2.medianBlur(img,5)
cv2.imshow("MedianBlur Img",median)
cv2.waitKey(0)
#Bilateral Filter.
bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral img",bilateral)
cv2.waitKey(0)

