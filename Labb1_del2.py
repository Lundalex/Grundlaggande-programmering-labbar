G = 6.674 * pow(10, -11)

avstånd = float(input("Ange avstånd (m): "))
omloppstid = float(input("Ange omloppstid (s): "))

massa = lambda d, T: d * T

print("Jordens massa: " + str(massa(avstånd, omloppstid)) + " gk")