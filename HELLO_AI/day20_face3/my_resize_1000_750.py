import cv2

image = cv2.imread('team.png')
image = cv2.resize(image, (1008, 756))
cv2.imwrite("team_1000_750.png", image)