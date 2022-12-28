# how to split RGB space into separte form.
import cv2
from cv2 import waitKey
import numpy as np
img=cv2.imread("d.jpg")
cv2.imshow("out put",img)
cv2.waitKey(0)
# to extract rgb.
B,G,R=cv2.split(img)
#create in image...with the help of zero matrix.
zeros=np.zeros(img.shape[:2],dtype="uint8") 
#for rgb color space merge function is used
cv2.imshow("Blue",cv2.merge([B,zeros,zeros])) # first we will extract plan/color 1 using merge function.
waitKey(0)
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
waitKey(0)
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
waitKey(0)
cv2.destroyAllWindows()