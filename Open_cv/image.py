import cv2
img=cv2.imread("d.jpg")

cv2.imshow("output image", img)
# cv2.waitKey(0)
gry=cv2.cvtColor(img,6)
cv2.imshow("gray image",gry)
cv2.waitKey(0)
cv2.destroyAllWindows()