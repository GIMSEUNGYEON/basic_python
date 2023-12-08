import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

x_test1 = x_test[0:1]

img = cv2.imread("4.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_28 = cv2.resize(img_gray, (28,28))
x_test1 = np.reshape(img_gray_28, (1,28,28,1)) / 255
x_test1_rev = 1 - x_test1
 
model = tf.keras.models.load_model('first.h5')
model.summary()

pred = model.predict(x_test1_rev)
print(pred)
