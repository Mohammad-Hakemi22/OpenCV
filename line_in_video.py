import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while(True):
    ret,frame = cap.read()
    # color= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.rectangle(frame, (100,200),(300,400),(0,255,0),10)
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'this is for test',(305,405),font,5,(100,0,0),3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()