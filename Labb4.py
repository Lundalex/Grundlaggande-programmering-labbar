class country:
    def __init__(self, name: str, population: int, landlocked: bool):
        self.name = name
        self.population = population
        self.landlocked = landlocked
        
def split_line(line:str):
    parts = []
    # Split line by commas, and then strip away white spaces
    for part in line.split(","):
        part:str = part.strip()
        parts.append(part)
        
    return parts
        
def get_data_from_file(path: str):
    
    # Load file text data
    with open(path) as f:
        lines = f.readlines()
    
    # Extract the data for each line  of text (each country)
    countries = []
    for line in lines:
        parts = split_line(line)
        
        # Four data items for each country
        if len(parts) < 4:
            continue # skip if data is odd
        
        # Map the data
        name = parts[0]
        # area = float(parts[1]) (unused data)
        population = int(parts[2])
        landlocked = (parts[3] == "Y")

        countries.append(country(name, population, landlocked))

    return countries

def get_landlocked_countries(countries):
    landlocked_countries = []
    for country in countries:
        if (country.landlocked):
            landlocked_countries.append(country)
            
    return landlocked_countries

def green_str(str: str):
    return "\033[92m" + str + "\033[0m"

def print_green(str: str):
    print(green_str(str))

def print_countries(countries):
    for country in countries:
        print_green(country.name)
        
def print_stats_from_countries(countries):
    
    # Calculate stats
    num_countries = len(countries)
    tot_population = 0
    for country in countries: sum
        tot_population += country.population
    
    # Print stats
    print_green(f"Totalt bor i dessa {num_countries} länder {tot_population} människor")

if __name__ == '__main__':
    # Get data
    path = "./europa.txt"
    countries = get_data_from_file(path)

    # Filter data
    landlocked_countries = get_landlocked_countries(countries)

    # Print results from data
    print_green("I Europa har följande länder inte tillgång till hav:")
    print_countries(landlocked_countries)
    print_stats_from_countries(landlocked_countries)