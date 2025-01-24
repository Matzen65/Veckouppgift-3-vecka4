
# Veckouppgift3 vecka 4, Öva på loopar och listor
#----------------------------------------------------

# Svar: 1a Skriv färdigt kodexemplet.

answer = 0
for i in range(1,11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

#----------------------------------------------------
#Svar: 1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

answer = 0
for i in range(1,101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))

#----------------------------------------------------
# Svar: 1c Skriv om 1b så att den använder en while-loop.

answer = 0
i=0
while(i <= 100):
    answer += i
    i += 1
print("Summan av talen 1 till 100 är: " + str(answer))

#----------------------------------------------------
# Svar: 2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]

element = 0
list = [1, -2, 3, -2, 4, -3]
element = sum(list)
print(element)

#----------------------------------------------------
# 3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
# Svar: 3a  Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar.
#           Skriv ut hela listan 2med funktionen print.

movies = ["Alien", "Twins", "Mad Max", "Matrix"]
#print(movies)                      #version 1 skriver ut vanlig lista
#print(*movies, sep = "\n")         # version 2 skriver ut innehåll med ny rad
print()
print("Svar 3a. Nedan är listan med fyra filmer utskriven rad för rad")
x = 0                               # version 3 räknare som skriver ut med ny rad
for x in range(len(movies)):
    print(movies[x])

#----------------------------------------------------
# svar: 3b Lägg till "Fellowship of the ring" sist i listan.
print()
print("Svar 3b. Nedan är listan efter att ha lagt in Fellowship of the ring The two towers i sista positionen...")
movies = ["Alien", "Twins", "Mad Max", "Matrix"]
movies.append("Fellowship of the ring")
for x in range(len(movies)):
    print(movies[x])

#----------------------------------------------------
# Svar: 3c Lägg till "The two towers" på första platsen i listan. (index noll)
# Med insert(position, new_entry) kan man skapa en ny post på valfri position

movies.insert(0,"The two towers ")
print()
print("Svar 3c. Nedan är listan efter att ha insert The two towers i första positionen...")
x = 0                               # version 3 räknare som skriver ut med ny rad
for x in range(len(movies)):
    print(movies[x])
#----------------------------------------------------
# svar: 3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
print()
print("Svar 3d. The Fellowship of the ring, har nu position",(movies.index("Fellowship of the ring")), "i listan")

#----------------------------------------------------
# Svar: 3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?

movies.remove("Mad Max")
position = movies.index("Fellowship of the ring") + 1
print("Svar 3e. Efter att ha tagit bort Mad Max, har nu The Fellowship of the ring, position",(position), "i listan")

#----------------------------------------------------
# svar: 3f Ta reda på hur lång listan är. (len)

print("Svar 3f. Det finns nu", len(movies), "filmer i listan")

#----------------------------------------------------
# Svar: 3g Vänd listan baklänges.

movies.reverse()
print("Svar 3g. Listan ör nu i omvänd ordning enligt...", (movies))

#----------------------------------------------------
# Svar: 3h Sortera listan stigande i bokstavsordning.

movies.sort()
print("Svar 3g. Listan ör nu i bodstavsordning enligt...", (movies))

