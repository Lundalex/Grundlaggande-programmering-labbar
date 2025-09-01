from sys import path
def hamtaSyror() -> str:
    '''Försöker hämta syror från filen aminosyror.txt'''
    # Vi börjar med att öppna filen
    try:
        with open('aminosyror.txt') as f:
            syror_i_ordning = f.read().replace('\t', '').replace('\n', '\n')
    except FileNotFoundError:
        exit(f'File aminosyror.txt not found in {path[0].split('/')[-1]}')
    return syror_i_ordning

def printaVal():
    print("""Välj ett av följande:
        1 - Lista alla aminosyror
        2 - Spara en sekvens av aminosyror (peptid)
        3 - Lista alla sekvenser sorterare i viktordning
    4 - Avsluta""")

# Denna tar bort 
def formatera_lista(syror_i_ordning:str) -> list[list[str]]:
    # tar bort skumma karaktärer som '\t' och delar sedan upp stringen för varje ny rad 
    syralista1:list[str] = syror_i_ordning.replace('\t','').split('\n')
    ny_fixad_syralista = []
    for syra in syralista1:
        ny_fixad_syralista.append(syra.split()) # lägger till delarna när alla mellanslag tagits bort och den har splittats där dem var.
    return ny_fixad_syralista

# lite variabler som används senare
syralista = formatera_lista(syror_i_ordning)
CHOOSE_COMMAND: str = """Välj ett av följande:
1 - Lista alla aminosyror
2 - Spara en sekvens av aminosyror (peptid)
3 - Lista alla sekvenser sorterare i viktordning
4 - Avsluta"""
list_of_sequences:list = []

def add_value_sequence_to_list(sekvens:str):
    global list_of_sequences
    for char in sekvens:
        pass

def mainloop():
    global CHOOSE_COMMAND
    syror_i_ordning = hamtaSyror()
    choice:int = 1 # värde som inte gör något
    while choice:
        printaVal()
        match choice:
            case 1:
                print(syror_i_ordning)
            case 2:
                add_value_sequence_to_list(input('Ange en sekvens:\n'))

        choice = input(CHOOSE_COMMAND)

if __name__ == '__main__':
    mainloop()
