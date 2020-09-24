"""
Verbessern Sie das Programm zur Eingabe und Umrechnung eines
beliebigen Inch-Werts in Zentimeter. Eingabefehler des Anwenders
sollen abgefangen werden. Das Programm soll den Anwender so lange
zur Eingabe auffordern, bis sie erfolgreich war.
"""

# init loop until 0

zahl = 1
print("Um das Programm zu beenden, geben Sie 0 ein")

while zahl != 0:
    # init fehlerabfang
    fehler = 1

    while fehler == 1:
        print("Bitte geben sie einen Wert als Inch ein, um diesen in Zentimeter umzurechnen.")
        

        z = input()

        try:
            zahl = float(z);
            if zahl == 0:
                break
            print(zahl, "Inch sind umgerechnet", zahl*2.54, "cm!")
            fehler = 0
        except:
            print("Der eingegebene Wert ist keine Zahl!")

print("Sie haben das Programm erfolgreich beendet")
