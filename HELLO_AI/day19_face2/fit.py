import cv2
import os
import numpy as np
import tensorflow as tf
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten

x_train_arr = []
y_train_arr = []

for folder in range(4) :
    folder_path = 'team/' + str(folder) + '/'
    print(folder_path)
    for i in os.listdir(folder_path):
        img = folder_path + i
        imgs = cv2.imread(img, cv2.IMREAD_COLOR)
        x_train_arr.append(imgs)
        y_train_arr.append(folder)

x_train = np.array(x_train_arr)
y_train = np.array(y_train_arr)
np.save("x_train",x_train)
np.save("y_train",y_train)

x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)

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

model.add(Dense(4, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

hist = model.fit(x_train, y_train,
                 epochs=10,
                 batch_size=4,
                 validation_data=(x_train, y_train))

pred = model.predict(x_train)
print(pred)
model.save('cifarteam.h5')