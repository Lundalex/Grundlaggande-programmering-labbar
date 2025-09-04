from sys import path
def hamtaSyror() -> str:
    '''Försöker hämta syror från filen aminosyror.txt'''
    # Vi börjar med att öppna filen
    try:
        print('\033[91m reading aminoacids...\n...done.'+'\033[0m')
        with open('aminosyror.txt') as f:
            SYROR_I_ORDNING = f.read()
    except FileNotFoundError:
        exit(f'File aminosyror.txt not found in {path[0].split('/')[-1]}')
    return SYROR_I_ORDNING

def hämtaVal():

    print("""\033[91m Välj ett av följande:
    1 - Lista alla aminosyror
    2 - Spara en sekvens av aminosyror (peptid)
    3 - Lista alla sekvenser sorterare i viktordning
    4 - Avsluta\n"""+"\033[0m")
    

    val = input("\033[32m") + "\033[0m" # skumma bokstäver här för att ta in i färg grön
    return int(val[:-4])

# Denna tar bort 
def formatera_lista(SYROR_I_ORDNING:str) -> list[list[str]]:
    # tar bort skumma karaktärer som '\t' och delar sedan upp stringen för varje ny rad 
    syralista1:list[str] = SYROR_I_ORDNING.split('\n')
    ny_fixad_syralista = []
    for syra in syralista1:
        splittad_syra = syra.split() # ex: ['P', 'Prolin', 'hydrofob', '115.13']
        if len(splittad_syra) != 4:
            continue
        ny_fixad_syralista.append((splittad_syra[0], splittad_syra[-1])) # tar med bokstav och nummer för senare beräkningar
    return ny_fixad_syralista # tar bort sista för blankraden

def add_value_sequence_to_list(skapad_sekvens, syror_lista:list):
    totalt_värde:float = 0
    bokstavs_lista = [par[0] for par in syror_lista]
    for char in skapad_sekvens:
        index_of_bokstav = bokstavs_lista.index(char)
        värde = syror_lista[index_of_bokstav][1]
        totalt_värde+= float(värde)
    return totalt_värde

def mainloop():
    # variabler
    sekvenser = {}
    SYROR_I_ORDNING = hamtaSyror()
    syror_lista = formatera_lista(SYROR_I_ORDNING)
    choice = 1 # arbiträrt nummer != 0. Uppdateras sen
    while choice:
        choice = hämtaVal()
        match choice:
            case 1:
                print("\033[91m"+SYROR_I_ORDNING+"\033[0m")
            case 2:
                print('\033[91m Ange en sekvens:'+'\033[0m')
                sekvens = (input("\033[32m") + "\033[0m")[:-4] # skumma karaktärer här för att ta in i färg grön
                värde = add_value_sequence_to_list(sekvens, syror_lista)
                sekvenser[sekvens] = värde
            case 3:
                for sekvens in sekvenser.keys():
                    print(f'\033[91m {sekvens}:{round(sekvenser[sekvens],2)}'+ '\033[0m')
            case 4:
                choice = 0

if __name__ == '__main__':
    mainloop()
