from ctypes.wintypes import RGB
import cv2
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)
if cap.isopened():
    ret,frame=cap.read()
    print(ret)
    print(frame)
else:
    ret=False
img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.title("Live image")
plt.xticks([])
plt.yticks([])
plt.show()
cap.release()
