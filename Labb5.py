from sys import path
def hamtaSyror() -> str:
    '''Försöker hämta syror från filen aminosyror.txt'''
    # Vi börjar med att öppna filen
    try:
        with open('aminosyror.txt') as f:
            syror_i_ordning = f.read().replace('\t', '').replace('\n', '\n')
    except FileNotFoundError:
        exit(f'File aminosyror.txt not found in {path[0].split('/')[-1]}')
    print('reading aminoacids...\n...done.')
    return syror_i_ordning

def hämtaVal():
    val = int(input("""Välj ett av följande:
    1 - Lista alla aminosyror
    2 - Spara en sekvens av aminosyror (peptid)
    3 - Lista alla sekvenser sorterare i viktordning
    4 - Avsluta\n"""))
    return val

# Denna tar bort 
def formatera_lista(syror_i_ordning:str) -> list[list[str]]:
    # tar bort skumma karaktärer som '\t' och delar sedan upp stringen för varje ny rad 
    syralista1:list[str] = syror_i_ordning.replace('\t','').split('\n')
    ny_fixad_syralista = []
    for syra in syralista1:
        splittad_syra = syra.split() # ex: ['P', 'Prolin', 'hydrofob', '115.13']
        if len(splittad_syra) != 4:
            continue
        ny_fixad_syralista.append((splittad_syra[0], splittad_syra[-1])) # tar med bokstav och nummer för senare beräkningar
    return ny_fixad_syralista[:-1]# tar bort sista för blankraden

def add_value_sequence_to_list(skapad_sekvens, syror_lista:list):
    totalt_värde:float = 0
    for char in skapad_sekvens:
        bokstavs_lista = [par[0] for par in syror_lista]
        index_of_bokstav = bokstavs_lista.index(char)
        värde = syror_lista[index_of_bokstav][1]
        totalt_värde+= float(värde)
    return totalt_värde
def mainloop():
    sekvenser = {}
    syror_i_ordning = hamtaSyror()
    syror_lista = formatera_lista(syror_i_ordning)
    choice = 1 # arbiträrt nummer != 0. Uppdateras sen
    while choice:
        choice = hämtaVal()
        match choice:
            case 1:
                print(syror_i_ordning)
            case 2:
                sekvens = input('Ange en sekvens:\n')
                värde = add_value_sequence_to_list(sekvens, syror_lista)
                sekvenser[sekvens] = värde
            case 3:
                for sekvens in sekvenser.keys():
                    print(f'{sekvens}:{round(värde,2)}')

if __name__ == '__main__':
    mainloop()