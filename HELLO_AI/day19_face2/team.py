import cv2
import os

arr = [
    {'lbl':'0', 'f':'0', 'n':'김승연'},
    {'lbl':'1', 'f':'1', 'n':'배유림'},
    {'lbl':'2', 'f':'2', 'n':'우민규'},
    {'lbl':'3', 'f':'3', 'n':'유길상'}
   ]

cnt = 0

def mp4ToImg(myname, folder_name):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    global cnt
    cap = cv2.VideoCapture(f"img/{myname}.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
    
        if ret:
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
            for(x,y,w,h) in faces :
                cropped = frame[y:y + h, x:x + w]
                small = cv2.resize(cropped, (32,32))
                cv2.imwrite(f'team/{folder_name}/{cnt}.png', small)
            cnt += 1
        else:
            break

for a in arr :
    print(a['n'], a['f'])
    mp4ToImg(a['n'], a['f'])
    