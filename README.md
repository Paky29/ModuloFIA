# ModuloFIA
Il sistema proposto consiste nella realizzazione di un sistema di raccomandazione che suggerisca un insieme di libri ad un utente sulla base dei prestiti effettuati e delle valutazioni che quest’ultimo e gli altri utenti hanno espresso relativamente ai libri del catalogo. Inoltre, il sistema utilizza le caratteristiche dell’utente e dei libri per fornire i consigli migliori.

La directory [dataset](https://github.com/Paky29/ModuloFIA/tree/master/dataset) contiene i dataset originali, estratti da Kaggle, e i dataset processati.  
La directory [model](https://github.com/Paky29/ModuloFIA/tree/master/model) contiene il codice python per generare il modello di machine learning.  
La directory [utility](https://github.com/Paky29/ModuloFIA/tree/master/utility) contiene:  

* [analysis_threshold.py](https://github.com/Paky29/ModuloFIA/blob/master/utility/analisys_threshold.py) contiene le funzioni utilizzate per variare la rating threshold
* [preprocessing.py](https://github.com/Paky29/ModuloFIA/blob/master/utility/preprocessing.py) contiene le funzioni necessarie per data preparation
* [visualization.py](https://github.com/Paky29/ModuloFIA/blob/master/utility/visualization.py) contiene le funzioni utilizzate per creare i grafici
* [manageModel.py](https://github.com/Paky29/ModuloFIA/blob/master/utility/manageModel.py) contiene le funzioni per il caricamento e il salvataggio del model
* [searchParameters.py](https://github.com/Paky29/ModuloFIA/blob/master/utility/searchParameters.py) contiene le funzioni che permettono di ottenere il modello con i parametri migliori

La directory [presentazione](https://github.com/Paky29/ModuloFIA/tree/master/presentazione) contiene la presentazione power point del modulo.
