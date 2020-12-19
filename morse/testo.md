# Esempio d'esame 'Morse'

Si scriva un programma in linguaggio Python per la codifica e decodifica di un testo con l'alfabeto Morse. 
L'alfabeto Morse è un codice che assegna, ad ogni lettera dell'alfabeto, numero o simbolo di punteggiatura,
un codice a lunghezza variabile, costituito da punti e linee.

La tabella di conversione è contenuta nel file `morse.txt`, di cui si rappresentano le prime righe:
```
A .-
B -...
C -.-.
D -..
E .
F ..-.
G --.
(eccetera...)
```
Su ogni linea, il primo carattere rappresenta il simbolo alfamumerico, ed è seguito dalla sequenza di punti e linee corrispondente, separati da uno spazio.

Il programma richiede all'utente due informazioni:
- se deve **c**odificare (da testo a Morse) o **d**ecodificare (da Morse a testo) un messaggio (`c`/`d`)
- il nome del file da codificare/decodificare. Tale file conterrà una sola linea di testo.

Il programma dovrà quindi produrre sullo schermo la traduzione del file specificato.
  
## Note 
Il programma, nel caso di codifica, dovrà saltare la codifica di tutti i caratteri non 
presenti nel file `morse.txt`, e non dovrà distinguere tra caratteri minuscoli e maiuscoli.

Il programma, nel caso di codifica, dovrà separare con uno spazio i simboli Morse stampati come 
risultato.

Nel caso di decodifica si  assuma che  il testo da decodificare consista di simboli Morse  
separati con uno spazio. Eventuali simboli Morse non riconosciuti devono essere ignorati.

## Esempio di Esecuzione
 
Supponendo che il file  `testo.txt` contenga:
``` 
TRE TIGRI CONTRO TRE TIGRI 
```
Il risultato sarà 
```
- .-. . - .. --. .-. .. -.-. --- -. - .-. --- 
```

Supponendo che il file  codice.txt contenga:
``` 
.- .. ..- - --- ... --- ... 
```

Il risultato sarà
``` 
AIUTOSOS
``` 
