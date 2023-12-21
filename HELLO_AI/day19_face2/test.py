import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import ImageFont, ImageDraw, Image

model = tf.keras.models.load_model('cifarteam.h5')
image = cv2.imread('team.png')
image = cv2.resize(image, (622, 504))
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

imgNum  = 0

for(x,y,w,h) in faces :
    cv2.rectangle(image, (x,y), (x+w, y+h),(0,255,0), 2)
    cropped = image[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
    cropped = image[y:y + 65, x:x + 65]
    # cv2.imwrite("thumbnail" + str(imgNum) + ".png", cropped)
    cropped = cv2.resize(cropped, (32,32))
    imgNum += 1
    cv2.imshow('btob' + str(imgNum), cropped)
    cropped = cropped.reshape(1,32,32,3)
    pre = model.predict(cropped)
    print(pre)
    
    text = ""
    if np.argmax(pre)==0 :
        text = "김승연"
    elif np.argmax(pre)==1:
        text = "배유림"
    elif np.argmax(pre)==2:
        text = "우민규"
    elif np.argmax(pre)==3:
        text = "유길상"
        
    img_pillow = Image.fromarray(image)  # cv2 이미지를 Pillow 이미지로 변환

    fontpath = "fonts/gulim.ttc" #폰트 
    font = ImageFont.truetype(fontpath, 12) #글자 사이즈
    
    b, g, r, a = 0, 255, 0, 255 #폰트 색상
    
    # Pillow 이미지에 텍스트 그리기
    draw = ImageDraw.Draw(img_pillow)
    draw.text((x, y-20), text, font=font, fill=(b, g, r, a))
    
    image = np.array(img_pillow)  # Pillow 이미지를 cv2 이미지로 변환
    # image = cv2.putText(image, text, (x-10,y-10), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 0), 1, cv2.LINE_AA) 
    
cv2.imshow('result', image)
cv2.imwrite('result.png', image)
cv2.waitKey()



