import re

# hur många av orden som ska printas
printa_st: int = 10

def lasInOrdenFranFil(fil:str, ord:bool = False) -> str:
    with open(fil, 'r') as f:
        text = f.read()
    if not ord: # tar bort lite skräp om det är från artikeln. Måste göras innan split.
        text = text.replace('\n',' ').replace('.', '').replace(',', '').replace('-', '').replace('–', '').replace('?', '').replace(':', '')
    # delar upp orden ord för ord.
    split_text = text.lower().replace('\n',' ').split(' ')
    return split_text

def rensaVanligaOrd(artikel:list[str], vanliga_ord:list[str])-> list:
   filtrerade_ord = []
   for word in artikel:
        if (word == '') or (word in vanliga_ord) or not word.isalpha():
            continue
        filtrerade_ord.append(word)
   return filtrerade_ord 

def raknaOvanliga(artikel:list[str], unika_ord:str):
    for i,ord in enumerate(unika_ord):        
        unika_ord[i] = [ord, artikel.count(ord)]
    sorterat = sorted(unika_ord, key=lambda par: par[1])[::-1]
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