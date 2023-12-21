import cv2
import os

file = '../img/김민경.mp4'
cap = cv2.VideoCapture(file)

cnt = 0
while cap.isOpened() :
    ret, frame = cap.read()
    
    if ret : 
        cv2.imwrite('kmk{}.png'.format(cnt), frame)
        cnt+=1
    else :
        break
    if cv2.waitKey(1) & 0xff == ord('q') :
        break
        
cap.release()
cv2.destroyAllWindows()