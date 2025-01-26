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
        if x == 1 or x==3 or x==5 or x==7:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if  y == 2 and 3 <= x <= 6 or y == 5 and 3 <= x <= 6:
            s += "#"
        elif x==2 and 2 <= y <= 5 or x==7 and 2 <= y <= 5:
            s += "#"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if  x == y-5 or x == y-2 or x == y+1 or x == y+4 or x == y+7:
            s += "#"
        elif x == y-4 or x == y-1 or x == y+2 or x == y+5:
            s += "0"
        else:
            s += "."
    print(s)

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if  y >= 1 and y<=3 and (x == 3 or x == 6):
            s += "#"
        elif y>=5 and (x == y-5 or x == y-3 or x == y-1 or x == y+1 or x == y+3):
            s += "#"
        else:
            s += "."
    print(s)
