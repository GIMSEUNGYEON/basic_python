import cv2

print(cv2.__version__)

image = cv2.imread('btob.jpg')
(h, w) = image.shape[:2]
# image.shape 는 이미지의 높이와 너비를 가진 튜플이므로 0인덱스(높이)를 h에 1인덱스(너비)를 w에 담는 구문
(cX, cY) = (w / 2, h / 2)

img45 = cv2.getRotationMatrix2D((cX, cY), -45, 1.0)
rotated = cv2.warpAffine(image, img45, (w,h))
    
cv2.imshow('btob', image)
cv2.imshow('rotate Test', rotated)
cv2.waitKey()

print(image)

