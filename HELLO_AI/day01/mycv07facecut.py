import cv2

print(cv2.__version__)

image = cv2.imread('btob.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
# scaleFactor : 얼굴을 인식할 때 픽셀 단위로 시작해서 점차 큰 이미지의 범위를 감지하여 얼굴을 탐색하는데, 이렇게 점차 크기를 키울때
# 다음 크기를 얼만큼 크게 찾을지 정하는 값, 일반적으로 1.1 사용
# minNeighbors : 얼굴을 감지하는 데 사용되는 정교한 정도. 높을 수록 정교해지며, 3에서 5정도의 값을 사용
# minSize : 얼굴로 인식할 가장 작은 크기. 30, 30 이하의 크기는 무시함

for idx, (x,y,w,h) in enumerate(faces) :
    # cv2.rectangle(image, (x,y), (x+w, y+h),(0,255,0), 2)
    # cropped = image[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
    cropped = image[y:y + h, x:x + w]
    cv2.imshow('{}'.format(idx), cropped)
    cv2.imwrite("{}.png".format(idx), cropped)
    
cv2.imshow('btob', image)

cv2.waitKey()

print(image)


