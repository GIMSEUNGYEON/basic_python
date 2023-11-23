import cv2

# 첫 번째 이미지 읽기
image1 = cv2.imread('sukgu.jpg')

# 두 번째 이미지 읽기 (투명한 배경을 가진 PNG 파일)
image2 = cv2.imread('mask/116.png', cv2.IMREAD_UNCHANGED)

# 합칠 좌표 (예시)
x, y = 100, 50

# 두 번째 이미지의 크기
height, width, _ = image2.shape

# 합칠 좌표에 따라 이미지 크기를 조정
roi = image1[y:y+height, x:x+width]

# 알파 채널 추출
alpha_channel = image2[:, :, 3]

# 원본 이미지에 알파 채널을 적용하여 두 이미지를 합침
result = cv2.addWeighted(roi, 1.0, image2[:, :, :3], alpha_channel / 255.0, 0)

# 합쳐진 부분을 원본 이미지에 적용
image1[y:y+height, x:x+width] = result

# 합쳐진 이미지 보기
cv2.imshow('Merged Image', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()