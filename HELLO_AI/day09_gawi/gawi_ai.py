import tensorflow as tf
import numpy as np

x_train = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

y_train = np.array([
    2,0,1
])

model = tf.keras.models.load_model('gawi.h5')

pred = model.predict(x_train)

print(pred)

while True :
    mine = input('가위 바위 보 : ')
    
    if mine == '가위' : 
        x_rf = np.array([
            [1,0,0] # 가위   
        ])
    elif mine == '바위':
        x_rf = np.array([
            [0,1,0] # 바위    
        ])
    elif mine == '보':
        x_rf = np.array([
            [0,0,1] # 보    
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
    if com == 2:
        com_ans = "보"
    elif com == 0 :
        com_ans = "가위"
    elif com == 1 :
        com_ans = "바위"
    
    result = ""
    print("com : " + com_ans)
    if mine == com_ans :
        result = "비김"
        
    elif mine == "가위" and com_ans == "바위" :
        result = "짐"
    elif mine == "가위" and com_ans == "보" :
        result = "이김"
        
    elif mine == "바위" and com_ans == "가위" :    
        result = "이김"
    elif mine == "바위" and com_ans == "보" :
        result = "짐"
        
    elif mine == "보" and com_ans == "가위" :
        result = "짐"
    elif mine == "보" and com_ans == "바위" :
        result = "이김"
    
    print(result)