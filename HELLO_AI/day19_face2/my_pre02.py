import cv2
import os
path = "img"

files = os.listdir(path)

for idx, file in enumerate(files):
    
    file = "img/" + file
    cap = cv2.VideoCapture(file)
    cnt = 0
    while cap.isOpened() :
        ret, frame = cap.read()
        folder = str(idx+100)[1:]
    
        if ret : 
            cv2.imwrite(f'pre01/{folder}/{cnt}.png', frame)
            cnt+=1
        else :
            break
