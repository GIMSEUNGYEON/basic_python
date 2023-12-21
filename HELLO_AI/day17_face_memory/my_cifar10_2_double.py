import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train1 = x_train
y_train1 = y_train
x_test1 = x_test
y_test1 = y_test

for i in range(1, 15+1) :
    x_train = np.append(x_train, x_train1)
    x_train = x_train.reshape(-1, 32, 32, 3)
    print(x_train.shape)
    np.save("D:/py_temp/x_train{}".format(i), x_train)

    y_train = np.append(y_train, y_train1)
    y_train = y_train.reshape(-1, 1)
    print(y_train.shape)
    np.save("D:/py_temp/y_train{}".format(i), y_train)

    x_test = np.append(x_test, x_test1)
    x_test = x_test.reshape(-1, 32, 32, 3)
    print(x_test.shape)
    np.save("D:/py_temp/x_test{}".format(i), x_test)

    y_test = np.append(y_test, y_test1)
    y_test = y_test.reshape(-1, 1)
    print(y_test.shape)
    np.save("D:/py_temp/y_test{}".format(i), y_test)

