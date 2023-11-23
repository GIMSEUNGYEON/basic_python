import cv2

cap = cv2.VideoCapture("sarang.mp4")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

while cap.isOpened():
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    
    for (x,y,h,w) in faces:
        cropped = frame[y:y+h, x:x+w]
        # cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
        cropped = cv2.resize(cropped, (w//15, h//15))
        cropped = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y+h, x:x+w] = cropped 
        
    if ret : 
        cv2.imshow('frame',frame)
        
    if cv2.waitKey(1) == 113:
        break
cap.release()
cv2.destroyAllWindows()