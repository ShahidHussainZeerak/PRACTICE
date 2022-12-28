import cv2
import numpy as np
windowname='Drawing'
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowname)
# mouse click back function:
def Draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0))
    if event==cv2.EVENT_MBUTTONDOWN:
         cv2.circle(img,(x,y),50,(0,0,255))
    if event==cv2.EVENT_RBUTTONDBLCLK:
      cv2.circle(img,(x,y),60,(255,0,0))
cv2.setMouseCallback(windowname,Draw_circle)
while True:
    cv2.imshow(windowname,img)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()  