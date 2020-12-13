import csv
# from matplotlib import pyplot

FILENAME = '01TXYOV_2020.csv'

# Leggi l'elenco degli studenti e salvalo in un array
def leggi(nomefile):
  file = open(nomefile, 'r')
  reader = csv.reader(file)

  # prima = True
  # studenti = []
  # for line in reader:
  #   if prima: #skip first line (headers)
  #     prima = False
  #   else:
  #     studenti.append(line)

  studenti = list(reader) # ogni riga del file va in un elemento della lista
  del studenti[0] # cancella la prima riga (contiene i nomi delle colonne)

  file.close()
  return studenti

# estrai i nomi di battesimo da un elenco di studenti
def nomi(elenco):
  # nomi = []
  # for riga in elenco:
  #   nomi.append(riga[2])

  nomi = [ riga[2] for riga in elenco ]

  return nomi

# Calcola le frequenze dei vari nomi presenti in un array
def frequenze(tokens):
  freq = {}

  # for token in tokens:
  #   if token in freq:
  #     freq[token]= freq[token]+1
  #   else:
  #     freq[token] = 1

  uniquetokens = set(tokens) # elimina i duplicati
  for token in uniquetokens:
    freq[token] = len([tok for tok in tokens if tok==token])

  return freq

# calcola il massimo valore presente nelle frequenze
def maxFrequenza(freq):
  return max(freq.values())

def nomiPiuFrequenti(freq, max):
  return [nome for (nome, frequenza) in freq.items() if frequenza==max]

if __name__=='__main__':
  stud = leggi(FILENAME)
  nomi = nomi(stud)
  print(f"Nella classe ci sono {len(stud)} studenti")
  freq = frequenze(nomi)
  max = maxFrequenza(freq)
  print(f"Il nome più frequente compare {max} volte")
  nomiMax = nomiPiuFrequenti(freq, max)
  print(f"Si tratta di : {nomiMax}")
  # estrai solo i nomi che compaiono almeno 2 volte
  freq2 = { k:v for (k,v) in freq.items() if v>=2}
  print(f"I nomi che compaiono più di una volta sono {', '.join(sorted(list(freq2.keys())))}.")

  # pyplot.barh(list(freq2.keys()), freq2.values())
  # pyplot.show()

