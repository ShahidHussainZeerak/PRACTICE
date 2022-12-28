import cv2
img=cv2.imread("d.jpg",0)  #direct method to convert rgb to gray scale image just worte 0 with file name.
cv2.imshow("RGB image",img)
ret,bi=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret mean return it is used to save the value of different layer.
cv2.waitKey(0)
cv2.destroyAllWindows()