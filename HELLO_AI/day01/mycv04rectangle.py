import cv2

print(cv2.__version__)

image = cv2.imread('sukgu.jpg')

yellow = (0,255,255)
cv2.rectangle(image, 
              (400,100),
              (750,500),
              yellow, 
              thickness=1)

cv2.rectangle(image,
              (400, 100, 350, 400),
              (0,0,255),
              1
              )
print(image)

cv2.imshow('손석구씨', image)
cv2.waitKey()


