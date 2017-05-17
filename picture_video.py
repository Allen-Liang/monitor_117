import numpy as np  
import cv2
import time 
  
cap = cv2.VideoCapture(0)  
c = 1  
  
while(cap.isOpened()):  
    ret, frame = cap.read()  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    time.sleep(0.5)  
    cv2.imwrite('image/'+str(c) + '.jpg',frame)
    c = c+1  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
cap.release()  
cv2.destroyAllWindows() 