import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape((60000, 28, 28, 1))/255.0
x_test = x_test.reshape((10000, 28, 28, 1))/255.0

model = tf.keras.models.load_model('firsth5.h5')

pred = model.predict(x_test)

for idx, i in enumerate(y_test) : 
    goog = i
    myidx = np.argmax(pred[idx])
    if goog != myidx :
        cv2.imwrite(f"x/{idx}_{myidx}_{goog}.png", x_test[idx]*255)
        # 인덱스_예상한 숫자_실제 표현하고있는 숫자
    
