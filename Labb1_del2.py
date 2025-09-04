from math import pi
# Constants
G = 6.674 * pow(10, -11)

# Lambda function for mass
massa = lambda s, T : (4*pow(pi,2)*pow(s,3))/(G*pow(T,2))
# fix
if __name__ == '__main__':
    # Prompt the user
    avstånd = float(input("Ange avstånd (km): "))*1000
    omloppstid = float(input("Ange omloppstid (dygn): "))*24*60**2

    # Calculate and print the earth's mass
    print(f"Jordens massa: {massa(avstånd, omloppstid):.2e} kg")