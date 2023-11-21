import cv2

print(cv2.__version__)

image = cv2.imread('btob.jpg')

cv2.imwrite('./botob.png', image)

cv2.imshow('btob', image)

cv2.waitKey()

print(image)


