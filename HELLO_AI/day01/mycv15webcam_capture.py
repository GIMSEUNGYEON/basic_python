import cv2

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
cnt = 0

while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv2.imshow("test", frame)
        key = cv2.waitKey(1)
    if key == ord('a') :
        cv2.imwrite("{}.png".format(cnt), frame)
        cnt+=1
        # a 키를 누르면 캡쳐
    if key == 27 or key == ord('q') or cv2.getWindowProperty("test", cv2.WND_PROP_VISIBLE) < 1:
        break  # ESC 또는 q 키를 누르면 루프 탈출
webcam.release()
cv2.destroyAllWindows()