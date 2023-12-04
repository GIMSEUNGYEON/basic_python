import tensorflow as tf
from tensorflow import keras
import numpy as np
# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 입력 데이터 전처리
x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

# 모델 구성
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])
# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train)

pred = model.predict(x_test)
gg = y_test[1]
print("gg", gg)
print(pred.shape)
print(pred[1])
myidx = np.argmax(pred[1])
print("myidx", myidx)

s_cnt = 0
f_cnt = 0
for idx, i in enumerate(pred) :
    if y_test[idx] == np.argmax(i) :
        s_cnt +=1
    else :
        f_cnt +=1
        
print("맞춘 개수",s_cnt)
print("틀린 개수", f_cnt)
print("합", s_cnt + f_cnt)