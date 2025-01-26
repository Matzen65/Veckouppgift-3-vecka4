"""
Version 3: programmet ska fråga hur många procent dricks man vill lägga på.
Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

Nice to have: prova att använda try+except eller isdigit för att hantera de fall när användaren skriver ett felaktigt värde.
Python Try Except , isdigit | StackOverflow
("Nice to have" handlar om funktionalitet som inte är nödvändig, men som är bra att ha.
Gå gärna vidare till nästa uppgift och återvänd till den här om du vill lära dig mer.)

"""

pris_person = 25
antal = int(input("Hur många är ni? "))
dricks_input = 0

if antal >= 1:
    pris_tot = pris_person * antal
    print(f"Det blir {pris_tot} alltså {pris_person} kronor per person")
    dricks_input =input("Hur många procent extra dricks vill ni lägga på? ")

    try:
        val = int(dricks_input)+10
        pris_tot = pris_tot + (pris_tot * val) / 100

    except ValueError:
        val = 10
        pris_tot = pris_tot + (pris_tot * val) / 100
print("Ert slutliga pris inklusive",val,"% dricks blir", pris_tot, "kr")