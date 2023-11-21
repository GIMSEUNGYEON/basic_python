import cv2

print(cv2.__version__)

image = cv2.imread('btob.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

imgNum  = 0

for(x,y,w,h) in faces :
    cv2.rectangle(image, (x,y), (x+w, y+h),(0,255,0), 2)
    cropped = image[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
    cv2.imwrite("thumbnail" + str(imgNum) + ".png", cropped)
    imgNum += 1
    
cv2.imshow('btob', image)

cv2.waitKey()

print(image)


