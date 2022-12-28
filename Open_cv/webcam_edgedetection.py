import cv2
from numpy import mask_indices
def sketch(img):
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    canny_edge=cv2.Canny(img_gray_blur,70,255)
    ret,mask=cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    return mask
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("our Live sketch",sketch(frame))
    if cv2.waitKey(1)==13:
        break
cv2.release()
cv2.destroyAllWindows()