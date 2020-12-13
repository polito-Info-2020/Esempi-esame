# Esempio esame "Statistiche Comuni"

Si consideri un file in formato testuale contenente le informazioni sui comuni italiani (`Elenco-comuni-italiani.csv`)
in cui vi sia l'informazione di un comune per ciascuna riga del file, con i campi separati dal carattere '`;`'.

Si realizzi un programma in linguaggio Python che, dopo avere letto le informazioni contenute nel file, permetta
all'utente di inserire il nome di una regione italiana, e per tale regione stampi:

- il numero di comuni presenti in tale regione
- il comune il cui nome ha il numero minimo di caratteri (a parità di lunghezza, si stampi quello che viene prima in
  ordine alfabetico)
- il comune il cui nome ha il numero massimo di caratteri (a parità di lunghezza, si stampi quello che viene prima in
  ordine alfabetico)

Il programma ripeterà l'elaborazione finché l'utente non inserirà '`***`' come nome di regione.

## Note di formato
- La prima riga del file deve essere ignorata in quanto contiene i nomi dei campi 
- Il nome del comune si trova nel settimo campo
- Il nome della regione si trova nell'undicesimo campo 
  
## Esempio di riga del file:
```01;201;001; 006 ;001006;Almese;Almese;;1;Nord-ovest;Piemonte;Torino;3;0;TO;1006;1006;1006;1006;A218;ITC;ITC1;ITC11```

(Fonte dati: https://www.istat.it/it/archivio/6789)
