import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from time import time

bef = time()

x_train = np.load("D:/py_temp/x_train1.npy")
y_train = np.load("D:/py_temp/y_train1.npy")
x_test = np.load("D:/py_temp/x_test1.npy")
y_test = np.load("D:/py_temp/y_test1.npy")

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

print('y_train :', np.shape(y_train))

width = 32
height = 32
channel = 3

model = Sequential(name='CIFAR10_CNN')

model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu', 
                 input_shape=(width, height, channel)))
model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

hist = model.fit(x_train, y_train,
                 epochs=1,
                 batch_size=32,
                 validation_data=(x_test, y_test))


aft = time()

print(aft - bef)

# 그래프를 그리기 위한 matplotlib 라이브러리
# import matplotlib.pyplot as plt
#
# # Training Loss VS Validation Loss 비교를 위한 그래프 그리기 
# plt.plot(hist.history['loss'], 'y', label='train loss')
# plt.plot(hist.history['val_loss'], 'r', label='val loss')
#
# # y축 범위 설정
# plt.ylim([0.0, 2.5])
#
# # 각 축의 이름 정하기
# plt.xlabel('epoch')
# plt.ylabel('loss')
#
# # 각 그래프의 설명 위치 설정 후 표시
# plt.legend(loc='upper left')
#
# plt.show()