# Animal-Model-Recognition

Link sui siti Kaggle per i dataset:
1. Animals: https://www.kaggle.com/datasets/alessiocorrado99/animals10/data
2. Sea Creature: https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste?select=Jelly+Fish


Struttura del progetto:

1) Creazione del rumore delle immagini circa 10 esempi per ogni immagine, per evitare overfitting, e che la rete impari a memoria.
   
2) Creazione del dataset, prese le due cartelle elencate sopra, estratte le immmagini, sporcate e inserite in un dataset, a tensore, con etichetta nome degli animali.
   
3) Preprocess dei dati, come conversione dei pixel da 0-255 a 0-1, gestione dei punti di precisione, come da int64, a float32, per ridurre l'uso di ram, split dei dati di train e test, e relative etichette. applicazione del OHE alle etichette.
   
4) Modello, una rete CNN, che prende in input i dati preprocessati, e poi passa in output MaxPooling 3x3, da un immagine iniziale 64x64, ad una rete Densa, per predirre la classe di appartenenza tramite la SoftMax.
   
5) La rete presenta 8 layer, 2 di convoluzione, 2 di MaxPooling, 1 di input, 1 di flatten, 1 layer di output, e 1 layer fully connected Denso. (non elencati in ordine)
    
6) Infine, presenta un grafico che riconosce gli animali predetti, e quelli veri.

