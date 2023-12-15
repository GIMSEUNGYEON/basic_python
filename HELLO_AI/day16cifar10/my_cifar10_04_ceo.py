from keras.datasets import cifar10
from keras.utils import np_utils
import tensorflow as tf
import numpy as np
import cv2

# airplane : 0
# automobile : 1
# bird : 2
# cat : 3
# deer : 4
# dog : 5
# frog : 6
# horse : 7
# ship : 8
# truck : 9
(x_train, y_train), (x_test, y_test) = cifar10.load_data()



x_test_ori = x_test

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

print(x_test[0])
print(y_test[0])

model = tf.keras.models.load_model("cifar_10.h5")

model.summary()

pred = model.predict(x_test)

for idx, i in enumerate(x_test_ori) :
    goog = np.argmax(y_test[idx])
    myidx = np.argmax(pred[idx])
    if goog != myidx :
        cv2.imwrite(f"img/x/{idx}_{myidx}_{goog}.png", x_test_ori[idx])