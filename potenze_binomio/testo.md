# Esempio esame "Potenze binomio"

Si scriva un programma in grado di calcolare la _potenza di un binomio_ del tipo `(ax + by)**N`, dove `x` e `y` sono le
variabili indipendenti, `a` e `b` sono coefficienti reali, ed `N` è un intero positivo.

Il programma deve acquisire dall'utente una sola volta il valore dei coefficienti `a` e `b`, ed in seguito potrà
acquisire più valori di `N`. Per ciascun valore di `N`, il programma stamperà l'espressione del polinomio potenza. Il
programma termina quando `N=0`.

Esempio:

```
Potenze del binomio (ax+by)^N
Inserisci a: 1
Inserisci b: 2
Calcolo le potenze  (1.0x + 2.0y)^N
Inserisci N: 3
Risultato: 1.0 x^3 + 6.0 x^2 y + 12.0 x y^2 + 8.0 y^3 
Inserisci N: 5
Risultato: 1.0 x^5 + 10.0 x^4 y + 40.0 x^3 y^2 + 80.0 x^2 y^3 + 80.0 x y^4 + 32.0 y^5 
Inserisci N: 0
```

Per il calcolo dei coefficienti del polinomio potenza, costruire una funzione `tartaglia(N)` che calcoli
il _triangolo di Tartaglia_ fino all'ordine `N`, sotto forma di lista di liste:
`[ [1], [1,1], [1,2,1], [1,3,3,1] ... ]`
