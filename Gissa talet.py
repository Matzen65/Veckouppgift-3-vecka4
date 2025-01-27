"""5 Gissa talet
Gör ett spel som slumpar ett hemligt tal mellan 1 och 100.
Sedan ska man försöka gissa det. Om man gissar för lågt eller för högt ska spelet tala om det.
Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
secret = random.randint(1, 100)

Exempel:
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
Gissa: 40
Nej, det är för lågt!
Gissa: 55
Nej, det är för högt!
Gissa: 51
Det är rätt!! Du gjorde det på 3 gissningar.

Version 2: skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
"Nu börjar det brännas!"
"""

import random

secret = (random.randint(1, 100))
guess = 0
tries = 0
print("hemliga talet är", secret)
print()
print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

while guess != secret:
    guess = int(input("Gissa: "))
    tries = tries + 1
    if guess < secret:
        print("för lågt, gissa igen: ")
        if (secret - guess <= 5):
            print("Det bränns")
    elif guess > secret:
        print("för högt, gissa igen: ")
        if (guess - secret <= 5):
            print("Det bränns")
print("Det är rätt!!! Du klarade det på ",tries, "gissningar")