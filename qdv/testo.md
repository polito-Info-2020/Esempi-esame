# Esempio d'esame "Qualità della Vita"

Consideriamo gli indicatori della _Qualità della vita_ nelle diverse province italiane, pubblicate da _Il Sole 24 ORE_
il 14/12/2020 e disponibili on-line alla pagina https://github.com/IlSole24ORE/QDV in formato CSV, nel file denominato
`20201214_QDV2020_001.csv`.

Si realizzi un programma Python che, a partire dai dati presenti nel file, permetta all'utente di scegliere uno degli
indicatori considerati (campo `INDICATORE`, nella sesta colonna) e stampi il valore di tale indicatore (campo `VALORE`
nella quinta colonna) per tutte le province, in ordine decrescente, a fianco del nome della provincia stessa (campo
`DENOMINAZIONE CORRENTE`, quarta colonna).

Il programma dovrà scoprire gli indicatori possibili analizzando il contenuto del file, e presenterà un semplice _menù_ 
all'utente, che potrà scegliere (inserendo un numero intero) l'indicatore di suo interesse. Si noti che esistono 90
indicatori diversi definiti nel file.

## Formato del file

Il formato del file è documentato alla pagina https://github.com/IlSole24ORE/QDV e la prima riga contiene i nomi
dei campi. Tale prima riga è la seguente:
```
"NOME PROVINCIA (ISTAT)","CODICE NUTS 3 2021","CODICE PROVINCIA ISTAT (STORICO)","DENOMINAZIONE CORRENTE","VALORE","INDICATORE","UNITA' DI MISURA","RIFERIMENTO TEMPORALE","FONTE ORIGINALE"
```
Tutti i campi sono delimitati da virgole, e i campi di tipo testuale sono ulteriormente delimitati da virgolette doppie
(che non fanno parte del dato). Nota: nel file originale, in alcuni casi il carattere `,` compariva all'interno di alcuni
campi testuali. Questo è stato rimosso nel file fornito in questo esercizio, per semplicità di lettura.

Si più assumere che il formato del file sia corretto.

## Esempio

All'avvio il programma mostrerà l'elenco degli indicatori disponibili (nota: l'ordine non è importante):
```
Indicatori della qualità della vita:
1.
2.
3.
...ecc...
```

In seguito, l'utente inserisce l'indicatore prescelto:
```
Inserisci l'indicatore: 3
```

A questo punto, il programma stamperà la classifica delle province secondo tale indicatore (dal valore più grande al più piccolo):
```
Classifica secondo l'indicatore "XXXX":

Valle d'Aosta: 999
Napoli: 998
...ecc...
```
