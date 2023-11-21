import cv2

print(cv2.__version__)

image = cv2.imread('sukgu.jpg')

print(image)

cv2.imshow('손석구씨', image)

img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('손석구씨 흑백', img2)


cv2.waitKey()



