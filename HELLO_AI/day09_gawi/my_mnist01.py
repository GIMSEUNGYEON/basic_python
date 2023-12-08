import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

y_train = np.array([
    0,1,2
])

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(3,)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 모델 훈련
model.fit(x_train, y_train, epochs=20)

model.save('gawi.h5')

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
    [1,0,0] # 가위
])

pred_rf = model.predict(x_rf)

print(np.argmax(pred_rf))


