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
while True :
    mine = input('홀 짝 : ')
    
    if mine == '홀' : 
        x_rf = np.array([
            [1,0] # 홀    
        ])
    elif mine == '짝':
        x_rf = np.array([
            [0,1] # 짝    
        ])
    elif mine =='종료' : 
        print("게임 종료")
        break
    else : 
        print('잘못된 입력!')
        continue
    pred_rf = model.predict(x_rf)
    com = np.argmax(pred_rf)
    com_ans = ""
    if com == 0:
        com_ans = "홀"
    else :
        com_ans = "짝"
        
    print("com : " + com_ans)
    if mine == com_ans :
        print("user 승리")
    else :
        print("com 승리")
