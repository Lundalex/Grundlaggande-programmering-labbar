# Constants
G = 6.674 * pow(10, -11)

# Prompt the user
avstånd = float(input("Ange avstånd (m): "))
omloppstid = float(input("Ange omloppstid (s): "))

# Lambda dunction for mass
massa = lambda d, T: d * T
fix
if __name__ == '__main__':
    # Calculate and print the earth's mass
    print("Jordens massa: " + str(massa(avstånd, omloppstid)) + " gk") f string