import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0],
    [0,1]
])

y_train = np.array([
    1,0
])

model = tf.keras.models.load_model('holl.h5')

pred = model.predict(x_train)

print(pred)

test_loss, test_acc = model.evaluate(x_train, y_train)

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
