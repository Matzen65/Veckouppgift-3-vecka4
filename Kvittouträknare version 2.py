"""
Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
Hur många är ni? 3
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!
"""
pris_person = 25
antal = int(input("Hur många är ni? "))

if antal >= 1:
    pris_tot = pris_person * antal
    print(f"Det blir {pris_tot} alltså {pris_person} kronor per person")


