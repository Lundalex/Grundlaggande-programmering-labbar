import math

def print_menu():
    print("""
1 - Mata in de tävlandes resultat.
2 - Se statistik för tidigare inmatade
3 - Avsluta""")

def get_standard_deviation(values, mean, num):
    # Calculate variance from this formula: https://stackoverflow.com/questions/35583302/how-can-i-calculate-the-variance-of-a-list-in-python
    # (fancy syntax for a for loop)
    variance = sum((x - mean) ** 2 for x in values) / num
    return math.sqrt(variance)

def inmatning(): # Gathers input data
    participants_num = int(input("Hur många tävlande: "))
    
    # Creata and populate m_inputs
    m_inputs = list()
    for i in range(participants_num):
        m = float(input(f"Ange för deltagare {i+1} (m): "))
        m_inputs.append(m)
    
    return m_inputs

def statistik(): # Calculates and shows statistics data
    # Validate data
    participants_num = len(m_participants)
    if (participants_num <= 0):
        print("Inga deltagare inmatade. Återvänder till menyn...")
        return
    
    # Calculate the mean and max values
    min_m = min(*m_participants)
    max_m = max(*m_participants)
    mean = sum(m_participants) / participants_num
    
    # Calculate the standard deviation
    standard_deviation = get_standard_deviation(m_participants, mean, participants_num)
    
    print(f"Medelvärdet är {mean:.2f}m med standardavvikelse {standard_deviation:.2f}m. Högsta värde var {max_m:.2f}m och det lägsta {min_m:.2f}m")
     
if __name__ == '__main__':
    m_participants = []
    while (True):
        print_menu()
        choice = int(input("Ditt val: "))
        
        # Choice 3
        # I could also use match if on pyhton 1.13
        if (choice == 3):
            exit()
        
        # Choice 1
        if (choice == 1): m_participants = inmatning()
        
        # Choice 2
        else: statistik()