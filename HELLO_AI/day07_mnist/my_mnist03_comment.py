import tensorflow as tf
from tensorflow import keras

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 입력 데이터 전처리(정제)
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0
# 3차원 배열을 신경망에 맞춰주기 위해 4차원 배열로 만들고 있음 부동 소수점을 만들기 위해 255로 나누어서 모든 수를 1 미만 실수로 만듦

# 모델 구성(신경망 구성)(컴파일하기까지)(cnn)
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])
# Flatten : 다차원 배열을 1차원 배열로 나열 
# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.2)
# epoch : 5번 반복
# batch_size : 전체 데이터를 한번에 학습하기에 메모리 과부하 및 속도 저하 문제가 발생하므로 지정한 크기만큼 쪼개어 여러번 학습시키는 것.

# 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
# accuracy : 대략적인 정확도