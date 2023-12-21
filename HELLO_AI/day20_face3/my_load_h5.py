from keras.datasets import cifar10
from keras.utils import np_utils
import tensorflow as tf
import numpy as np

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)

model = tf.keras.models.load_model("face.h5")

model.summary()

preds = model.predict(x_train)

print(preds.shape)
for pred in preds :
    print(np.argmax(pred), end="\t")