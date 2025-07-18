# 🔢 Importazione delle librerie necessarie
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# `numpy` serve per operazioni numeriche
# `tensorflow` è il framework che contiene Keras
# `layers` e `models` ci servono per costruire la rete
# `matplotlib.pyplot` serve per disegnare grafici (es. accuratezza, loss)
class Model:
    def __init__(self):
        self.model = models.Sequential()
        #layer di input
        self.model.add(layers.Input(shape=(64, 64, 3)))
        # Aggiungiamo uno strato convoluzionale con 32 filtri 3x3, attivazione ReLU, 32 kernel 
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu'))
        # Segue uno strato di max pooling 2x2 (riduce dimensione e mantiene caratteristiche)
        self.model.add(layers.MaxPooling2D((32, 32)))
        # Secondo strato convoluzionale con 64 filtri 3x3
        #self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        #self.model.add(layers.MaxPooling2D((50, 50)))
        # Terzo strato convoluzionale
        #self.model.add(layers.Conv2D(32, (3, 3), activation='relu'))
        # Appiattiamo il tensore per passarlo a uno strato fully connected
        self.model.add(layers.Flatten())
        # Strato denso con 64 neuroni e ReLU
        self.model.add(layers.Dense(64, activation='relu'))
        # Strato di output con 10 neuroni (uno per cifra), attivazione softmax per classificazione
        self.model.add(layers.Dense(9, activation='softmax'))
    
    
    def compile(self, optimizer, loss, metrics):
         # ⚙️ Compilazione del modello
       return self.model.compile(optimizer=optimizer,   # `adam` è un algoritmo di ottimizzazione che funziona bene nella pratica
                    loss=loss,  # `categorical_crossentropy` è la funzione di errore per classificazione multiclasse
                    metrics=metrics)   # `accuracy` è la metrica che ci interessa monitorare

    
    def training (self, x_train, y_train_cat, epochs, batch_size, validation_split):
        # 🚂 Addestramento del modello
        history = self.model.fit(x_train, y_train_cat,
                            epochs=epochs,
                            batch_size=batch_size, #i pesi vengono aggiornati dopo 64 immagini
                            #fa la media dei valori delle 64 immagini e poi aggiorna
                            validation_split=validation_split) #splitta validation e train)

        # `epochs=5`: il modello passerà 5 volte su tutti i dati di training
        # `batch_size=64`: aggiorna i pesi ogni 64 immagini
        # `validation_split=0.1`: usa il 10% dei dati per la validazione durante l'addestramento
        return history
        
    def predict(self, X_test):
        y_pred_scaled = self.model.predict(X_test)
        return y_pred_scaled

    def evaluation (self, x_test, y_pred_cat):
        # ✅ Valutazione sul test set
        test_loss, test_acc = self.model.evaluate(x_test, y_pred_cat)
        return f"Test accuracy: {test_acc:.2f}, \n Test loss: {test_loss:.2f}"

        # Usiamo i dati di test per vedere se il modello generalizza bene