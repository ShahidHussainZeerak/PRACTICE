# how to write in image.
import cv2
img=cv2.imread("kivanic1.jpg")
cv2.imshow("original image ",img)
cv2.imwrite("original.jpg",img)
cv2.imwrite("original.png",img)

cv2.waitKey(0)
cv2.destroyAllWindows()