# Kvittouträknaren version 1
#=============================

summa = 0
user_input = ""
tal = 0
print()
print("Välkommen till Kvittokompis! Skriv in ett belopp, avsluta genom att skriva: 'avsluta' eller 'quit'")
print()
while True:
    user_input = input("Skriv in ett belopp: ")

    if user_input == "quit" or user_input == "avsluta":
        print()
        print(f"Det blir {summa} kr totalt. Välkommen åter!")
        break
    summa += int(user_input)
    print(f"     Running total : {summa}")
