import cv2
import numpy as np
img=cv2.imread("d.jpg")
cv2.imshow("original img", img)
cv2.waitKey(0)
#create shraping kernel
kerenl_sharp=np.array([[-1,-1,-1],
                         [-1,9,-1],
                        [-1,-1,-1]])
#apply diffrent kerenl to different image.
sharped=cv2.filter2D(img,-1,kerenl_sharp)
cv2.imshow('Sharp img',sharped)
cv2.waitKey(0)
cv2.destroyAllWindows()