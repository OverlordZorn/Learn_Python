# Import Modul Random
import random
random.seed() #Zufallsgenerator initialisieren

# Zufallswerte 
a = random.randint(1,100)
b = random.randint(1,100)
c = a + b
print("Die Aufgabe:", a, "+", b)

# Schleife mit while

# Schleife initialisieren
zahl = c + 1

# Anzahl initialisieren
versuch = 0

# Eingabe
while zahl != c:
    #Anzahl Versuche
    versuch = versuch + 1
     
    # Eingabe
    print("Bitte eine Zahl eingeben:")
    zahl = int(input())

    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig!")
    else:
        print(zahl, "ist falsch")

# Anzahl ausgeben
print("Ergebnis: ", c)
print("Anzahl der Versuche:", versuch)
