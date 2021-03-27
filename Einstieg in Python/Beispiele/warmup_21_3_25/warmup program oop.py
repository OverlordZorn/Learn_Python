import random, time, glob
# Hauptprogramm
while True:
    # Hauptmenü, Auswahl
    try:
        menu = int(input("Bitte eingeben 0: Ende, 1: Highscore, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue
    
    # Anlegen eines Objekts oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs = Highscore()
        print(hs)
    elif menu == 2:
        s = Spiel()
        s.messen(True)
        s.spielen()
        s.messen(False)
        print(s)
    else:
        print("Falsche Eingabe")


# Klasse "Spiel"
class Spiel:
    def __init__(self):
        #Start des Spiels
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): ")
        self.spieler = s[0:10]
    
    def spielen(self):
        # Spielablauf
        for i in range(1,self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig = a.beantworten()
    
    def messen(self, start):
        # Zeitmessung
        if start:
            self.startzeit = time.time()
        else:
            endzeit = time.time()
            self.zeit = endzeit - startzeit

    def __str__(self):
        # Ergebnis
        ausgabe = f"Richtig: {self.richtig:d} von {self.anzahl:d} in {self.zeit:.2f} Sekunden"
        if self.richtig == self.anzahl:
            ausgabe += ", Highscore"
            hs = Highscore()
            hs.speichern(self.spieler, self.zeit)
            print(hs)
        else:
            ausgabe += ", leider kein Highscore"
        return ausgabe

# KLasse "Highscore"
class Highscore:
    # Liste aus Datei lesen
    def __init__(self):
        self.liste = []
        if not glob.glob("highscore.csv"):
            return
        
        d = open("highscore.csv")
        zeile = d.readline()
        while zeile:
            teil = zeile.split(";")
            name = teil[0]
            zeit = teil[1][0:len(teil[1])-1]
            zeit = zeit.replace (",", ".")
            self.lsite.append([name, float(zeit)])
            zeile = d.readline()
        d.close()

    # Liste Ändern