import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_test_ori = x_test

x_train = x_train.reshape((60000, 28, 28, 1))/255.0
x_test = x_test.reshape((10000, 28, 28, 1))/255.0

model = tf.keras.models.load_model('firsth5.h5')

pred = model.predict(x_test)

for idx, img in enumerate(x_test_ori) :
    myidx = np.argmax(pred[idx])
    goog = y_test[idx]
    # print(idx, "myidx", myidx, goog)
    if myidx != goog :
        cv2.imwrite('x/{}_{}_{}.png'.format(idx, myidx, goog), img)