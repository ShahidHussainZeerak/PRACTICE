import cv2
import numpy as np
img=cv2.imread("d.jpg")
# store height and width of image 
height,width=img.shape[:2]
print(height)
print(width)
# quarter the height and length.this is Translational factor.
quarter_height,quarter_width=height/4,height/4
print(quarter_height)
print(quarter_width)

# translational matrix.
T=np.float32([[1, 0, quarter_width],[0, 1, quarter_height]])

print(T)
#use warpaffine to shift image from one side to other.
img_translation=cv2.warpAffine(img, T, (width,height))
cv2.imshow("original image",img)
cv2.imshow("Translation",img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
