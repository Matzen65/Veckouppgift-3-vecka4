#4 Figurer med loopar
#Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 3 <= x <= 5:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 3 <= x < 4 or y == 3:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 5 <= x < 6 or x == (7 - y):
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y or x == (7 - y):
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        # väljer att använda udda tal(positioner)
        if x % 2 == 1:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (2 <= x <= 7 and 2 <= y <= 5) and not (3 <= x <= 6 and 3 <= y <= 4):
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 3 == (y + 1) % 3:
            s += "#"
        elif x % 3 == (y + 2) % 3:
            s += "O"
        else:
            s += "."

    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (x % 3 == 0 and y <= 3) or (x % 2 == 0 and y == 5) or (x % 2 == 1 and y == 6):
            s += "#"
        else:
            s += "."

    print(s)
