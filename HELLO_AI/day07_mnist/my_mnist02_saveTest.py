import tensorflow as tf
from tensorflow import keras
import cv2

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# cv2.imshow(f"img/{y_train[0]}/{y_train[0]}.png", x_train[59999])

for idx, i in enumerate(x_train) :
    cv2.imwrite(f"img/{y_train[idx]}/{idx}.png", x_train[idx])

# cv2.waitKey()