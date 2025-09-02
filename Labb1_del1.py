def calculate_money(start, inter, t):
    return start * pow((1 + inter), t)

if __name__ == '__main__':
    # Prompt the user
    money_start = int(input("Ange ditt belopp (kr): "))
    time = int(input("Ange den tid som beloppet kommer förräntas (år): "))
    interest = 0.01 * int(input("Ange räntan (%/år): "))

    # Calculate and print the predicted amount of money
    money_end = calculate_money(money_start, interest, time)
    print(f"Beräknad slutsumma: {money_end:.2f} kr")