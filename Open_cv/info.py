# how to get image info.
import  cv2
img=cv2.imread("d.jpg")
cv2.imshow("output",img)
gry=cv2.cvtColor(img,6)
cv2.imshow("gray image",gry)
print(img.shape)
print("height in pixel is:",img.shape[0])
print("width in pixel is:",img.shape[1])
print("layer in pixel is:",img.shape[2])
cv2.waitKey(0)
cv2.destroyAllWindows()