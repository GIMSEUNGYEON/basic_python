from keras.datasets import cifar10
from keras.utils import np_utils
import tensorflow as tf
import numpy as np
import cv2
class AiFace :
    def __init__(self):
        self.model = tf.keras.models.load_model("face.h5")
        
    def getNameByImg(self, img):
        arr = [
            {'lbl':0, 'f':'00', 'n':'김승연'},
            {'lbl':1, 'f':'01', 'n':'배유림'},
            {'lbl':2, 'f':'02', 'n':'우민규'},
            {'lbl':3, 'f':'03', 'n':'유길상'}
           ]
    
        img = img.reshape(1,32,32,3) / 255.0
        
        pred = self.model.predict(img)
        
        lbl= np.argmax(pred[0])
        return arr[lbl]['n']

if __name__ == '__main__':
    af = AiFace()
    
    img = cv2.imread('pre01/00/10.png')
    
    myname = af.getNameByImg(img)
    
    print(myname)