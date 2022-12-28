import numpy as np
import cv2 
# first we will create a square image
square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow("square img",square)
cv2.waitKey()
# ecllipse image
ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse img",ellipse)
cv2.waitKey(0)
# now perfprm bitwise operation by adding both pictures....And operation.
And=cv2.bitwise_and(square,ellipse)
cv2.imshow("And img",And)
cv2.waitKey(0)
# OR operation
Or=cv2.bitwise_or(square,ellipse)
cv2.imshow("or img",Or)
cv2.waitKey()
#Xor operation
Xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow("Xor img",Xor)
cv2.waitKey()
# Not operation.
Not=cv2.bitwise_not(square,ellipse)
cv2.imshow("Not img",Not)
cv2.waitKey()