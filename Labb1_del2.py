from math import pi
# Constants
G = 6.674 * pow(10, -11)

# Prompt the user
avstånd = float(input("Ange avstånd (km): "))*1000
omloppstid = float(input("Ange omloppstid (dygn): "))*24*60**2

# Lambda function for mass
massa = (4*pow(pi,2)*pow(avstånd,3))/(G*pow(omloppstid,2))
# fix
if __name__ == '__main__':
    # Calculate and print the earth's mass
    print(f"Jordens massa: {massa:.2e} k")
    