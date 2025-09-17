# hur många av orden som ska printas
printa_st: int = 10

def lasInOrdenFranFil(fil:str, ord:bool = False) -> str:
    '''Läser in orden från filen vi väljer'''
    def ersätt_flera(text:str,ersätt_lista:list):
        '''En inre funktion som tar bort tecknen i ersätt_lista'''
        for sträng in ersätt_lista:
            text = text.replace(sträng, '')
        return text
    with open(fil, 'r') as f:
        text = f.read()
    if not ord: # tar bort lite skräp om det är från artikeln. Måste göras innan split.
        text = ersätt_flera(text, ['.', ',', '-', '–', ':','(',')'])
    # delar upp orden ord för ord.
    split_text = text.lower().replace('\n',' ').split(' ')
    return split_text

def rensaVanligaOrd(artikel:list[str], vanliga_ord:list[str]) -> list:
   filtrerade_ord = []
   for word in artikel:
        # skippar om vanliga ord eller ogiltiga ord
        if (word == '') or (word in vanliga_ord) or not word.isalpha():
            continue
        filtrerade_ord.append(word)
   return filtrerade_ord 

def raknaOvanliga(artikel:list[str], unika_ord:list[str]) -> list:
    for i,ord in enumerate(unika_ord):       
        # Vi ersätter unika ordet med [unika ordet, antal av det i artikeln] 
        unika_ord[i] = (ord, artikel.count(ord))
    # vi sorterar listan efter andra värdet, alltså count värdet ovan. Sedan flippar vi runt listan i andra hållet
    sorterat = sorted(unika_ord, key=lambda par: par[1], reverse=True) # Här är key vad den sorterar på. I vårt fall andra värdet i listan alltså ordet och inte antalet
    return sorterat

def printaLista(lista):
    global printa_st
    for par in lista[:printa_st]:
        print(f'\033[91m Ordet "{par[0]}" förekommer {par[1]} st gånger \033[0m')

if __name__ == '__main__':
    print('\033[91m Ange en fil att granska: ' + '\033[0m')
    fil_granska = (input("\033[32m") + "\033[0m")[:-4]
    artikel = lasInOrdenFranFil(fil=fil_granska)
    vanliga_ord = lasInOrdenFranFil(fil='vanligaord.txt', ord=True)
    artikel = rensaVanligaOrd(artikel, vanliga_ord)
    unika_ord = list(set(artikel))
    räknad_lista = raknaOvanliga(artikel, unika_ord)
    printaLista(räknad_lista)