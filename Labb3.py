# hur många av orden som ska printas
printa_st: int = 7

def lasInOrdenFranFil(fil:str, ord:bool = False) -> str:
    with open(fil, 'r') as f:
        text = f.read()
    if not ord: # tar bort lite skräp om det är från artikeln. Måste göras innan split.
        text = text.replace('.', '').replace(',', '').replace('-', '').replace('–', '').replace('?', '').replace(':', '')
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

def raknaOvanliga(artikel:list[str], unika_ord:str) -> list:
    for i,ord in enumerate(unika_ord):       
        # Vi ersätter unika ordet med [unika ordet, antal av det i artikeln] 
        unika_ord[i] = (ord, artikel.count(ord))
    # vi sorterar listan efter andra värdet, alltså count värdet ovan. Sedan flippar vi runt listan i andra hållet
    sorterat = sorted(unika_ord, key=lambda par: par[1], reverse=True)
    return sorterat

def printaLista(lista):
    global printa_st
    for par in lista[:printa_st]:
        print(f'Ordet "{par[0]}" förekommer {par[1]} st gånger')

if __name__ == '__main__':
    fil_granska = input('Ange en fil att granska: ')
    artikel = lasInOrdenFranFil(fil=fil_granska)
    vanliga_ord = lasInOrdenFranFil(fil='vanligaord.txt', ord=True)
    artikel = rensaVanligaOrd(artikel, vanliga_ord)
    unika_ord = list(set(artikel))
    räknad_lista = raknaOvanliga(artikel, unika_ord)
    printaLista(räknad_lista)