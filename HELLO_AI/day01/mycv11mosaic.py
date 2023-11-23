import cv2

img = cv2.imread('sukgu.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

while True :
    for idx, (x,y,w,h) in enumerate(faces) :
        cropped = img[y:y+h, x:x+w]
        cropped = cv2.resize(cropped, (w//15, h//15))
        cropped = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_AREA)
        img[y:y+h, x:x+w] = cropped 
        # cv2.imshow("{}.png".format(idx), img)
    else:
        break

# 모자이크 처리 하고싶은 부분을 따로 이미지에 저장, 저장한 부분을 특정 비율로 축소한 후 전체 비율로 다시 확대하여 
# 원본 파일의 같은 위치에 모자이크 처리된 부분을 덮어씌우기
cv2.imshow('dongsuk', img)
cv2.waitKey()
cv2.destroyAllWindows()