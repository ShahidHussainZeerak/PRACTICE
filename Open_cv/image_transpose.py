import cv2
import numpy as np
img=cv2.imread("d.jpg")
rotated_img=cv2.transpose(img)
cv2.imshow("original image",img)
cv2.imshow("rotated image",rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()