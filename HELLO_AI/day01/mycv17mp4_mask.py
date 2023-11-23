import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture('sarang.mp4')
img = cv2.imread("./mask/116.png", cv2.IMREAD_UNCHANGED)  
v = 20

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    for (x, y, w, h) in faces:
        roi_img = cv2.resize(img, (w, h))
    
        alpha_channel = roi_img[:, :, 3] / 255.0
        roi_color = frame[y:y+h, x:x+w, :3]
        
        for c in range(3):
            roi_color[:, :, c] = (1 - alpha_channel) * roi_color[:, :, c] + alpha_channel * roi_img[:, :, c]
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()