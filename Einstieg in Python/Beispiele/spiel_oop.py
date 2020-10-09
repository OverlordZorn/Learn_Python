import random

# Definition der Klasse Spiel
class Spiel:
    def __init__(self):

        # Start des Spiels
        random.seed()
        self.richtig = 0

        # Anzahl bestimmen
        self.anzahl = -1
        while self.anzahl < 0 or self.anzahl>10:
            try:
                self.anzahl = int(input("Wie viele Aufgaben? 1-10: "))
            except:
                continue # Beendet die momentane Iteration und fängt mit der nächsten an

    # Methode spielen() definieren
    def spielen(self):
            
        #Spielablauf
        for i in range(1,self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def __str__(self):
        # Ergebnis
        return "Richtig: " + str(self.richtig) + " von " + str(self.anzahl) + " Aufgaben!"


# Defintion der Klasse Aufgabe
class Aufgabe:
    # Aufgabe initialisieren
    def __init__(self, i, anzahl):
        self.nr = i
        self.gesamt = anzahl

    # Aufgabe stellen
    def __str__(self):
        a = random.randint(10,30)
        b = random.randint(10,30)
        self.ergebnis = a + b
        return "Aufgabe " + str(self.nr) + " von " + str(self.gesamt) + ": " + str(a) + " + " + str(b) + " = ?"

    # Aufgabe beantworten
    def beantworten(self):
        try:
            if self.ergebnis == int(input()):
                print(self.nr, ": *** Richtig ***")
                return 1
            else:
                raise
        except:
            print(self.nr, ": *** Falsch ***")
            return 0
            
        


# Hauptprogramm

s = Spiel()
s.spielen()
print(s)

