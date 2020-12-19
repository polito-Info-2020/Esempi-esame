# Soluzione proposta esempio "Morse"

FILE_MORSE = 'morse.txt'


def leggi_testo(nomefile):
    try:
        infile = open(nomefile, 'r')
    except:
        exit('Impossibile aprire il file')

    linea = infile.readline()
    if linea != '':
        linea = linea.rstrip('\n')
    else:
        exit('Il file è vuoto!')

    infile.close()
    return linea


def leggi_morse():
    morsefile = open(FILE_MORSE, 'r')
    conversione = []
    for line in morsefile:
        campi = line.strip().split()
        regola = {
            'testo': campi[0].upper(),
            'morse': campi[1]
        }
        conversione.append(regola)
    return conversione


def codifica(testo, conversione):
    msg = ''
    for ch in testo:
        if ch.upper() in conversione:
            msg = msg + conversione[ch.upper()] + ' '
    return msg


def decodifica(testo, conversione):
    msg = ''
    simboli = testo.strip().split()
    for simbolo in simboli:
        if simbolo in conversione:
            msg = msg + conversione[simbolo]
    return msg


def main():
    conversione = leggi_morse()

    conversione_testo_morse = {}
    conversione_morse_testo = {}
    for regola in conversione:
        conversione_testo_morse[regola['testo']] = regola['morse']
        conversione_morse_testo[regola['morse']] = regola['testo']

    op = ''
    while op != 'c' and op != 'd':
        op = input('Che operazione vuoi fare? codifica (c) o decodifica (d): ')
        op = op.strip().lower()

    file_name = input('Nome del file da elaborare: ')

    messaggio = leggi_testo(file_name)

    if op == 'c':
        risultato = codifica(messaggio, conversione_testo_morse)
    else:
        risultato = decodifica(messaggio, conversione_morse_testo)
    print('Messaggio tradotto:', risultato)


main()
