import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

np.save("x_train", x_train)
np.save("y_train", y_train)
np.save("x_test", x_test)
np.save("y_test", y_test)

# print(y_train.shape)
#
# x_train2 = np.append(x_train, x_train)
#
# x_train2 = x_train.reshape(-1, 32, 32, 3)
#
# print(x_train2.shape)


