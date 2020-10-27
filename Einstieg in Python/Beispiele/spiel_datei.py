# Module
import random, time, glob, pickle

# Funktion Highscore lesen

def hs_lesen():
    # Liste wird hier erzeugt
    global hs_liste
    
    # Kein Highscore vorhanden, leere Liste
    if not glob.glob("highscore.bin"):
        hs_liste = []
        return

    # Highscore vorhanden, laden
    d = open("highscore.bin", "rb")
    hs_liste = pickle.load(d)
    d.close()

# Funktion Highscore anzeigen
def hs_anzeigen():
    # Highscore nicht vorhanden
    if not hs_liste:
        print("Keine Highscores vorhanden")
        return

    # Ausgabe Highscore
    print(f"{'P':>2}. {'Name':10}{'Zeit':>5}")
    for i in range(len(hs_liste)):
        print(f"{(i+1):>2d}. {hs_liste[i][0]:10}{hs_liste[i][1]:5.2f}")
        if i >= 9:
            break
    print()

# Funktion Highscore schreiben
def hs_schreiben():
    # Zugriff
    d = open("highscore.bin", "wb")
    pickle.dump(hs_liste,d)
    d.close()

# Funkton Spiel
def spiel():
    # Eingabe des Namens
    name = input("Bitte geben Sie ihren Namen ein (max. 10 Zeichen): ")
    name = name[0:10]

    # Initialisierung Counter und Zeit
    richtig = 0
    startzeit = time.time()

    #  5 Aufgaben
    for aufgabe in range(5):
        # Aufgabe mit Ergebnis
        a = random.randint(10,100)
        b = random.randint(10,100)
        c = a + b

        # Eingabe
        try:
            zahl = int(input("Aufgabe " + str(aufgabe+1) + "von 5: " + str(a) + " + " + str(b) + " = "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print("*** Falsch ***")

    # Auswertung
    endzeit = time.time()
    differenz = endzeit - startzeit
    print(f"Ergebnis: {richtig:d} von 5 in {differenz:.2f} Sekunden", end="")
    if richtig == 5:
        print(", Highscore!")
    else:
        print(", leider kein Highscore")
        return
    
    # Mitten in Liste schreiben
    gefunden = False
    for i in range(len(hs_liste)):
        # Einsetzen in Liste
        if differenz < hs_liste[i][1]:
            hs_liste.insert(i, [name, differenz])
            gefunden = True
            break
    # Ans Ende der Liste schreiben
    if not gefunden:
        hs_liste.append([name, differenz])
    
    # Highscore-Liste anzeigen
    hs_anzeigen()

# Hauptprogramm

# Initialisierung Zufallsgenerator
random.seed()

# Highscore aus Datei in Liste lesen
hs_lesen()

# Endlosschleife
while True:
    # Hauptmenü, Auswahl

    try:
        menu = int(input("0: Ende \n1: Highscores \n2: Spielen\nBitte Wählen: "))
    except:
        print("Falsche Eingabe")
        continue
    print()
    # Aufruf einer FUnktion oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs_anzeigen()
    elif menu == 2:
        spiel()
    else:
        print("Falsche Eingabe")

# Highscore aus Liste in Datei schreiben
hs_schreiben()