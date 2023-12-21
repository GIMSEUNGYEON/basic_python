import cv2
from day20_face3.my_pred_oop import AiFace
from PIL import ImageFont, ImageDraw, Image
import numpy as np
print(cv2.__version__)

image = cv2.imread('team_1000_750.png')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
af = AiFace()

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

for idx, (x,y,w,h) in enumerate(faces) :
    
    cropped = image[y:y + h, x:x + w]
        
    cropped = cv2.resize(cropped, (32,32))
    
    myname = af.getNameByImg(cropped)
    cv2.rectangle(image, (x,y), (x+w, y+h),(255,0,0), 2)
    
    img_pillow = Image.fromarray(image) 

    font = ImageFont.truetype("fonts/gulim.ttc", 20)

    draw = ImageDraw.Draw(img_pillow)
    draw.text((x, y-20), myname, font=font, fill=(255, 255, 0, 255))
    
    image = np.array(img_pillow) 
    
cv2.imshow('Face Detection', image)

cv2.waitKey()



