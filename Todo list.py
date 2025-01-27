"""
6 Todo list (att göra-lista)
Bygg ett program där användaren kan lägga till saker till en todo-lista.
Tips: använd en loop, input och en variabel för listan.
Exempel:

** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
Välj ett alternativ: 1
Din lista är tom
.
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: mata guldfisken
Ok, lade till "mata guldfisken" i listan.
.
Välj ett alternativ: 1
+ Mata guldfisken
.

"""
#############################################
# version 1
"""
list =[]
print("** Todo list extravaganza **")
print("1. Se innehållet i din lista")
print("2. Lägga till nya punkter i din lista")
print()
while True:
    val = int(input("Välj ett alternativ: "))
    if val == 1:
        if not list:
            print("Din lista är tom")
        else:    
            print(list)
    if val == 2:
        item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        list.append(item)
        print(f"Ok, lade till {item} i listan")
"""

################################################
# Version 2: lägg till ett menyalternativ, "Markera som klar".
# När användaren väljer det, ska programmet fråga efter vilken
# grej man är färdig med. Den färdiga grejen ska tas bort från listan.
"""
list =[]
print("** Todo list extravaganza **")
print("1. Se innehållet i din lista")
print("2. Lägga till nya punkter i din lista")
print("3. markera som klar")
print()
while True:

    val = int(input("Välj ett alternativ: "))
    if val == 1:
        print()
        if not list:
            print("Din lista är tom")
        else:
            print(list)
    if val == 2:
        print()
        item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        list.append(item)
        print(f"Ok, du lade till {item} i listan")

    if val == 3:
        print()
        print(list)
        klar = int(input("välj en punkt ovan som är färdig: "))
        print("tar bort punkt", list[klar],"från listan")
        list.pop(klar)
        print(list)
        print()
"""

################################################
# Version 3: lägg över färdiga grejer i en ny lista.
# Användaren ska kunna välja vad man har bockat av tidigare,
# eller välja att lägga tillbaka grejen i todo-listan.

list = []
done_list = []
print("** Todo list extravaganza **")
print("1. Se innehållet i din lista")
print("2. Lägga till nya punkter i din lista")
print("3. markera som klar")
print("4. Se eller ångra tidigare klarmarkerade punker")
print()
while True:

    val = int(input("Välj ett alternativ: "))
    if val == 1:
        print()
        if not list:
            print("Din lista är tom")
        else:
            print(list)
    if val == 2:
        print()
        item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        list.append(item)
        print(f"Ok, du lade till {item} i listan")

    if val == 3:
        print()
        print(list)
        klar = int(input("välj en punkt i din lista ovan som är färdig: "))
        print("tar bort punkt", list[klar], "från listan")
        done_list.append(list[klar])
        list.pop(klar)
        print(list)
        print()

    if val == 4:
        print()
        print(done_list)
        regret = int(input("välj punkt ovan som ska läggas tillbaka i att göra listan: "))


