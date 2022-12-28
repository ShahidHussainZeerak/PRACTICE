import cv2
import numpy as np
img=cv2.imread("ks.jpg")
cv2.imshow("original image",img)
cv2.waitKey(0)
# extract height and width.
height,width=img.shape[:2]
#get the start pixel (row and column) of the image.
start_row,start_col=int(height*.40),int(width*.45)
#get the end pixel (row and column) of the image.
end_row,end_col=int(height*60),int(width*.55)
# use indexing method to cropped the image.
cropped=img[start_row:end_row,start_col:end_row]
cv2.imshow("cropped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
