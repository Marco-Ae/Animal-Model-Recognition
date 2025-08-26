# Importazione delle librerie necessarie
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
# `numpy` serve per operazioni numeriche
# `tensorflow` è il framework che contiene Keras
# `layers` e `models` ci servono per costruire la rete
# `matplotlib.pyplot` serve per disegnare grafici (es. accuratezza, loss)
class preprocessing:
    def __init__(self):
        pass
    
    def split(self, X, Y, test_size, random_state,shuffle,stratify):
        self.x_train, self.x_test, self.y_train, self.y_test= train_test_split(X,Y, test_size=test_size, random_state=random_state, 
                                                                               shuffle=shuffle, stratify=stratify)
        return self.x_train, self.x_test, self.y_train, self.y_test
    
    def normalize(self, denominatore=255):
        #Normalizzazione dei dati
        self.x_train = self.x_train.astype('float32') / denominatore
        self.x_test = self.x_test.astype('float32') / denominatore

        #Converte in NumPy array PRIMA del reshape
        self.train_images = self.x_train.to_numpy().reshape(-1, 64, 64, 3)
        self.test_images = self.x_test.to_numpy().reshape(-1, 64, 64, 3)

        return self.train_images, self.test_images

    def le(self): #label encoding
        le=LabelEncoder()
        self.y_train_label=le.fit_transform(self.y_train)
        self.y_test_label=le.transform(self.y_test)
        return self.y_train_label,  self.y_test_label
    
    def ohe(self, num_classes): #one hot encoding
        #One-hot encoding delle etichette
        self.y_train_cat = tf.keras.utils.to_categorical(self.y_train_label, num_classes) # Le etichette da 0 a 9 vengono trasformate in vettori binari di lunghezza 10
        self.y_test_cat = tf.keras.utils.to_categorical(self.y_test_label, num_classes)
        return self.y_train_cat,  self.y_test_cat
                

