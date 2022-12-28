# how to convert rgb to gry
import cv2
img=cv2.imread("Kristen-Stewart.jpg",0)  #direct method to convert rgb to gray scale image just worte 0 with file name.
cv2.imshow("RGB image",img)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # indirect method of converting rgb to gry scale image
# cv2.imshow("gray scale",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
