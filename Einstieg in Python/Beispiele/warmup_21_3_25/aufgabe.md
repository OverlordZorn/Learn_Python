# 8.10 Spiel, Version mit Highscore-Datei

Es folgt eine weitere Vresion des bereits bekannten Kopfrechenspiels. Die Daten des Spielers (Name und Zeit) werden mithilfe der Serialisierung (siehe 8.5) dauerhaft gespeichert, sodass eine Highscore-Liste geführt werden kann.

Es wird zunächst nach dem Namen des Spielers gefragt. Anschließend bekommt der Spieler fünf Additionsaufgaben mit Zahlen aus dem Bereich von 10 bis 30 gestellt. Pro Aufgabe hat er nur einen Versuch. Ungütlige Eingaben oder falsche Ergebnisse werden mit dem Text `Falsch` kommentiert. Zuletzt wird die Gesamtzeit angegeben, die der Spieler für die LÖsungsversuche benötzigt hat.

Falls der Spieler alle fünf Aufgaben richtig löst, werden sein Name und die benötigte Zeit in eine Highscore-Liste aufgenommen, die in einer Datei abgespeichert wird.

## 8.10.1 Eingabebeispiel

Folgend sehen Sie einen typischen Durchlauf des Programms.

```
Bitte eingeben (0: Ende, 1: Highscores, 2: Spielen): 1
P. Name                 Zeit
1. Ole              8.03 sec
2. Rudi             8.36 sec
3. Gerd             9.32 sec
4. Ben             12.13 sec
5. Tom             12.15 sec
Bitte eingeben (0: Ende, 1: Highscores, 2: Spielen): 2
Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): Paul
Aufgabe 1 von 5: 20 + 30 : 50
*** Richtig ***
Aufgabe 2 von 5: 29 + 29 : 58
*** Richtig ***
Aufgabe 3 von 5: 23 + 21 : 44
*** Richtig ***
Aufgabe 4 von 5: 29 + 10 : 39
*** Richtig ***
Aufgabe 5 von 5: 27 + 30 : 57
*** Richtig ***
Ergebnis: 5 von 5 in 9.48 Sekunden, Highscore
P. Name                 Zeit
1. 
(...)
Bitte Eingeben (0: Ende, Highscore: 1, Spielen: 2): 0
```

Der Benutzer (Paul) schaut sich zuerst die Highscores an. Dort gibt es bereits einige Einträge. Anschließend spielt er eine Runde, löst alle fünf Aufgaben richtig, und sein Name erscheint ebenfalls im Highscore. Als Letztes verlässt er das Programm.

## 8.10.2 Aufbau des Programms

Das Programm enthält ein Hauptprogramm und vier Funktionen. Im Hauptprogramm wird innerhalb einer Endlosschleife ein Hauptmenü augerufen. Darin kann sich der Spieler entweder die Highscores anzeigen lassen, spielen oder das Programm beenden.

Es folgen die vier Funktionen des Programms:

* hs_lesen(): Lesen der Highscores aus der Datei in einer Liste
* hs_anzeigen(): Anzeigen der Highscore_liste auf dem Bildschirm
* hs_schreiben(): Schreiben der Highscore-Lsite in die Datei
* spiel(): Stellen der Aufgaben, Lösen der Aufgaben, Einfügen der ermittelten Zeiten in die Highscore-Liste
  
## 8.10.3 Code des Programms

Im nachfolgenden Listing sehen Sie den Beginn des Programms mit der Funktion zum Lesen der Highscore-Daten aus der Datei:

```py
# Module
import random, time, glob, pickle

# Funktion Highscore lesen
def hs_lesen():
    # Liste wird hier erzeugt 
    global hs_liste

    # Kein Highscore vorhanden? => leere Liste
    if not glob.glob("highscore.bin"):
        hs_liste = []
        return
    
    # Highscore vorhanden! => laden
    d = open("highscore.bin", rb)
    hs_liste = pickle.load(d)
    d.close()
```

Es werden die Module `random` (zum erzeugen der Zufallszahlen), `time` (zur Zeitmessung) und `glob` (zur Prüfung der Datei) benötigt.

Nach dem Einlesen aus der Datei stehen in der Liste `hs_liste` die Namen und Ergebniszeiten der Spieler. Da die Liste in dieser Funktion erstmalig benutzt, aber im gesamten Programm benötigt wird, wird sie hier mit `global` im globalen Namensraum bekannt gemacht.

Falls die Datei nicht vorhanden ist, wird eine leere Liste erzeugt. Ist die Datei vorhanden, wird der gesamte Inhalt mithilfe der Funktion `load()` aus dem Modul `pickle` in die Liste `hs_liste` gelesen.

Es folgt die Funktion zum Anzeigen des Highscores:

```py
# Funktion Highscore anzeigen
def hs_anzeigen():
    # Highscore nicht vorhanden
    if not hs_liste:
        print("Kein Highscore vorhanden")
        return
    
    # Ausgabe Highscore
    print("P. Name                  Zeit")
    for i in range(len(hs_liste)):
        print(f"{i+1:2d}. {hs_liste[i][0]:10} {hs_liste[i][1]:5.2f} sec")
        if i >= 9:
            break
```

Falls die Highscore_lsite leer ist, wird eine entsprechende Meldung angezeigt. Ist die Liste nicht leer, werden nach einer Überschrift maximal zahn Highscores formatiert ausgegeben, und zwar mit den Informationen *Platzierung, Name, Ergebniszeit`.

Es folgt die Funktion zum Schreiben der Highscore_liste in die Datei:

```py
# Funktion Highscore schreiben
def hs_schreiben():
    # Zugriff
    d = open("highscore.bin", "wb")
    pickle.dump(hs_liste, d)
    d.close()
```

Die gesamte Liste wird mithilfe der Funktion `dump()` aus dem Modul `pickle` in die Datei geschrieben.

Es folgt die Funktion zum Spielen:

```py
# Funktion Spiel
def spielen():

    # Eingabe des Namens
    name = input("Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): ")
    name = name[0:10]

    # Initialisierung Counter und Zeit
    richtig = 0
    startzeit = time.time()

    # 5 Aufgaben
    for aufgabe in range(5):
        # Aufgabe mit Ergebnis
        a = random.randint(1,50)
        b = random.randint(50,100)
        c = a + b

        # Eingabe
        try:
            zahl = int(input("Aufgabe " + str(aufgabe+1)+ " von 5: " + str(a) + " + " + str(b) + " = "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print("* Falsch *")
    
    # Auswertung
    endzeit = time.time()
    differenz = endzeit - startzeit
    print(f"Ergebnis: {richtig:d} von 5 in {differenz.2f} Sekunden", end="")
    if richtig == 5:
        print(", Highscore!")
    else:
        print(", leider kein Highscore")
    return

# Mitten in Liste schreiben
gefunden = false
for i in range(len(hs_lsite)):
    # Einsetzen in Liste
    if differenz < hs_liste[i][1]:
        hs_liste.insert(i, [name, differnz])
        gefunden = True
        break

# Ans Ende der Liste schreiben
if not gefunden:
    hs_liste.append([name, differenz])

# Highscore_liste Anzeigen
hs_anzeigen()
```

Nach der Eingabe des Namens wird er zur einheitlichen Ausgabe auf maximal zen Zeichen verkürzt. Es folgen einige Programmteile, die bereits aus früheren Versionen des Spiels bekannt sind: Stellen der fünf Aufgaben, Eingabe der Lösungen, Bewertung der Lösungen, Messung der Zeit. Beachten Sie, dass die Zahlenvariablen `aufgabe`, `a` und `b` für die FUnktion `input()` in Zeichenketten umgewandelt werden müssen.

Falls nicht alle fünf Aufgaben richtig gelöst werden, kann kein Eeintrag in die Highscore-Liste erfolgen.

Die Highscore-Liste wird Element für Element durchsucht. Wird ein Element gefunden, in dem eine größere als die neue Ergebniszeit eingtragen ist, so wird die neue Ergebniszeit mithilfe der Funktion `insert()` an dieser Stelle in die Highscore-Liste eingefügt.

Falls kein Eintrag durch Einfügen erfolgte, wird die neue Ergebniszeit mithilfe der Funktion `append()` ans Ende der Liste angehängt. Auf diese Weise sit dafür gesorgt, dass die Highscore-Lsite immer aufsteigend nach Ergebniszeit sortiert ist. Sie wird nach jeder Änderung angezeigt.

Es folgt das Hauptprogramm mit dem Hauptmenü:

```py
# Hauptprogramm

# Initialisierung Zufallsgenerator
random.seed()

# Highscore aus Datei in Liste lesen
hs_lesen()

# Endlosschleife
while True:
    # Hauptmenü, Auswahl
    try:
        menu = int(input("Bitte Eingeben 0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue
    
    # Aufruf einer Funktion oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs_anzeigen()
    elif menu == 2:
        spielen()
    else:
        print("Falsche Eingabe")

# Nach Beenden des Programms HS in Datei Schreiben
hs_schreiben()
```

Nach der Initialisierung des Zufallsgenerators wird die Highscore-Datei eingelesen. Es beginnt die Endlosschleife mit dem Hauptmenü. Der Benutzer kann 0, 1 oder 2 eingeben. Alle anderen Eingaben sind falsch.
* Nach der Eingabe von 1 wird die Highscore-Liste angezeigt, anschließend erscheint wieder das Hauptmenü.
* Nach der Eingabe von 2 beginnt das Spiel, anschließend erscheint wieder das Hauptmenü.
* Nach der Eingabe von 0 wird die Endlosschleife verlassen. Die Highscore-Liste wird in die Datei geschrieben. Das programm endet.

## 8.11 Spiel, objektorientierte Version mit Highscore-Datei

Es folgt eine weitere objektorientierte Version des Kopfrechenspiels. Diesmal werden die Daten des Spielers (name und Zeit) in einer CSV-Datei gespeichert. Diese CSV-Datei können sie sich mithilfe von MS Excel oder LibreOffice ansehen.

Neben den beiden Klassen `Spiel` und `Aufgabe` benötigen Sie die Klasse `Highscore`. Die KLasse `Aufgabe`hat sich gegenüber der Version in der Datei spiel_oop.py nicht verändert.

Zunächst die Importanweisung und das Hauptprogramm:

```py
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
```

Es werden die Module `random`, `time` und `glob` benötigt.

Falls der Benutzer die Highscore-Liste sehen möchte, wird ein Objekt der Klasse Highscore erzeugt und ausgegeben. Falls er spielen möchte, wird ein Objekt der Klasse Spiel erzeugt. Nach der Messung der Zeit und dem eigentlichen Spielvorgang werden die Ergebnisse ausgegeben.

Es folgt die Klasse Spiel:

```py
# Klasse "Spiel"
class Spiel:
    def __init__(self):
        #Start des Spiels
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie Ihren Namen ein (max. 10 Zeichen): ")
        self.spieler = s[0:10]

        if self.spieler == "anna":
            self.spieler = "best anna!"
        elif self.spieler == "Anna":
            self.spieler = "Best Anna!"
        
    
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
```

Im Konstruktor der KLasse wird der Zufallsgenerator initiert. Der Zähler für die richtig gelösten Aufgaben wird auf 0, die Anzahl der Aufgaben auf 5 gesetzt. Es wird der Name des Spielers ermittelt. Dabei werden drei Eigenscahften der Klasse `Spiel` gesetzt: `richtig`, `anzahl` und `spieler`.

In der Methode `spielen()` werden insgesamt fünf Aufgaben gestellt und beantwortet. Die Methode `messen()` dient zur Zeitmessung. Es wird die Eigenscahft `zeit` der Klasse `spiel` gesetzt.

Falls der Spieler alle Aufgaben ricthig löst, wird der Ausgabemethode ein Objekt der Klasse Highscore erzeugt und gespeichert. Anschließend wird die Liste ausgegeben.

Die neue Klasse `Highscore` sieht wie folgt aus:

```py

```