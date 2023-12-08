import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

model = tf.keras.models.load_model('first.h5')

img = cv2.imread('4.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, dsize=(28,28))
# cv2.imshow("test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img_train = img.reshape((1, 28, 28, 1)) / 255.0

print(img_train.shape)
pred = model.predict(img_train)

answer = np.argmax(pred[0])
print(answer)