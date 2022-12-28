import cv2
import numpy as np
img=cv2.imread("Kristen-stewart.jpg")
#extract height.
height,width=img.shape[:2]
#rotation Matrix.
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),45,.6)
rotated_image=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow("original Image",img)
cv2.imshow("Rotated image",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()