import tensorflow as tf
from tensorflow import keras
import cv2

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

for idx, i in enumerate(x_train):
    cv2.imwrite(f"img/{y_train[idx]}/{idx}.png", i)