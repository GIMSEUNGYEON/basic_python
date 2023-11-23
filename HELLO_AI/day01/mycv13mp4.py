import cv2

cap = cv2.VideoCapture("sarang.mp4")

while cv2.waitKey(33) < 0:
    ret, frame = cap.read()
    if ret : 
        cv2.imshow("VideoFrame", frame)
    else :
        break
    
cap.release()
cv2.destroyAllWindows()