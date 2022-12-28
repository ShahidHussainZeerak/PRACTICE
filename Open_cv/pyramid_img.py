# how to resize the image directly.
import cv2
import numpy as np
img=cv2.imread("d.jpg")
smaller=cv2.pyrDown(img)
large=cv2.pyrUp(img)
cv2.imshow("original image",img)
cv2.imshow("small image",smaller)
cv2.imshow("large image",large)
cv2.waitKey(0)
cv2.destroyAllWindows()