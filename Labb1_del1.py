money_start = int(input("Ange ditt belopp (kr): "))
time = int(input("Ange den tid som beloppet kommer förräntas (år): "))
interest = 0.01 * int(input("Ange räntan (%): "))

def calculate_money(start, inter, t):
    return money_start * pow((1 + interest), time)

money_end = calculate_money(money_start, interest, time)
print("Beräknad slutsumma: " + str(money_end) + " kr")