import cv2

print(cv2.__version__)

image = cv2.imread('sukgu.jpg')
image2 = cv2.imread('sukgu.jpg', 0)
image3 = cv2.imread('sukgu.jpg', -1)
# 이미지 읽기

cv2.imshow('손석구씨', image)
cv2.imshow('손석구씨 회색', image2)
cv2.imshow('손석구씨 알파', image3)
# 새 창을 띄워 이미지 출력
cv2.waitKey()
# 대기시간 설정(안하면 출력이 안되는데 이유는 모르겠음)

print(image)

# cv2.destroyAllWindows()

