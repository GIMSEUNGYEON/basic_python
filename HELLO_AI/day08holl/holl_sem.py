import tensorflow as tf
from tensorflow import keras
import numpy as np
mine = input('홀 짝')
com = ""
mine = ""
result = ""

model = tf.keras.models.load_model('holl.h5')

pred_rf = None

if mine == "홀" :
    pred_rf = model.predict(np.array([[1,0]]))
else :
    pred_rf = model.predict(np.array([[0,1]]))

myidx = np.argmax(pred_rf)
if myidx == 1 :
    com = "짝"
else :
    com = "홀"

if com == mine : 
    result = "이김"
else :
    result = "짐"

print("mine : ", mine)
print("com : ", com)
print("result : ", result)