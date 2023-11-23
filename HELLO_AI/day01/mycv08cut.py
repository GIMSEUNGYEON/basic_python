import cv2

print(cv2.__version__)

image = cv2.imread('btob.jpg')

cropped = image[:, 500]
    
cv2.imshow('btob', image)
cv2.imshow('crop', cropped)

cv2.waitKey()

print(image)


