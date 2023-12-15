import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

x_test_ori = x_test

x_train = x_train.reshape((60000, 28, 28, 1))/255.0
x_test = x_test.reshape((10000, 28, 28, 1))/255.0

model = tf.keras.models.load_model('fashion.h5')

pred = model.predict(x_test)

for idx, i in enumerate(x_test_ori) : 
    goog = y_test[idx]
    myidx = np.argmax(pred[idx])
    if goog != myidx :
        cv2.imwrite(f"img/x/{myidx}_{goog}_{idx}.png", x_test_ori[idx])
        # 예상_실제답_인덱스
