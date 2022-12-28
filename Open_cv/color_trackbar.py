import cv2
import numpy as np
# we will pass object so for that we define a function here.
def Nothing(x):
    pass
# create a blank image
img=np.zeros((500,500,3),np.uint8)
cv2.namedWindow("image")
cv2.createTrackbar("R",'image',0,255,Nothing)
cv2.createTrackbar("G",'image',0,255,Nothing)
cv2.createTrackbar("B",'image',0,255,Nothing)
switch="0:OFF \n 1:ON"
cv2.createTrackbar(switch,'image',0,1,Nothing)
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1)==13:
        break
    # now get position of img component.
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos("G",'image')
    b=cv2.getTrackbarPos("B",'image')
    s=cv2.getTrackbarPos(switch,'image')
# now condition for switch.
    if s==0:
        img[:]==0
    else:
        img[:]==[b,g,r]
cv2.destroyAllWindows()
