import tensorflow as tf
import numpy as np
# 1. MNIST 데이터셋 임포트
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# print("x_train", x_train.shape)
# print("y_train", y_train.shape)

# 2. 데이터 전처리
# x_train, x_test = x_train/255.0, x_test/255.0

x_train = np.array([
    [1,0],
    [0,1]
])

y_train = np.array([
    0,1
])

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(2,)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 훈련
model.fit(x_train, y_train, epochs=20)

model.save('holl.h5')

pred = model.predict(x_train)

print(pred)

# 6. 정확도 평가
test_loss, test_acc = model.evaluate(x_train, y_train)
print('테스트 정확도:', test_acc)

for p in pred :
    print("p",p)
    print(np.argmax(p))
# accuracy : 정확도(Dense가 클수록 커짐)
# loss : 근접한 정도(epoch가 클수록 줄어듬)
print("+=======================+")
x_rf = np.array([
    [1,0] # 홀
])

pred_rf = model.predict(x_rf)

print(np.argmax(pred_rf))


