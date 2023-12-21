from keras.datasets import cifar10
from keras.utils import np_utils
import tensorflow as tf
import numpy as np
import cv2

arr = [
    {'lbl':0, 'f':'00', 'n':'김승연'},
    {'lbl':1, 'f':'01', 'n':'배유림'},
    {'lbl':2, 'f':'02', 'n':'우민규'},
    {'lbl':3, 'f':'03', 'n':'유길상'}
   ]

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

img = cv2.imread("20.png")
img = img.reshape(1,32,32,3) / 255.0

x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)

model = tf.keras.models.load_model("face.h5")

model.summary()

pred = model.predict(img)

print(pred)
print(np.argmax(pred[0]))

lbl= np.argmax(pred[0])
print(arr[lbl]['n'])