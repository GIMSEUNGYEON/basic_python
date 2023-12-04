import tensorflow as tf
from tensorflow import keras

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = tf.keras.models.load_model('firsth5.h5')
model.summary() # 모델의 대략적인 정보를 출력해주는 메서드
pred = model.predict(x_test)

print(pred.shape)

