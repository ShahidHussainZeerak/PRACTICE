# how to perform arithmatic operation on image.
import cv2
import numpy as np
img=cv2.imread("ks.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)
# to perform operation on image we need to create a matrix 
M=np.ones(img.shape,dtype="uint8")*150
# adding operation.
added=cv2.add(img,M)
cv2.imshow("add img",added)
# subtraction matrix.
sbutracted=cv2.subtract(img,M)
cv2.imshow("subtract img",img)
# multiplication matrix.
mul=cv2.multiply(img,M)
cv2.imshow("multiply image",mul)
cv2.waitKey(0)
cv2.destroyAllWindows()