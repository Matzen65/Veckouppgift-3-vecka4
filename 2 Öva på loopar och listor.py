"""
2 Öva på loopar och listor
#########################################################

1a Skriv färdigt kodexemplet.
answer = 0
for i in ????????????:
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

1c Skriv om 1b så att den använder en while-loop.


2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]


3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
3b Lägg till "Fellowship of the ring" sist i listan.
3c Lägg till "The two towers" på första platsen i listan. (index noll)
3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
3f Ta reda på hur lång listan är. (len)
3g Vänd listan baklänges.
3h Sortera listan stigande i bokstavsordning.

"""




#####################################
# Svar: 1a Skriv färdigt kodexemplet.

answer = 0
for i in range(1,11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))

#####################################
#Svar: 1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

answer = 0
for i in range(1,101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))

#####################################
# Svar: 1c Skriv om 1b så att den använder en while-loop.

answer = 0
i=0
while(i <= 100):
    answer += i
    i += 1
print("Summan av talen 1 till 100 är: " + str(answer))

#####################################
# Svar: 2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]

element = 0
list = [1, -2, 3, -2, 4, -3]
element = sum(list)
print(element)

######################################
# 3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
# Svar: 3a  Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar.
#           Skriv ut hela listan 2med funktionen print.

filmer = ["Alien", "Twins", "Mad Max", "Matrix"]




