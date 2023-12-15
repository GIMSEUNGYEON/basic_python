from keras.datasets import cifar10
from keras.utils import np_utils
import tensorflow as tf

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

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = tf.keras.models.load_model("cifar_10.h5")

model.summary()

pred = model.predict(x_test)

print(pred)