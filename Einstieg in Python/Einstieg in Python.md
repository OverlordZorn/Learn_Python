# Einstieg in Python

- [Einstieg in Python](#einstieg-in-python)
  - [1 Einführung](#1-einführung)
    - [1.1 Vorteile von Python](#11-vorteile-von-python)
    - [1.2 Verbreitung von Python](#12-verbreitung-von-python)
    - [1.3 Aufbauch des Buchs](#13-aufbauch-des-buchs)
  - [2 Erste Schritte](#2-erste-schritte)
    - [2.1 Python als Taschenrechner](#21-python-als-taschenrechner)
      - [EVA Prinzip](#eva-prinzip)
      - [Operatoren + - *](#operatoren----)
      - [Operatorenn / // %](#operatorenn---)
      - [Rangfolge und Klammern](#rangfolge-und-klammern)
      - [Variablen und Zuweisung](#variablen-und-zuweisung)
      - [Einige Hinweise](#einige-hinweise)
      - [Variablennamen](#variablennamen)
    - [2.2 Erstes Programm](#22-erstes-programm)
      - [2.2.1 Hallo Welt](#221-hallo-welt)
      - [2.2.2 Eingabe eines Programms](#222-eingabe-eines-programms)
      - [2.2.3 Speicher und Ausführen](#223-speicher-und-ausführen)
        - [Kommandozeile](#kommandozeile)
        - [In IDLE](#in-idle)
      - [2.3.4 Kommentare](#234-kommentare)
      - [2.3.5 Verkettung von Ausgaben](#235-verkettung-von-ausgaben)
      - [2.3.6 Lange Ausgaben](#236-lange-ausgaben)
  - [3 Programmierkurs](#3-programmierkurs)
    - [3.1 Ein Spiel programmieren](#31-ein-spiel-programmieren)
    - [3.2 Variablen und Operatoren](#32-variablen-und-operatoren)
      - [3.2.1 Berechnung und Zuweisung](#321-berechnung-und-zuweisung)
      - [3.2.2 Eingabe einer Zeichenkette](#322-eingabe-einer-zeichenkette)
      - [3.2.3 Eingabe einer Zahl](#323-eingabe-einer-zahl)
      - [3.2.5 Zufallszahlen](#325-zufallszahlen)
      - [3.2.6 Typhinweise](#326-typhinweise)
    - [3.3 Verzweigungen](#33-verzweigungen)
      - [3.3.1 Vergleichsoperatoren](#331-vergleichsoperatoren)
      - [3.3.2 Einfache Verzweigung](#332-einfache-verzweigung)
      - [3.3.3 Spiel - Version mit Bewertung der Eingabe](#333-spiel---version-mit-bewertung-der-eingabe)
      - [3.3.4 Mehrfache Verzweigung](#334-mehrfache-verzweigung)
      - [3.3.5 Logische Operatioren](#335-logische-operatioren)
      - [3.3.6 Mehrere Vergleichsoperatoren](#336-mehrere-vergleichsoperatoren)
      - [3.3.7 Spiel, Verson mit genauer Bewertung der Eingabe](#337-spiel-verson-mit-genauer-bewertung-der-eingabe)
      - [3.3.8 Rangfolge der Operatoren](#338-rangfolge-der-operatoren)
    - [3.4 Schleifen](#34-schleifen)
      - [3.4.1 for-Schleife](#341-for-schleife)
      - [3.4.2 Schleifenabbruck mit `break`](#342-schleifenabbruck-mit-break)
      - [3.4.3 Geschachtelte Kontrollstrukturen](#343-geschachtelte-kontrollstrukturen)
      - [3.4.4 Spiel, Version mit for-Schleife und Abbruch](#344-spiel-version-mit-for-schleife-und-abbruch)
      - [3.4.5 For schleife mit `range()`](#345-for-schleife-mit-range)
      - [3.4.6 Spiel, Version mit range()](#346-spiel-version-mit-range)
      - [3.4.7 while-Schleife](#347-while-schleife)
      - [3.4.8 Spiel, Version mit while-Schleife und Zähler](#348-spiel-version-mit-while-schleife-und-zähler)
      - [3.4.9 Kombinierte Zuweisungsausdrücke](#349-kombinierte-zuweisungsausdrücke)
    - [3.5 Entwicklung eines Programmes](#35-entwicklung-eines-programmes)
    - [3.6 Fehler und Ausnahmen](#36-fehler-und-ausnahmen)
      - [3.6.1 Basisprogramm](#361-basisprogramm)
      - [3.6.2 Fehler abfangen](#362-fehler-abfangen)
      - [3.6.3 Eingabe wiederholen](#363-eingabe-wiederholen)
      - [3.6.4 Exkurs: Schleifenfortsetzung mit `continue`](#364-exkurs-schleifenfortsetzung-mit-continue)
      - [3.6.5 Spiel, Version mit Ausnahmebedingung](#365-spiel-version-mit-ausnahmebedingung)
    - [3.7 Funktionen und Module](#37-funktionen-und-module)
      - [3.7.1 Einfache Funktionen](#371-einfache-funktionen)
      - [3.7.2 Funktionen mit einem Parameter](#372-funktionen-mit-einem-parameter)
      - [3.7.3 Funktionen mit mehreren Parametern](#373-funktionen-mit-mehreren-parametern)
      - [3.7.4 Funktionen mit Rückgabewert](#374-funktionen-mit-rückgabewert)
      - [3.7.5 Spiel, Version mit Funktionen](#375-spiel-version-mit-funktionen)
    - [3.8 Das fertige Spiel](#38-das-fertige-spiel)
  - [4 Datentypen](#4-datentypen)
    - [4.1 Zahlen](#41-zahlen)
      - [4.1.1 Ganze Zahlen](#411-ganze-zahlen)
      - [4.1.2 Zahlen mit Nachkommastellen](#412-zahlen-mit-nachkommastellen)
      - [4.1.3 Typ ermitteln](#413-typ-ermitteln)
      - [4.1.4 Operator **](#414-operator-)
      - [4.1.5 Rundung und Konvertierung](#415-rundung-und-konvertierung)
      - [4.1.6 Winkelfunktionen](#416-winkelfunktionen)
      - [4.1.7 Weitere mathematische Funktionen](#417-weitere-mathematische-funktionen)
      - [4.18 Bitoperatoren](#418-bitoperatoren)
      - [4.1.9 Brüche](#419-brüche)


## 1 Einführung

### 1.1 Vorteile von Python
Python ist eine sehr einfach zu erlernende Programmiersprache und für den Einstieh in die Welt der Programmierung ideal geeignet. Trotz ihrer Einfachheit bietet diese Sprache auch die Möglichkeit, komplexe Programme für vielfältige Anwendungsgebiete zu schreiben.

Python eignet sich besoders zur schnellen Entwicklung umfangreicher Anwendungen. Diese TEchnik ist unter dem Stichwort RAD ( Rapid Application Development) bekannt geworden. Python vereint zu diesem Zweick folgende Vorteile:
* Eine einfache, eindeutige Syntax: Python ist für Einsteiger eine ideale Programmiersprache. Sie beschränkt sich auf einfache, klare Anweisungen und häufig auf einen einzigen möglichen Lösungsweg. Dieser prägt sich schnell ein und wird dem Entwickler vertraut.
* Klare Strukturen: Python verlangt vom Entwickler, in einer gut lesbaren sStruktur zu schreiben. Die Anordnung der Programmzeilen ergibt zugleich dielogische STruktur des Programms.
* Wiederverwendung von Code: Die Modularisierung, also die Zerlegung eines Problems in Teilprobleme und die anschließende Zusammenführung der Teillösungen zu einer Gesamtlösung, wird in Python sehr leicht gemacht. Die vorhandenen Teillösungen können unkompliziert für weitere Aufgabenstellungen genutzt werden, sodass Sie als Entwickler bald über einen umfangreichen Pool an Modulen verfügen.
* Objektbearbeitung: In Python werden alle Daten als Objekte gespeichert. Dies führt zu einer einheitlichen Behandlung für Objekte unterschiedlichen Typs. Andererseits erfolg die physikalische Speicherung der Objekte von Python automatisch, also ohne Eingriff des Entwicklers. Der Entwickler muss sich nicht um die Reservierung und Freigabe geeigneter Speicherbereiche kümmern.
* Interpreter/Compiler: Python-Programme werden unmittelbar interpretiert. Sie müssen nicht erst kompiliert und gebunden werden. Dies ermöglicht einen häufigen, schnellen Wchsel zwischen Codierungs- und Testpahse.
* Unabhängigkeit vom Betriebssystem: Sowohl Programme, die von der Kommandozeile aus biedient werden, als auch Programme mit grafischen Benutzeroberflächen können auf unterschiedlichen Betriebssystemen (Windows, Linux, macOs) ohne Neuentwicklung und Anpassung eingesetzt werden.

### 1.2 Verbreitung von Python
Aufgrund seiner vielen Vorzüge gehört Python zu den beliebtesten Programmiersprachen überhaupt. So wird es z. B. innerhalb des Projekts 100-Dollar-Laptop, das der Schulausbikldung von Kindern in aller Welt dient, für die Benutzeroverfläche verwendet. Aber auch in zahlreichen großen Unternehmen wird Python eingesetzt, hier ein paar Beispiele.:
* Google: Python ist eine der drei offiziellen Programmiersprachen
* youTube: Wurde zum großen Teil mithilfe von Python entwickelt.
* NASA: Nutzt Python zur Softwareentwicklung im Zusammenhang mit den Spache-Shuttle-Missionen.
* Industrial Light&Magic: Auch HOllywood setzt auf Python - die Produktionsfirma ILM nutzt es z.B. bei der Entwicklung von Spezialeffekten.
* Honeywell: Python wird weltweit in vielen Firmen zur allgemeinen Hardware- und Softwareentwicklung eingesetzt.

### 1.3 Aufbauch des Buchs
Das vorliegende Buch führt Sie in die Programmiersprache Python ein. Besonderer Wert wird darauf gelegt, dass Sie selbst praktisch mit Python aribeten. Daher empfehle ich Ihnen, von Anfang an dem logischen Faden von Erklärungen und Beispielen zu folgen.

Python 3 wurde im Jahr 2008 eingeführt und ist mit der Version 3.8 die aktuelle Version für Einsteiger. Python 2, die klassische Versiuon, existiert noch in großen, langlebigen Projekten und wird auch weiterhin von den Python-Entwickerln unterstützt. Daher gehe ich in einem eigenen Kaptiel auf die Unterschiede zwischen 2 und 3 ein.

Erste Zusammenhänge werden in Kapitel 2 anhand von einfachen Berechnungen vermittelt. Außerdem lernen Sie, ein Programm einzugeben, zu speicher und es unter den verschiedenen Umgebungen auszuführen.

Sie werden die Sprache spielersich kennen lernen. Dhaer begleitet Sie ein selbst programmiertes Spiel durch das Buch. In dem Spiel soll der Benutzer eine oder mehrere Kopfrechenaufgaben lösen. Es wird mit dem "Pgrogrammierkurs" in Kapitel 3 eingeführt und im weitern Verlauf des Buchs kontinuerlich erweitert und verbessert.

Nach der Vorstellung der verschiedenen Datentypen mit ihren jeweiligen Eigenschaften und Vorteilen in Kapitel 4 werden die Programmierkenntnisse in Kapitel 5 vertieft.

Kapitel 6 widmet sich der objektorientierten Programmierung mit Python.

Einige nützliche Module zur Ergänzung der Programme werden in Kapitel 7 vorgestellt.

In Kapitel 8 und 10 lernen Sie, Daten dauerhaft in Dateien oder Datenbanken zu speichern. Python wird zudem in der Internetprogrammierung eingesetzt. Die Zusammenhänge zwischen Python und dem internet vermittelt Kapitel 9.

Sowohl Windows als auch Ubuntu Linux und macOS bieten komfortable grafische Benutzeroberflächen (GUI). Kapitel 11 beschäftigt sich mit der GUI Erzeugung mithilfe des Moduls tkinter. Dieses stellt eine Schnittstelle zwischen dem grafischen Tooklit Kk und Python dar.

Kapitel 12 fasst diejenigen Unterschiede zwischen Python 2 und Python 3, die besonders für Einsteiger interessant sind, noch einmal zusammen.

Python ist die primäre Sprache für die Programmierung von elektronischen Schaltungen mithilfe des Einplatinencomputers RasPi. In Kaptiel 13 werden wir uns damit beschäftigen.

## 2 Erste Schritte
### 2.1 Python als Taschenrechner
#### EVA Prinzip
Eingabe, Verarbeitung, Ausgabe.

#### Operatoren + - *

```
>>> 41 + 7.5
48.5

>>> 12 - 18
-6 

>>> 7 * 3
21
```

#### Operatorenn / // % 

```
>>> 22 / 8
2.75

>>> 22 // 8
2

>>> 22 % 8
6
```

#### Rangfolge und Klammern

```
>>> 7 + 2 * 3
13

>>> (7 + 2) * 3
27
```

#### Variablen und Zuweisung
```
>>> mi = 1.609344
>>> 2 * mi
3.218688
>>> 5 * mi
8.04672
>>> 22.5 * mi
36.21024
>>> 2.35 * mi
3.7819584000000006
```

#### Einige Hinweise

In Python-Variablen können sie ganze Zahlen, Zahlen mit Nachkommastellen, Zeichenketten (also Texte) und andere Objekte eines Programms mithilfe von Zuweisungen speichern.

Das Ergebnis der letzten Berechnung ist mathematisch falsch. 2,35 Meilen entsprechen 3,7819583 Kilometern, also ohne eine weiter 6 an der 16. Nachkommastelle. Woher kommt die falsche Anzeige?

Zahlen mit Nachkommastellen können im Gegensatz zu ganzen Zahlen nicht mathematisch exakt gespeichert werden. Es gibt einige Stellen im Buch, an denen dies auffallen wird. Bei den meisten Bereichnungen ist allerdings die Abweichung so gering, dass sie in der Praxis zu nvernachlässigen ist.

Es ist überlich, den Wert in Kilometer so auszugeben, dass dass auf drei Stellen hinter dem Komma gerunden wird, also auf den Meter genau. Auf eine solche formatierte Ausgabe gehen wir später noch ein.

#### Variablennamen
Den Namen einer Variablen können Sie unter Einhaltung der folgenden Regeln weitgehend frei wählen:
* Er kann aus den Buchstaben a-z, A-Z, 0-9 oder _ bestehen.
* Er darf nicht mit einer Ziffer beginnen.
* Er darf keinem der reservierten Wörter der Programmiersprache Python entsprechen. Das sind: `and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, rpint, raise, return, try, while, with, yield.
* Bachten Sie die Groß- und KLeinschreibung: Namen und Anweisungen müssen genau wie vorgegeben geschrieben werden. Die Namen `mi` und `Mi` bezeichnen verschiedene variablen.


### 2.2 Erstes Programm

Ein erstes Python-Programm wird eingegeben, abgespeichert und aufgerufen. Dieser Vorgang wird ausführlich erklärt. Die einzelnen Schritte sind später bei jedem Python-Programm auszuführen.


#### 2.2.1 Hallo Welt


#### 2.2.2 Eingabe eines Programms

Zur Eingabe des Programms rufen Sie in der Entwicklungsumgebung IDLE im Menü File zunächst den Menübefehl New File auf. Es öffnet sich ein neues Fenster mit dem Titel Untitled. ADas Hauptfenster rückt in den Hintergrund.



```py
print("Hallo Welt")
```

#### 2.2.3 Speicher und Ausführen

##### Kommandozeile
```
cd \Python38\Beispiele
python hallo.py
```

##### In IDLE
Run > Run Module (F5)

#### 2.3.4 Kommentare

```
# Mein erstes Programm
print("Hallo Welt")     # Eine Ausgabe
"""Kommentar in
    mehreren Zeilen"""
```
Ausgabe:
```
================================= RESTART: C:\Python38-32\Beispiele\hallo.py ================================
Hallo Welt
>>> 
```


#### 2.3.5 Verkettung von Ausgaben
Mithilfe der Funktion print() können auch mehrere Ausgaben in einer Zeile vorgenommen werden. Das Programm wird weiter verändert:

```
# Mein erstes Programm
print("Hallo", "Welt")
```
Ausgabe:
```
================================= RESTART: C:\Python38-32\Beispiele\hallo.py ================================
Hallo Welt
>>> 
```

Die einzelnen TEile der Ausgabe werden durch KOmmata voneinander getrennt. Nach jedem Teil der Ausgabe wird automatisch ein Leerzeichen eingesetzt. Dieses Verhalten können sie als Programmierer beeinflussen; mehr dazu im Abschnitt 5.2.1 über die Funktion print().

#### 2.3.6 Lange Ausgaben
Zeichenketten, die mithilfe der Funktion print() ausgegeben werden, können sehr lang werden, eventuell sogar über den rechten Rand innerhalb des Editors hinausgehen. Damit wird der Programmcode allerdings etwas unübersichtlich. Sie können solche Zeichenketten aber auch auf mehrere Zeilen verteilen - dieses Vorgehen wird auch im vorliegenden Buch aufgrund der begrenzten Druckbreite häufig angewerndet.

Wenngleich es für dieses kurze Programm eigentlich nicht notwendig ist, verteilen wir hier zur verdeutlichung den Code auf mehrere Zeilen:

```
# Mein erstes Programm
print("Hallo",
      "Welt")
print("Hallo "
      "Welt")
```

```================================= RESTART: C:\Python38-32\Beispiele\hallo.py ================================
Hallo Welt
Hallo Welt
```

Es bietet sich an, den Zeilenumbruch nach einem Komma durchzuführen, wie bei der ersten Ausgabe von `Hallo Welt`. Teiltexte müssen nicht durch Kommata voneinander getrennt werden. Sie sind allerdings jeweils mit Anführungsstrichen zu bregrenzen. Das trennende Leerzeichen zwischen "Hallo" und "Welt" müssen Sie nun von Hand setzen.

```
print("Hallo"
      "Welt")
```
Ausgabe:
```
HalloWelt
```

## 3 Programmierkurs

Der folgende Programmierkurs mit ausführlichen Erläuterungen führt Sie schrittweise in die Programmierung mit Python ein. Begleitet wird der Kursa von einem Programmierprojekt, das die vielen Teilaspekte zu einem Ganzen verknüpft.

### 3.1 Ein Spiel programmieren

Damit Sie die Programmiersprache Python auf unterhaltsame Weise kennenlernen, werden Sie im Folgenden ein Spiel programmieren. Es wird im Verlauf des Buchs kontinuierlich erweitert und verbessert. Zunächst wird der Ablauf des Spiels beschrieben.
Nach Aufruf des Programms wird dem Benutzer eine Kopfrechenaufgabe gestellt. Er gibt das von ihm ermittelte Ergebnis ein, und das Programm bewertet seine Eingabe.

Die Aufgabe: 9 + 26
Bitte eine Zahl eingeben: 
34
34 ist falsch
Bitte eine Zahl eingeben:
35
35 ist richtig
Ergebnis: 35
Anzahl Versuche: 2

Das Spiel wird in mehreren Einzelschritten erstellt. Zunächst entsteht eine ganz einfache Version. Mit zunehmenenden Programmierkenntnissen entwickeln Sie immer komplexere Versionen. Die im jeweiligen Abschnitt erlernten Programmierfähigkeiten setzen Sie unmittelbar zur Verbesserung des Spielablaufs ein.

In späteren Abschnitten des Buchs entstehen weitere Versionenen des Spiels.

Es begleitet Sie auf diese Weise durch das gesamte Buch. Unter anderem wird es um die folgende Möglichkeiten erweitert:
* Es werden mehrere Aufgaben gestellt.
* Die benötigte Zeit wird gemessen.
* Der Name des Spielersa und die benötigte Zeit werden als Highscore-Liste dauerhaft in einer Datei oder einer Datenbank gespeichert.
* Die Highscore-Liste wird mit neuen Ergebnissen aktualisiert und auf dem Bildschirm dargestellt.
* Es gibt eine Version auf einer grafischen Benutzeroberfläche.
* Es gibt eine Version, die das Spielen im Internet ermöglicht.

### 3.2 Variablen und Operatoren

Zur Speicherung von Werten werden Variablen benötigt. Operatoren dienen zur Ausführung von Berechnungen.

#### 3.2.1 Berechnung und Zuweisung
Im folgenden Programm wird eine einfache Berechnung mithilfe eines Operators durchgeführt. Das Ergebnis der Berechnung wird mit dem Gleichheitszeichen einer Variablen zugewiesen. Es erfolgt eine Ausgabe. Diese Schritte kennen Sie bereits aus Abschnitt 2.1.5.

```
# Werte 
a = 5
b = 3

# Berechnung
C = a + b

# Ausgabe
print("Die Aufgabe:", a, "+", b)
print("Das Ergebnis:", c)
```

In den beidne Variablen wird jeweils ein Wert gespeichert. Die beiden Werte werden addiert, das Ergebnis wird der Variablen c zugewiesen. Die Aufgabenstellung wird ausgegeben, anschließend das Ergebnis.

#### 3.2.2 Eingabe einer Zeichenkette
IUn diesem Abschnitt wird die Funktion input() zur Eingabe einer Zeichenkette durch den Benutzer eingeführt. Ein kleines Beispiel:

```
# Eingabe einer Zeichenkette
print("Bitte einen text eingeben")
x = input()
print("Ihre Eingabe:", x)
```

#### 3.2.3 Eingabe einer Zahl

Im weiteren Verlauf des Spiels ist es notzwendig, die Eingabe des Benutzers als Zahl weiterzuverwenden. Dazu muss die Zeichenkette, die die Funktion input() liefert, in eine Zahl umgewandelt werden.

Zur Umwandlung gbit es unter anderem die folgenden Funktionen:
* Die eingebaute Funktion int() wandelt eine Zeichenkette in eine ganze Zahl um; eventuell vorhandene Nachkommastellen werden abgeschnitten.
* Die eingebaute Funktion float() wandelt eine Zeichenkette in eine Zahl mit Nachkommastellen um.
* Falls die Zeichenkette für float() keine gültige Zahl enthält, kommt es zu einem Programmabbruch. Bei int() muss es sich sogar um eine gültige Zahl handeln. In Abschnitt 3.6 lernen Sie, wie Sie Programmabbrüche abfangen.
  
#### 3.2.5 Zufallszahlen

Natürlich wird nicht immer die gleiche Kopfrechenaufgabe gerstellt. In Python steht ein Zufallszahlengenerator zur Verfügung. Er erzeugt zufällige Zahlen, die wir zur Bildung der Aufgabenstellung nutzen.

Die funktionen des Zufallszahlengenerators befinden sich in einem zusätzlichen Modul, dass zunächst importiert werden muss. Das Programm wird wie folgt verändert:

```
# Modul random inportieren
inport random

# Zufallsgenerator initialisieren
random.seed()

# Zufallswerte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
```

Zusätzliche Module können Sie mitheilfe der Anweisung `inport` in das Programm einbinden. Die Funktionen dieser Module können Sie anschließend in der Schreibweise `Modulname.Funktionsname` aufrufen.

Der Aufruf der Funktion `seed()` des Moduls `random` führt dazu, dass der Zufallszahlengenerator mit der aktuellen Systemzeit initialisiert wird. Anderenfalls könnte es passieren, dass anstelle einer zufälligen Auswahl immer wieder die gleichen Zahlen geliefert würden.

Die Funktion `randint()` des Moduls `random` liefert eine ganze Zufallszahl im angegebenen Bereich. Im vorliegenden Fall ist dies also eine zufällige Zahl von 1 bis 10.

Die Funktionen des Moduls `raondom`können für die zufälligen Werte eines Spiels genutzt werden. Falls Sie zufällige Werte zum Zwecke der Verschlüsselung oder aus Gründen der Sicherheit benötigen, sollten sie die Funktionen des Moduls `secrets`nutzen, das es seit Python 3.6 gibt.

#### 3.2.6 Typhinweise

Seit Python 3.6 können Sie angeben, welchen Datentyp eine Variable haben soll. Allerdings haben diese Typhinweise (english: type hints), auch Annotationen genannt, bisher nur provisorischen Charakter. Ihre Regeln können sich noch ändern und sind nicht binded.

Type Hints sollen u. A. die Lesbarkeit des Codes für Entwickler verbessern und bessere Hilfestellungen der Editoren innerhalb einer Entwicklungsumgebung ermöglichen. Allerdings gilt nach wie vor eine Grundregel der Entwickler von Python:
"Python wird eine dynamsich typisierte Sprache bleiben".

### 3.3 Verzweigungen

In den bisherigen Programmen werden alle Anweisungen der Reihe nach ausgeführt. Zur Steuerung des Programmablaufs werden alelrdings häufig Verzweigungen benötigt. Innerhalb des Programms wird anhand einer Bedinging entschieden, welcher Zweig des Programms ausgeführt wird.

#### 3.3.1 Vergleichsoperatoren
Bedingungen werden mitheilfe von Vergleichsoperatoren formuliert. Tabelle 3.1 listet die Vergleichsoperatoren mit ihrer Bedeutung auf.

| Operator | Bedeutung |
|---|---|
|>| größer als |
|<| kleiner als |
|>=|größer als oder gleich |
|<=|kleiner als oder gleich |
|==| gleich |
|!=| ungleich |

#### 3.3.2 Einfache Verzweigung
Im folgenden Beispiel wird untersucht, ob eine Zahl positiv ist. Ist dies der fall, wird `Diese Zahl ist positiv` ausgegeben, anderenfalls lautet die Ausgabe `Diese Zahl ist 0 oder negativ`. Es wird also nnur eine der beiden Anweisungen ausgeführt.

```
x = 12
print ("x:", x)

if x > 0:
    print("Diese Zahl ist positiv")
else:
    print("Diese Zahl ist 0 oder Negativ")
```

In der ersten Zeile erhält die Variable x den Wert 12.

In der vierten Zeile wird mitheilfe von *if* eine Verzweigung eingeleitet. Danach wird eine Bedingung formuliert, hier `x > 0`, die entweder wahr oder falsch ergibt. Anschließend kommt ein Doppelpunkt.

Es folgen eine oder mehrere Anweisungen, die nur ausgeführt werden, falls die Bedingung wahr iergibt. Die anweisungen müssen innerhalb des sogenannten if-Zweigs mithilfe der Tab Taste eingerückt werden, damit Python die Zugehörigkeit zur Verzweigung erkennen kann. Gleichzeitig macht die Einrückung das Programm übersichtlicher.

In der sechsten Zeile wird mithilfe der Anweisung `else` der alternative Teil der Verzweigung eingeleitet. Es folgt wiederum ein Doppelpunkt.

Dann folgen eine oder mehrere Anweisungen, die nur ausgeführt werden, falls die Bedingung `falsh`ergibt. Auch diese Anweisungen müssen eingerückt werden.

#### 3.3.3 Spiel - Version mit Bewertung der Eingabe

#### 3.3.4 Mehrfache Verzweigung

In vielen Anwendungsfällen gibt es mehr als zwei Möglichkeiten, zwischen denen zu entscheiden ist. Dazu wird eine mehrfache Verzweigung benötigt. Im folgenden Beispiel wird utnersucht, ob eine Zahl positiv, negativ oder gleich 0 ist. Es wird eine entsprechende Meldung ausgegeben:

```
x = -5
print("x:", x)

if x > 0:
    print("x ist positiv")
elif x < 0:
    print("x ist negativ")
else:
    print("x ist gleich null")
```

Die Verzweigung wird mithilfe von `if` eingeleitet. Falls x positiv ist, werden die nachfolgenden eingerückten Anweisungen ausgeführt.

Nach `elif` wird eine weitereBedingung formuliert. Sie wird nur untersucht, falls die erste Bedingung nach dem if nicht zutrifft. Falls x negativ ist, werden die nachfolgenden, eingerückten Anweisungen ausgeführt.

Die Anweisungen ach dem else werden nur durchgeführt, falls keine der beiden vorherigen Bedingungen zutraf ( nach dem if und nach dem elif).
In diesem Fall beduetet das, dass x gleich 0 ist, da es nicht positiv und nicht negativ ist.

**Hinweis**
Innerhalb einer Verzweigung können mehrere elif-Anweisungen vorkommen. Sie werden der Reihe nach untersucht, bis das Programm zu einer Bedingung kommt, die zutrifft. Die weiteren elif-Anweisungen oder eine else-Anweisung werden in diesem Fall nicht mehr bachtet.

#### 3.3.5 Logische Operatioren
Mithilfe der logsichen operatoren `and`, `or` und `not` können mehrere Bedingungen miteinander verknüpft werden.
* Eine Bedingung die aus einer oder mehreren Einzelbedingungen besteht, die jweils mit dem Operator `and` verkünft sind, ergibt wahr, wenn jede der Einzelbedingugnen wahr ergibt.
* Eine Bedingung die aus einer oder mehreren Einzelbedingugnen besteht, die mit dem Operator `or` verkünpft sind, ergibt wahr, wenn mindestens eine der Einzelbedingungen wahr ergibt.
* Der Operator `not` kehr den Wahrheitswert einer Bedingung um, d.h., eine falsche Bedingung wird wahr, eine wahre Bedingung wird falsch.


#### 3.3.6 Mehrere Vergleichsoperatoren
Bedingungen können auch mehrere Vergleichsoperatoren enthalten. Manche Verzweigungen sind auf diese Weise verständlicher. Ein Beispiel:

```
x = 12
y = 15
z = 20
print("x:", x)
print("y:", y)
print("z:", z)

# Bedingung 1
if x < y < z:
    print("y liegt zwischen x und z")

```
Die Bedingung `x < y <` entspricht dem Ausdruck `x < y and y < z`. In der Kurzform ist sie allerdings besser lesbar.

#### 3.3.7 Spiel, Verson mit genauer Bewertung der Eingabe

 Nun kann die Eingabe des Benutzers in dem Kopfrechenspiel auf verschiedene Art und Weise genauer bewertet werden:
 * Mithilfe einer mehrfachen Verzweigung
 * Anhand logischer OPeratoren
 * Anhand von Bedingungen mit mehreren Vergleichsoperatoren

insgesamt werden vier Möglichkeiten angeboten: über `if`, zweimal `elif` und `else`. Ist die Eingabe kleiner oder größer als 100, so ist sie ganz falsch. Dies wird mithielfe des logsichen Operators `or` gelöst.

Unterscheidet sich die eingegebene Zahl vom richtigen Ergebnis nur um den Wert 1, ist die Eingabe ganz nahe dran. Dies wird mit einer Bedingung ermittelt, die mehrere Vergleichsoperatoren enthält.

#### 3.3.8 Rangfolge der Operatoren
In vielen Ausdrücken treten mehrere Operatoren auf. Bisher sind dies Rechenoperatoren, Vergleichsoperatoren und logsiche Operatoren.

Die einzelnenn Teilschritte folgen der sogenannten Rangfolge der Operatoren. Die Teilschritte, bei denen höherrangige Operatoren beteiligt sind, werden zuerst ausgeführt.

Die nachfolgende Tabelle gibt die Rangfolge der bisher verwendeten Operatoren in Python an, beginnend mit den Operatoren

|Operator|Bedeutung |
|---|---|
| + - | positives vorzeichen einer Zahl, negatives Vorzeichen einer Zahl |
| * / % // | Multiplikation, Division, Modulo, Ganzzahldivision |
| + - | Addition, Subtraktion |
| < <= >= > == != | kleiner, kleiner gleich, größer, größergleich, gleich, ungleich |
| not | logische Verneinung|
| and | logisches Und |
| or | logisches Oder |

### 3.4 Schleifen

Neben der Verzweigung gibt es eine weiter wichtige Struktur zur Steuerung von Programmen: die Schleife. Mithilfe einer Schleife ermöglichen Sie die wiederholte Ausführung eines Programmschritts.

Es muss zwischen zwei Typen von Schleifen unterschieden werden:
der `for`-Schleife und der `while`-Schleife. Der jeweilige Anweindungsbereich der beiden Typen wird durch folgende Merkmale definiert:
* Eine `for`-Schleife wird verwendet, wenn ein Programmschritt für eine regelmäßige, zum Zeitpunkt der Anwendung bekannte Folge von Werten wiederholt ausgeführt werden soll.
* Eine `while`-Schleife wird verwendet, wenn sich erst durch Eingaben des Anwenders ergibt, ob ein Programmschritt ausgeführt werden soll und wie oft er wiederholt wird.

Eine `for`-Schleife wird auch als Zählschleife beziechnet, eine `while`-Schleife als bedingungsgesteuerte Schleife.

#### 3.4.1 for-Schleife

Die Anwendung der `for`-Schleife verdeutlicht das folgende Beispiel:

```py
for i in 2, 7.5, -22:
    print("Zahl:", i, ", Quadrat:", i*i)
```
Folgende Ausgabe wird erzeugt:

```
Zahl: 2, Quadrat: 4
Zahl: 7.5, Quadrat: 56.25
Zahl: -22, Quadrat: 484
```

Die erste Zeile ist wie folgt zu lesen: Führe die nachfolgenden eingerückten Anweisungen für jede Zahl in der Abfolge 2, 7.5 und -22 aus. Nenne diese Zahl in diesen Anweisungen i. Nach der Zahlenfolge muss, ebenso wie bei if-else, ein Doppelpunkt notiert werden. Anstelle von i können Sie auch eine andere Variable als Schleifenvariable nutzen. Die Zahlen werden zusammen mit einem kurzen INformationstext ausgegeben bzw. quadriert und ausgegeben.

**Hinweis**
Eine solche Abfolge von Objekten, die z. B. in einer For schleife udrchlaufen werden kann, nennt man auch iterierbares Objekt oder kurz iterable.
Diese Iterables werden uns in Python noch häufiger begegnen. Den Vorgang des Durchlaufens nennt man auch iterieren.



#### 3.4.2 Schleifenabbruck mit `break`

Die Anweisung `break` beitet eine weitere Möglichkeit zur Steuerung von Schleifen. Sie führt zu einem unmittelbaren Abbruch einer Schleife. Sie wird sinnvollerweise mit einer Bedingung verbunden und häufig bei Sonderfällen eingesetzt.
Ein Beispiel:

```py
for i in 12, - 4, 20, 7:
    if i*i > 200:
        break
    print("Zahl:", i,",Quadrat:", i*i)
print("Ende")
```

Diese Ausgabe wird erzeugt:
```
Zahl: 12, Quadrat: 144
Zahl: -4, Quadrat: 16
Ende
``` 

Die Schleifewird unmittelbar verlassen, wenn das Quadrat der aktuellen Zahl größer als 200 ist. Die Ausgabe innerhalb der Schleife erfolgt auch nicht mehr. Das Programm wird nach dier Schleife fortgesetzt.


#### 3.4.3 Geschachtelte Kontrollstrukturen

Wie das vorherige Programm verdeutlicht, können Kontrollstrukturen (also Verzweigungen und Schleifen) auch geschachtelt werden. Dies bedeutet, dass eine Kontrollstruktur eine weitere Kontrollstruktur enthält. Diese kann ihrerseits wiederrum eine Kontrollstruktur enthalten usw. Ein weiteres Beispiel:

```py
for x in -2, -1, 0, 1, 2:
    if x > 0:
        print (x, "positiv")
    else:
        if x < 0:
            print(x, "negativ")
        else:
            print(x, "gleich 0")
```

Es wird folgende Ausgabe erzeugt:
```
-2 negativ
-1 negativ
0 gleich 0
1 positiv
2 positiv
```

Zur Erläuterung:
* Die äuterste Kontrollstruktur ist eine `for`-Schleife. Alle einfach eingerückten Anweisungen werden - gemäß der Schleifensteuerung - mehrmals ausgeführt.
* Mit der äußeren if-Anweisung wird die erste Verzweigung eingeleitet.
* Ist x größer als 0, wird die folgende zweifache eingerückte Anweisung ausgeführt. Ist x nicht größer als 0, wird die innere if-Anweisung hitner der äußeren else-Anweisung untersucht.
* Trifft die Bedingung der inneren if-Anweisung zu, werden die folgenden dreifach eingerückten Anweisungen ausgeführt, die der inneren else-Anweisung folgen.
  
Zu beachten sind besonders die mehrfachen Einrückungen, damit die Tiefe der Kontrollstruktur von Python richtig erkannt werden kann.

Nach einem Doppelpunkt hinter dem Kopf einer Kontrollstruktur wird in der Entwicklungsumgebung IDLE automatisch mit einem Tabulatorspring eingerückt. Dieser Sprung erzeugt standardmäßig vier Leerzeichen, dadurch werden die Kontorllstrukturen für den Entwickler klar erkennbar.

Falls Sie mit einem anderen Editor arbeiten, müssen sie daruaf achten, dass um mindestens ein Leerzeichen eingerückt wird, damit Pythonm die Kontrollstruktur erkennt. Sinnvoller ist eine Einrückung um zwei oder mehr Leerzeichen, damit die Struktur auch für den Entwickler gut erkennbar ist.

#### 3.4.4 Spiel, Version mit for-Schleife und Abbruch

Die for-Schleife wird nun dazu gentuzt, die Eingabe und die Bewertung es Kopfrechenspiels insgesamt viermal zu durchlaufen. Der Benutzer hat somit vier Versuche, das richtige Ergebnis zu ermitteln. Die Anweisung break dient zum Abbruch der Schleife, sobald der Benutzer das richtige Ergebnis eingegeben hat.

Die Aufgabe wird einmal ermittelt und gestellt. Der Benutzer wird maximal viermal dazu aufgefordert, ein Ergebnis einzugeben. Jede seiner Eingaben wird bewertet. Ist bereits einer der ersten drei Versuche richtig, wird die Schleife vorzeitig abgebrochen.

#### 3.4.5 For schleife mit `range()`

Mist werden Schleifen für regelmäßige Abfolgen von Zahlen genutzt. Dabei erweist sich der Einsatz der Funktion range() als sehr nützlich. Ein Beispiel:

```py
for i in range(3,11,2):
    print("Zahl:" i, "Quardrat:" i*i)
```
Es wird ausgegeben:
```
Zahl: 3 Quadrat: 9
Zahl: 5 Quadrat: 25
Zahl: 7 Quadrat: 49
Zahl: 9 Quadrat: 81
```

Der englische Begriff `range` bedeutet `Bereich`. Innerhalb der Kalmmern hinter `range` können bis zu drei Ganze Zahlen, durch kommata getrennt eingetragen werden:
*  Die erste ganze Zahl gibt den Beginn des  Bereichs an, für den die folgenden Anweisungen ausgeführt werden.
*  Die zweite ganze Zahl kennzeichnet das Ende des Bereichs. Es ist die erste Zahl, für die die Anweisungen **nicht mehr** ausgeführt werden.
*  Die dritte ganze Zahl gibt die Schrittweite für die Schleife an. Die Zahlen, für die die Anweisugnen ausgeführt werden, stehen zueinander also jeweils im Abstand von +2.

Der Aufruf der funktion range() mit den Zahlen, 3 11 und 2 ergibt somit die Abfolge: 3, 5, 7, 9.

Wir die Funktion Range() nur mit zwei Zahlen aufgerufen, so wird eine Schrittweite von 1 angenommen.

Wird die Funktion range() sogar nur mit einer Zahl aufgerufen, so wird diese Zahl einfach als die obere Grenze angesehen. Als untere Grenze gilt 0.
Außerdem wird wiederrum eine Schrittweite von 1 angenommen.

range(3) => 0 1 2

**Hinweis**
Bei der Funktion `range()` können eine oder mehrere der drei Zahlen auch negativ sein. Achten Sie auf sinnvolle Zahlenkombinationen. Die Angabe range(3,-11, 2) ist nicht sinnvoll, 
da man von der Zahl +3 in Schritten von +2 nicht zur Zahl -11 gelangt. Python fängt solche Schleifen ab und lässt sie nicht ausführen. Dasselbe gilt für die Zahlenkonbination range (3, 11, -2).


Für den regelmäßigen Ablauf von Zahlen mit Nachkommastellen muss die Schleifenvariable passend umgerechnet werden. Ein Beispiel:

```py
# 1. Version
for x in range(18,22):
    print(x/10)
print()

# 2. Version
x = 1.8
for i in range(4):
    print(x)
    x = x + 0.1
```
Die Ausgabe lautet:

```
1.8
1.9
2.0
2.1

1.8
1.90000000000001
2.0
2.1
```

Es werden jeweils die Zahlen von 1,8 bis 2,1 in Schritten von o,1 erzeugt.
* In der ersten Version werden die ganzen Zahlen von 18 bis 21 erzeugt und anschließend durch 10 geteilt.
* In der zweiten Version wird mit dem ersten Wert begonnen und innerhalb der Schleife jeweils um 0,1 erhöht. Dabei müssen Sie vorher errechnen, wie häufig die Schleife durchlaufen werden muss.
  

#### 3.4.6 Spiel, Version mit range()
Im Kopfrechenspiel wird die Schleife zur Wiederholung der Eingabe nun mithilfe von range() gebildet. Gleichzeitig haben Sie damit einen Zähler, der die laufende Nummer des Versuchs enthält. 
Sie können ihn verwenden, um dem Benutzer die Anzahl der Versuche mitzuteilen.

Der Benutzer hat maximal neun Versuche: range(1,10). Die Variable versch dient als ZÄhler für die Versuche. 
Nach Eingabe der richtigen Lösung (oder nach vollständigem Durchlauf der Schleife) wird dem Benutzer die Anzahl der Versuche mitgeteilt.

#### 3.4.7 while-Schleife
Die `while`-Schleife dient zur Steuerung einer Wiederholung mithilfe einer Bedingung. Im folgenden Programm werden zufällige Zahlen addiert und ausgegeben. 
Solange die Summe der Zahlen kleiner als 30 ist, wird der Vorgang wiederholt. Ist die Summe gleich oder größer als 30, wird das Programm beendet.

```py
#Zufallsgenerator
import random
random.seed()

# Initialisierung
summe = 0

# while-Schleife
while summe < 30:
    zzahl = random.randint(1,8)
    summe = summe + zzahl
    print("Zahl:", zzahl, "Zwischensumme:", summe)

print("Endergebnis:", summe)
```

Zunächst wird die Variable für die Summe der Zahlen auf 0 gesetzt.

Die While eAnweisung leitet die Schleife ein. Die wörtliche Übersetzung der Zeile lautet:
solange die SUmme kleiner als 30 ist. Dies bezieht sich auf die nachfolgenden eingerückten Anweisungen

Nach dem Wort while folgt, wie bei einer If Anweisung, eine Bedingung, die mithilfe von Vergleichsoperatoren erstellt wird.

Auch hier dürfen Sie den Doppelpunkt am Ende der Zeile nicht vergessen, ähnlich wie bei uf-else und for.

Es wird eine zufällige Zahl ermittelt und zur bisherigen Summe addiert. Die neue Summe errechnet sich also aus der alten Summe plus der generierten Zahl. Die neue Summe wird ausgegeben.

Die Anweisung zur Ausgabe des Texts Ende wird erst erreicht, wenn die Summe nicht mehr kleiner als 30 ist.

#### 3.4.8 Spiel, Version mit while-Schleife und Zähler

Die while Schleife wird nun auch im Kopferechenspiel zur Wiederholung der Eingabe genutzt. Der Benutzer hat beliebig viele Versuche, die Aufgabe zu lösen. Die Variable versuch, die als Zähler für die Versuche dient, muss separat gesteuert werden.
Sie ist nicht mehr automatisch eine Schleifenvariable.

Die Ausgabe hat sich nicht geändert.

Der Benutzer hat beliebig viele Verusche.

Die While-Schleife läuft, solange die richtige LÖsung nicht ermittelt wird. Die Variable zahl wird mit einem Wert vorbesetzt, der dafür sorgt, dass die while-Schleife mindestens einmal läuft. Die Veriable versuch wird mit 0 vorbesetzt und dient als laufende Nummer. Nach Eingabe der richtigen LÖsung wird dem Benutzer die Anzahl der Versuche mitgeteilt.

#### 3.4.9 Kombinierte Zuweisungsausdrücke

Mit Python 3.8 wird der Operator := für kombinierte Zuweisungen eingeführt. Er führt auch den Spitznahmen walrus-operator, aufgrund der Ähnlichkeit mit den Augen und den Zähnen eines Walrosses.
Er ermöglicht kürzere Ausdrücke, in denen allerdings eine höhere Komplexität steckt.
Nachfolgend sehen Sie, wie Sie mithilfe des Operators das Beispiel aus Abschnitt 3.4.7 verkürzen können

```py
import random 
random.seed()
summe = 0

while (summe := summe + random.randint(1,8)) <30:
    print("Zwischensumme:", summe)
print("Ende")
```

Die Zeile, die mit dem Schlüsselwort while beginnt, beinhaltet mehrere abläufe. Zunächst wird die Summe un einen zufällig ermittelten Wert erhöht. Anschließend wird die nue Summe mit der Zahl 30 verglichen. 
Dieser Vergleich steuert die Schleife. Aufgrund des niedrigen Vorrangs des Operators := muss die Zuweisung in runden Klammern stehen.

### 3.5 Entwicklung eines Programmes

Bei der Entwicklung Ihrer eigenen Programme sollten Sie Schritt für Schritt vorgehen. Stellen Sie zuerst einige Überlegungen dazu an, wie das gesamte Programm aufgebaut sein sollte, und zwar auf Papier. Aus welchen Teilen sollte es nacheinander bestehen? Versuchen Sie anschließend nicht, das gesamte Programm mit all seinen kopmlexen Bestandteilen auf einmal zu schreiben! Dies ist der größte Fehler, den Einsteiger (und manchmal auch Fortgeschrittene) machen können.

Schreiben Sie zunächst eine einfache Version des ersten Programmteils. Anschließend testen Sie sie. Erst nach einem erfolgreichen TEst fügen Sie den folgenden Programmteil hinzu. Nach jeder Änderung testen Sie wiederum.
Sollte sich ein Fehler zeugen, wissen Sie, dass er aufgrund der letzten Änderung aufgetreten ist. Nach dem letzten Hinzufügen haben Sie eine einfache Version Ihres gesamten Programms erstellt.

Nun ändern Sie einen Teil Ihres Programmes in eine komplexere Version ab. Auf diese Weise machen Sie Ihr Programm Schritt für Schritt komplexer, bis  Sie schließlich das gesamte Programm so erstellt haben, wie es Ihren anfänglichen Überlegungen auf Papier entspricht.

Manchmal ergibt sich während der praktischen Programmierung noch die eine oder andere Änderung gegenüber Ihrem Entwurf. Das ist kein Problem, solange sich nicht der gesamte Aufbau ändert. Sollte dies allerdings der Fall sein, kehren Sie noch einmal kurz zum Papier zurück und überdenken den Aufbau. Das bedeutet nicht, dass Sie die bisherigen Programmzeilen löschen müssen, sondern möglicherweise nur ein wenig ändern und anders anordnen.

Schreiben Sie Ihre Programme übersichtlich. Falls Sie gerade überlegen, wie sie drei, vier bestimmte Schritte Ihres Programms auf einmal machen können: Machen Sie daraus einfach einzelne Anwendungen, die der Reihe nach ausgeführt werden. Dies vereinfacht eine eventuelle Fehlersuche. Wenn Sie oder eine andere person Ihr Programm später einmal ändern oder erweitern möchten, gelingt der Einstieg in den Aufbau des Programms wesentlich schneller.

Sie können die Funktion `print()` zur Kontrolle von Werten und zur Suche von logsichen Fehlern einsetzten. Zusätzlich können Sie einzelne Zeilen Ihres Programms als Kommentar kennzeichne, um festzustellen, welcher Teil des Programms fehlerfrei läuft und welcher Teil demnach fehlerbehaftet ist.

### 3.6 Fehler und Ausnahmen

Macht der Anwender nach einer Eingabeaufforderung eine falsche Eingabe (gibt er z. B. keine Zahl, sondern einen Text ein), wird das Programm mit einer Fehlermeldung beendet. Bisher gehe ich vereinfacht davon aus, dass der Anwender korrekte Eingaben vornimmt. In diesem Abschnitt beschreibe ich, wie Sie Fehler vermeiden oder abfangen können.

#### 3.6.1 Basisprogramm
Durch das Abfangen von falschen Eingaben wird die Benutzung eines Programms für den Anwender duetlich kompfortabler. Im folgenden Programm soll eine ganze Zahl eingegeben werden. Da der Benutzer diese Programm durch die Eingaber von Text oder Sonderzeichen zum Abbruch bringen kann, wird es immer weiter verbessert.

```py
# Eingabe
print("Bitte geben Sie eine Zahl ein!")
z = input()

# Umwandlung
zahl = int(z)

# Ausgabe
print("Sie haben die ganze Zahl", zahl, "richtig eingegeben")
print("Ende des Programms")
```

Gibt der Anwender eine Zahl, zB 12 ein, läuft das Programm fehlerfrei bis zum Ende und erzeugt die gewünschte Ausgabe.

Macht der Anweder jedoch eine falsche Eingabe (z.B. 3a), bricht das Programm vorzeitig ab und erzeugt die folgende Ausgabe:

```
Traceback (most recent call last):
  File "insert-path.py", line 6, in <module>
    zahl = int(z)
VauleError: invalid literal for int() with base 10: '3a'
```

Diese Information weisen auf die STelleim Programm hin, an der der Fehler bemerkt wird. Außerdem wird die Art des Fehler mitgeteilt (ValueError).

#### 3.6.2 Fehler abfangen

Zunächst soll eine Fehleingabe abgefangen werden, um einen Abbruch des Programms zu vermeiden. Zu diesem Zweck müssen Sie die STelle hausfinden, an der eine Fehleingabe auftreten kann. Hier müssen Sie das Programm verbessern.

Das Programm soll zukünftig an dieser Stelle alle Arten von Fehlern abfangen, die Python automatisch erkennen kann. Dies erreichen Sie in einem ersten Schritt durch die folgende Änderung:

```py
# Eingabe
print("Bitte geben Sie eine ganze Zahl ein")
z = input()

# Versuch der Umwandlung

try:
    zahl = int(z)
    print("Sie haben die ganze Zahl", zahl, " richtig eingegeben")

# Fehler bei Umwandlung

except:
    print("Sie haben die ganze Zahl nicht richtig eingegeben")

print("Ende des Programms")
```

Wenn der Anwender eine richtige ganze Zahl eingibt, läuft das Programm wie bisher. Bei einer falschen Eingabe erscheint nun eine entsprechende Meldung. Das Programm bricht jedoch nicht ab, sondern läuft bis zum Ende.

**try**
Die Anweisung try leitet eine Ausnahmebehandlung ein. Ähnlich wie bei der if-Anweisung gibt es verschiedene Zweige, die das Programm durchlaufen kann. Das programm versucht (try), die Anweisungen durchzuführen, die eingerückt nach try stehen.
Falls die Eingabe erfolgreich ist, wird der except Zweig nicht ausgeführt, ähnlich wie beim else Zweit der if-Anweisung.

**except**
Ist die Eingabe daggen nicht erfolgreich und handelt es such um einen Fehler, wird der Fehler oder adie Ausnahme(exception) mit der Anweisung except abgefangen. In diesem Fall werden alle eingerückten Anweisungen im except-Zweig durchgeführt. Das Programm läuft ohne Abbruch zu Ende, da der Fehler zwar auftritt, aber abgefangen wird.

Nach try und except muss jeweils ein Doppelunkt gesetzt werden, wie bei if-else, for oder while.

**Hinweis**
Nur die kritische Zeile wird in der Ausnahmebehandlung eingebettet. Sie sollten sich also Gedanken darüber machen, welche Stellen Ihres Programms fehlerträchtig sind. Eine Eingeabeaufforderung ist solch ein kritische Stelle. Andere Fehlermöglichkeiten sind z. B. die Bearbeitung einer Datei (die möglicherweise nicht exisitert) oder die Ausgabe an einen Drucker (der vielleicht nicht eingeschaltet ist).


#### 3.6.3 Eingabe wiederholen

In einem zweiten Schritt wird dafür gesorgt, dass der Anwender nach einer falschen Eingabe eine erneute Eingabe machen kann. Der gesamt Eingabevorgang mit Ausnahmebehandlung wird so lange wiederholt, bis die Eingabe erfolgreich war. Betrachten Sie das folgende Programm:

```py
# Initialisierung der while-Schleife
fehler = 1

# Schleife bei falscher Eingabe

while fehler == 1:
    # Eingabe
    print("Bitte geben Sie eine ganze Zahl ein")
    z = input()

    # Versuch der Umwandlung
    try:
        zahl = int(z)
        print("Sie haben die ganze Zahl", zahl, "eingegeben")
        fehler = 0
    
    # Fehler bei Umwandlung
    except:
        print("Sie ahben die ganze Zahl nicht richtig eingegeben")

print("Ende des Programms")
```

**Hinweis**
Beachten Sie die doppelte Einrückung: einmal nach while und nocheinmal nach try-except.

Die Variable fehler ist notwending, um die Eingabe gegebenenfalls wiederholen zu können. Sie wird zunächst auf den Wert 1 gesetzt. Es wird eine while-Schleife formuliert, in der der Eingabevorgang mit der Ausnahmebehandlung eingebettet ist. Die Schleife wird wiederholt, solange die Variable fehler den wert 1 hat.

Ist die Eingabe erfolgreich, wird die Variable fehler auf 0 gesetzt. Das führt dazu, dass die Schleife beendet wird und da Programm regulär fortfahren kann. Ist die Eingabe nicht erfolgreich, hat fehler nach wie vor den wert 1 und der Eingabevorgang wird wiederholt.

#### 3.6.4 Exkurs: Schleifenfortsetzung mit `continue`

An dieser Stelle möchte ich auf ein Thema zurückkommen, das bereists in Abschnitt 3.4 Schleifen, behandelt wurde. Sie kennen aus diesem Abschnitt die Anweisung break, die zum unmittelbaren Abbruch einer Schleife führt.

Die Anweisung `continue` dient zum unmittelbaren Abbruch des aktuellen Durchlaufs einer Schleife. Die Schleife wird anschließend mit dem nächsten Durchlauf fortgesetzt. Betrachten Sie hierzu das folgende Programm:

```py
for i in range (1,7):
    print("Zahl:", i)
    if 3 <= i <= 5:
        continue
    print("Quadrat:", i*i)
```

Die Schleife durchläuft alle Zahlen von 1 bis 6. Alle diese Zahlen werden auch ausgegeben. Liegt die aktuelle Zahl zwischen 3 und 5, wird der Rest der Schleife übergangen und unmittelbar der nächste Schleifendurchlauf begonnen. Andernfalls wird das Quadrat der Zahl ausgegeben.

#### 3.6.5 Spiel, Version mit Ausnahmebedingung

Die Ausnahmebehandlung und die Anweisung `continue` werden nun auch im KOpfrechenspiel eingesetzt. Damit kann ein Eingabefehler abgefangen und das Programm reulär fortgesetzt werden.

Die umwandlung der Eingabe steht in einem `try-except` Block. Falls die Umwandlung aufgrund einer falschen Eingabe nicht gelingt, erscheint eine entsprechende Meldung. 
Der Rest der Schleife wird übergangen, und die nächste Eingabe wird unmittelbar angefordert.

### 3.7 Funktionen und Module

Die Modularisierung, also die Zerlegung eines Programms in selbst geschriebene Funktionen, bietet besonders bei größeren Programmen unübersehbare Vorteile:
* Programmteile, die mehrmals benötigt werden, müssen nur einmal definiert werden.
* Nützliche Programmteile können in mehrerenProgrammen verwendet werden.
* Umfangreiche Programme können in übersichtliche Teile zerlegt werden.
* Pflege und Wartung von Programmen werden erleichtert.
* Der Programmcode ist für den Programmierer selbst (zu einem späteren Zeitpunkt) und für andere Programmierer leichter zu verstehen.

Neben den selbst geschriebenen Funktionen gibt es in Python, wie in jeder anderen Programmiersprache auch, zahlreiche vordefinierte Funktionen, die dem Entwickler viel Arbeit abnehmen können. Diese Funktionen sind entweder fest eingebaut oder über die Einbindung spezieller Module verfügbar.

Als Beispiel für eine fest eingebaute Funktion wird bereits `input()` eingesetzt. Jede Funktion hat eine spezielle Aufgabe. So hält bspw. die Funktion input() das Programm an und nimmt eine Eingabe entgegen.

Wie viele (aber nicht alle) Funktionen hat `input()` einen sogenannten Rückgabewert, liefert also ein Ergebnis an die Stelle des Programms zurück, von der sie aufgerufen wird: die eingegebene Zeichenkette.

Es folgen zwei Hinweise für fortschrittene Leser, die bereits mit einer anderen Programmiersprache gearbeitet haben:
* Funktionen können in Python nicht überladen werden. Falls Sie eine Funktion mehrfach definieren, gegebenenfalls mit unterschiedlichen Parametern, so gilt nur die jeweils letzt Definition.
* Seit Python 3.5 können Sie mithilfe eines Typenhinweises angeben, welche Datentyp der Rückgabewert einer Funktion haben soll. Beachten Sie dazu bitte Abschnitt 3.2.6.

#### 3.7.1 Einfache Funktionen

Einfache Funktionen führen bei Aufruf stets die gleiche Aktion aus. Im folgenden Beispiel führt jeder Aufruf der funktion `stern()` dazu, dass eine optische Trennung auf dem Bildschirm ausgegeben wird:

```py
# Definition der Funktion
def stern():
    print("----------------")
    print("*** Trennung ***")
    print("----------------")

# Hauptprogramm
x = 12
y = 5

stern()
print("x =", x, ", y =", y)
stern()
print("x + y =", x + y)
stern()
print("x - y =", x - y)
stern()
```

Im oberen Teil des Programms wird die Funktion stern() definiert. Nach der Anweisun `def` folgt der Name der Funktion (stern), anschließend folgen runde Klammern und der bereits bekannte Doppelunkt. Innerhalb der Klammern könnten Werte an die Funktion übergeben werden. Dazu mehr im Abschnitt 3.7.2 Parameter, und in Abschnitt 3.7.3 Mehrere Parameter. Die nachfolgenden eingerückten ANweisungen werden jedes Mal durchgeführt, wenn die Funktion aufgerufen wird.

Eine Funktion wird zunächst nur definiert und nicht durchgeführt. Sie steht sozusagen zum späteren Gebrauch bereit. Im unteren Teil der Datei beginnt das eigentliche Programm. Es werden einige Rechenoperationen mit zwei Variablen durchgeführt. Mithilfe der Funktion `stern()` werden die Ausgabezeilen otpsich voneinander getrennt. Sie wird insgesamt viermal aufgerufen. Nach Bearbeitung der Funktion fährt das Programm jedes Mal mit der Anweisung fort, die dem Aufruf der Funktion folgt.

Eine Funktion wird aufgerufen, indem Sie ihren Namen, gefolgt von runden Klammern, notieren. Falls Sie Informationen an die Funktion übergeben möchten, notieren Sie sie innerhalb der runden Klammern.

Den Namen einer Funktion können Sie weitgehend frei wählen - es gelten die gleichen Regeln wie bei den Namen von Variablen, siehe auch Abschnitt 2.1.5, `Variablen und Zuweisung`: Der Name kann aus den Buchstaben a-z, A-Z, 0-9 und _ bestehen. Er darf nicht mit einer Ziffer beginnen und keinem reservierten Wort in Python entsprechen.

#### 3.7.2 Funktionen mit einem Parameter

Bei einem Aufruf können auch Informationen An Funktionen übermittelt werden, sogenannte `Parameter`. Diese Informationen können innerhalb der Funktion ausgewertet werden und führen gegebenenfalls bei jedem Aufruf zu unterschiedlichen Ergebnissen. Ein Beispiel:

```py
# Definition der Funktion
def quadrat(x):
    q = x * x
    print("Zahl: " x, "Quadrat:", q)

# Hauptprogramm
quadrat(4.5)
a = 3
quadrat(a)
quadrat(a*2)
``` 

Die Definition der Funktion quadrat() enthält eine Variable innerhalb der KLammern. Beim Aufruf wird ein Wert an die Funktion übermittelt und dieser Variablen zugwiesen.

**Hinweis**
 Die Funktion erwartet genau einen Wert. Sie darf also nicht ohne einen Wert oder mit mehr als einen Wert aufgerufen werden, sonst bricht das Programm mit einer Fehlermeldung ab.

#### 3.7.3 Funktionen mit mehreren Parametern

Eine Funktion kann noch vielseitiger werden, wenn Sie ihr mehrere Parameter übermitteln. Dabei ist auf die übereinstimmende Anzahl und die richte Reihenfolge der Parameter zu achten. Ein Beispiel:

```py
# Definition der Funktion
def berechnung(x,y,z):
    ergebnis = (x+y) * z
    print:("Ergebnis:", ergebnis)

# Hauptprogramm
berechnung(2,3,5)
berechnung(5,2,3)
```

Es werden genau drei Parameter erwartet, bei beiden Aufrufen werden auch drei Werte übermittelt. Wie Sie am Ergebnis erkennen, ist die Reihenfolge der Parameter wichtig.
* Beim ersten Aufruf erhält x den Wert 2, y den Wert 3 und z den Wert 5. Das Ergebnis der Rechnung: (2+3) * 5 = 25.
* Beim zweiten Aufruf werden dieselben Zahlen übergeben, aber in anderer Reihenfolge. Es erbit sich die Rechnung: (5 + 2) * 3 = 21.

#### 3.7.4 Funktionen mit Rückgabewert

Funktionen werden häufig zur Berechnung von Ergebnissen eingestezt. Zu diesem Zweck können Funktionen ihre Ergebnisse als sogenannte Rückgabewerte zurückliefern.

Im Unterschied zu vielen anderen Programmiersprachen können Funktionen in Python mehr als einen Rückgabewert liefern, siehe Abschnitt 5.7.4, Mehrere Rückgabewerte. In diesem Abschnitt werden aber zunächst nur Funktionen betractet werden, die enau einen Rückgabewert zur Verfügung stellen.

Im folgendne beispiel wird eine Funktion, die einen Rückgabewert liefert, auf verschienene Arten vom Hauptprogramm aus aufgerufen.

```py
# Definition der Funktion
def mittelwert(x,y):
    ergebnis = (x+y)/2
    return ergebnis

# Hauptprogramm
c = mittelwert(3,9)
print("Mittelwert:", c)
x = 5
print("Mittelwert:", mittelwert(x,4))
```
```
Mittelwert: 6,0
Mittelwert: 4,5
```

Innerhalb der Funktion wird zunächst das Ergebnis berechnet. Es wir anschließend mithilfe der Anweisung return an die aufrugende Stelle zurückgeliefert. Die Anweisung return beendet außerdem unmittelbar den Ablauf der Funktion.

Beim ersten Aufruf wird der Rückgabewert in der Variablen c zwischengespeichert. Es kann im weiteren Verlauf des Programms an beliebiger Stelle verwendet werden.

Beim Zweifen Aufruf eschen zwei Dinge gleichzeitig: Die Funktion mittelwert() wird aufgerufen und liefer ein Ergebnis. Außerdem wird dieses Ergebnis unmittelbar ausgegeben.

#### 3.7.5 Spiel, Version mit Funktionen

Das Programm mit dem Kopfrechenspiel umfasst nun zwei Funktionen, die erste Funktion dient zur Ermittlung der Aufgabe, die zweite zur Bewertung der Eingabe.

Die Ausgabe hat sich nicht geändert.

In der Funktion *aufgabe()* werdne die beiden Zufallszahlen ermittelt, und die Aufgabe wird auf dem Bildschirm ausgegeben. Ußerdem wird das Ergebnis der Aufgabe als Rückgabewert an das Hauptprogramm zurückgeliefert.

Der Funktion *kommentar()* werden zwei Zahlen als parameter übermittelt: die Lösung des Anwenders und das richtige Ergebnis. Innerhalb der Funktion wird die eingegebene Lösung untersucht, und ein entsprechender Kommentar wird ausgegeben. Die Funktion hat keinen Rückgabewert.

### 3.8 Das fertige Spiel

Zum Abschluss des Programmierkurses erweitern wir das Kopfrechenspiel noch etwas - dabei nutzen wir die Programmiermittel, die Ihnen inzwischen zur Verfügung stehen.

Die Erweiterungen:
* Es werden bis zu zehn Aufgaben nacheinander gestellt. der Benutzer kann dabei die Anzahl selbst bestimmen.

* Zusätzlich zur Addition kommen die weiteren Grundrechenarten zum Einsatz: Subtraktion, Multiplikation und Division.

* Die Bereiche, aus denen die zufälligen Zahlen gewält werden, hängen von der Rechenart ab. ei der Multiplikation wird z. B. mit kleineren Zahlen gerechnet als bei der Addition.

* Der Benutzer hat maximal drei Versuche pro Aufgabe.

* Die Anzahl der richtig gelösten Aufgaben wird ermittelt.

Die einzelnen Abschnitte des Programms sind nummeriert. Diese Nummern finden sich in der Erkläuterung wieder. In späteren Kapiteln kommen weitere Ergänzungen hinzu. Es folgt das Programm:

```py
# 1 Zufallsgenerator
import random
random.seed()

# 2 Anzahl Aufgaben
anzahl = -1
while anzahl<0 or anzahl >10:
    try:
        print("Wie veile Aufgaben (1 bis 10):")
        anzahl = int(input())
    except:
        continue

# 3 Anzahl richtige Ergebnisse
richtig = 0

# 4 Schelife mit Anzahl Aufgaben
for aufgabe in range(1, anzahl+1):

    # 5 Operator Auswahl
    opzahl = random.randint(1,4)

    # 6 Operandenauswahl
    if opzahl == 1:
        a = random.randint(-10,30)
        b = random.randint(-10,30)
        op = "+"
        c = a + b
    
    if opzahl == 2:
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "-"
        c = a - b
    
    if opzahl = 3:
        a = random.randint(1,10)
        b = random.randint(1,10)
        op = "*"
        c = a * b

    # 7 Sonderfall Divison

    if opzahl = 4:
        b = random.randint(1,10)
        c = random.randint(1,10)
        op = "/"
        a = c * b
    
    # 8 Aufgabenstellung

    print("Aufgabe", aufgabe, "von" annzahl, ":", a, op, b)

    # 9 Schelife mit 3 Versuchen

    for versuch in range(1,4):
        
        # 10 Eingabe
        try:
            print("Bitte eine Zahl eingeben:")
            zahl = int(input())
        except:
            # Falls Umwandlung nicht erfolgreich
            print("Sie haben keine Zahl eingegeben")
            # Schleife unmittelbar fortsetzen
            continue

        # 11 Kommentar

        if zahl == c:
            print(zahl, "ist richtig!")
            richtig = richtig + 1
            break
        else:
            print(zahl, "ist falsch!")

    # 12 Richtiges Ergebnis der Aufgabe
    print("Ergebnis:", c)

# 13 Anzahl richtige Ergebnisse
print ("Richtig:" richtig, "von", anzahl)
```

Nach der Initialisierung des Zufallsgenerators (1) wird die gewünschte Anzahl der Aufgaben eingelesen (2). Da der Benutzer einen Fehler bei der Eingabe machen könnte, findet eine Ausnahmebehandlung statt.

Der Rückgabewert der Funktion `input()` wird unmittelbar als Parameter der Funktion `int()`genutzt. So werden zwei Schritte auf einmal erledigt.

Der Zähler für die Anzahl der Richtig gelösten Aufgaben (`richtig`) wird auf `0` gestellt (3). Es wird eine äußere `for`-Schleife mit der gewünschten Anzahl gestartet (4).

Der Operator wird per Zufallsgenerator ermittelt (5). Für jeden Operator gibt es andere Bereiche, aus denen die Zahlen ausgewählt werden (6). Der Operator selbst und das Ergebnis werden gespeichert.

Eine Besonderheit ist bei der Division zu beachten (7): Es sollen nur ganze Zahlen vorkommen. Die beiden zufälligen Operanden (a und b) werden daher aus dem Ergebnis einer Multiplikation ermittelt.

Die Aufgabe wird gestellt (8). Dabei werden zur besseren Orientierung des Benutzers auch die laufende Nummer und die Gesamtanzahl der Aufgaben ausgegeben. Es wird eine innere `for`-Loop für maximal drei Versuche gestartet (9).

Die Eingaben des Benutzers (10) werden komentiert (11). Nach maximal drei Versuchen wird das richtige Ergebnis ausgegeben (12). Zuletzt wird die Anzahl der richtig gelösten Aufgaben ausgegeben (13).


## 4 Datentypen

Dieses Kapitel beschäftigt sich mit den Eigenschaften und Vorteilen der verschiedenen Objekttypen. Es werden Operationen, Funktionen und Operatoren für die jeweiligen Datentypen vorgestellt. Ein eigener Abschnitt über Objektreferenzen und Objektidentität vervollständigt die Objektbetrachtung.

Der Datentyp einer Variablen muss in Python nicht festgelegt werden. Alle Daten werden als Objekte gespeichert. Es gibt grundsätzlich zwei Typen von Objekten:
1. einzelne Objekte, wie z.B. Zahlen oder Zeichen
2. zusammengehörige Gruppen von Objekten, wie zB. Strings, listen, Tupel, Dictionarys und Sets

In diesem Kapitel geht es zunächst um Zahlen. Später folgen die anderen Objekttypen. Dabei stelle ich auch die Gemeinsamkeiten und Unterschiee der Objekttypen vor.

Seit Python 3.6 können Sie angeben, welchen Datentyp eine Variable haben soll. Beachten Sie dazu Abschnitt 3.2.6 `Typhinweise`.

### 4.1 Zahlen

Ganze Zahlen, Zahlen mit Nachkommastellen, Brücke und Operationen mit Zahlen sind Themen dieses Abschnitts. Es gibt einige fest eingebaute Funktionen für Zahlen. Zudem enthält das Modul `math` eine Reihe von mathematischen Funktionen.

#### 4.1.1 Ganze Zahlen
Als Objekttyp für ganze Zahlen dient `int` (von engl `integer` für ganzzahlig). Zahlen dieses Typs sind unendlich genau.

Üblicherweise wird das dezimale Zahlensystem mit der Basis 10 benutzt. Außerdem stehen in Python die folgenden Zahlensysteme zur Verfügung:

* Das duale Zahlensystem (mit der Basis 2)
* Das oktale Zahlensystem (mit der Basis 8)
* das hexadezimale Zahlensystem (mit der Basis 16)

Ein Beispiel:

```py
a = 27
print("Dezimal:", a)
print("Hexadeimal:", hex(a))
print("Oktal:", oct(a))
print("Dual:", bin(a))

b = 0x1a + 12 + 0b101 + 0o67
print("Summe:", b)
```
```
Dezimal: 27
Hexadezimal: 0x1b
Oktal: 0o33
Dual: 0b11011
Summe: 98
```

Die dezimale Zahl 27 wird in die drei anderen Zahlensysteme umgerechnet und ausgegeben.

Die Funktion `hex()` dient zur Umrechnung und Ausgabe der Zahl in das hexadezimale System. Dieses System nutzt neben den Ziffern 0 bis 9 die Buchstaben a bis f (oder auch A bis F) als Ziffern für die Werte von 10 bis 15. Die zahl 0x1b entspricht dem folgenden Wert:

1 x 16^1 + B x 16^0 = 1 x 16^1 + 11 x 16^0 = 16 + 11 = 27

Zur Umrechnung und die Ausgabe der Zahl in das oktale system dient die Funktion `oct()`. Das oktale System nuttzt nur die Ziffern 0 bis 7. Die Zahl 0o33 entspricht dem folgenden Wert:

3x8^1 + 3x8^0 = 24 + 3 = 27

Die Funktion `bin()` dient zur Umrechnung und Ausgabe der Zahl in das duale / binäre System. Dieses System nutzt nur die Ziffern 0 und 1. Die Zahl 0b11011 entspricht dem folgenden Wert:

1x2^4 + 1x2^3 + 0x2^2 + 1x2^1 + 1x2^0 = 16 + 8 + 0 + 2 + 1 = 27

Sie können auch direkt mit Zahlen in anderen Zahlensystemen rechnen.
Die Berechnung der Variablen b ergibt:

0x1a + 12 + 0b101 + 0o67 =
1x16^1 + a x 16^0 + 12 + 1x2^2 + 0x2^1 + 1x1^0 + 6x8^1 + 7x8^0 =
16 + 10 + 12 + 4 + 0 + 1 + 48 + 7 = 98

Bei der Eingabe oder Zuweisung muss das Präfix `0x`, `0b` bzw. `0o` or der eigentlichen Ziffernfolge stehen, damit das zugehörige Zahlensystem erkannt wird.

Zahlen setzten sich auf der niedrigsten Ebene aus Bits und Bytes zusammen. Im Abschnitt 4.1.8 werden Sie noch ein wenig intensiver mit Dualzahlen, der Funktion `bin()` und den sogenannten Bitoperatoren arbeiten, die Ihnen den Zugriff auf Bit-Ebene erleichtern.

#### 4.1.2 Zahlen mit Nachkommastellen

Der Datentyp für Zahlen mit Nachkommastellen heißt `float`. Diese sogenannten Fließkommazahlen werden mithilfe des Dezimalpunkts und gegebenenfalls der Exponentialschreibweise angegeben.

Dazu ein kleines Beispiel:

```py
a = 7.5
b = 2e2
c = 3.5E3
d = 4.2e-3
e = 1_250_000.500_001

print(a,b,c,d,e)
```

```
7.5 200.0 3500.0 0.0042 1250000.500001
```

Die Variable `a` erhält den Wert 7.5. Die Nachkommastellen werden mit einem Dezimalpunkt abgetrennt. Dies gilt auch für die Eingabe einer Zahl mit Nachkommastellen mithilfe der Funktion input(). Die Ariable `b` erhält den Wert 200 (= 2x10^2 = 2x100). Die Variable `c` erhält den wert 3.500 (= 3,5 x 10^3 = 3,5 x 1.000), die Variable `d` den wert 0,0042 (=4,2 x 10^-3 = 4,2 x 0,001).

Bei der Zuweisung der Exponentialschreibweise wir dmithilfe des `e` (oder `E`) ausgedrückt, um wie viele Stellen und in welche Richtung der Dezimalpunkt innerhalb der Zahl verschoben wird. Diese Schreibweise eignet sich z.B. für sehr große oder sehr kleine Zahlen, da sie die Eingabe vieler Nullen erspart.

Seit Python 3.6 können Sie einen Unterstrich benutzen, um Zahlen mit vielen Ziffern lesbarer zu machen. Es bietet sich an, ihn nach jeder dritten Ziffer einzufügen.

#### 4.1.3 Typ ermitteln
Es ist häufig nützlich zu wissen, ob es sich bei einer Zahl um eine ganze Zahl (Datentyp `int`) oder eine Fließkommazahl (Datentyp `float`) handelt. Die Funktion type() gibe den Typ(Die Klasse) eines Objekts aus, nicht nur für Zahlentypen. Hierzu ein Programmbeispiel:

```py
a = 2
print("Typ:", type(a))
b = 12/6
print("Typ:", type(b))
print("Modulo liefert:", 12 % 6 == 0)
```

```
Typ: <class 'int'>
Typ: <class 'float'>
Modulo liefert: True
```

Die Variable `a`enthält den Wert 2 und ist vom Typ `int`. Die Variable `b` enthält den gleich Wert, allerdings als Ergebnis von 12/6. Es handelt sich um ein Objekt vom Typ `float`. Die Information, dass ein Ergebnis ganzzahlig ist, erhalten Sie mithilfe des Modulo-Operators (%).

#### 4.1.4 Operator **

Neben den bereits behandelten Rechenoperatoren + (Addition), - (Subtraktion), * (Multiplikation), / (Division) und % (Modulo, Rest einer Ganzzahldivision) wird der Operator ** (Potenz) eingesetzt.

```py
z = 5 ** 3
print("5 hoch 3 =", z)
z = 5.2 ** 3
print("5.2 hoch 3 =", z)
z = -5.2 ** 3
print("-5.2 hoch 3 =", z)
z = 5.2 ** 3.8
print("5.2 hoch 3.8 =", z)
```
```
5 hoch 3 = 125
5.2 hoch 3 = 140.608
-5.2 hoch 3 = -140.608
5.2 hoch 3.8 = 525.790...
```
Der Variablen z wird nacheinancher Das Ergebnis verschienener Exponentialrechnungen zugewiesen. Anschließend wird ihr jeweils aktueller Wert mit einem Kommentar ausgegeben.

#### 4.1.5 Rundung und Konvertierung

In diesem Abschnitt folgt ein Vergleich der Ergebnisse bei beiden eingebauten Funktionen `round()` und `int()`.
Die Funktion `round()` dient zur Rundung einer Zahl - im Unterschied zu der bereits bekannten Funktion int() zur Konvertierun (Umwandlung) in eine ganze Zahl.

```py
# Positive Zahl
x = 12/7 
print("x:",x)

# Rundung und Konvertierung
rx = round(x,3)
print("x gerundet auf 3 Nachkomma-stellen:", rx)
rx = round(x)
print("x gerundet auf 0 Nachkomma-stellen:", rx)
ix = int(x)
print("int(x):", ix)

print()

# Negative Zahl
x = -12/7
print("x:", x)

# Rundung und Konvertierung
rx = round(x,3)
print("x gerundet auf 3 Nachkomma-stellen:", rx)
rx = round(x)
print("x gerundet auf 0 Nachkomma-stellen:", rx)
ix = int(x)
print("int(x):", ix)
```
```
x: 1.7142857142857142
x gerundet auf 3 Nachkomma-stellen: 1.714
x gerundet auf 0 Nachkomma-stellen: 2
int(x): 1

x: -1.7142857142857142
x gerundet auf 3 Nachkomma-stellen: -1.714
x gerundet auf 0 Nachkomma-stellen: -2
int(x): -1
```

Es wird die Division 12/7 ausgeführt. Das Rechenergebnis wird anschließend auf drei verschiedene Arten umgewandelt:

1. Mithilfe der eingebauten Funktion `round()` wird das Ergebnis auf drei Stellen nach dem Komma gerundet.
2. Mit der gleichen Funktion wird das Ergebnis auf die nächsthöhere oder nächstniedrigere ganze Zahl gerundet.
3. Mithilfe der eingebauten funktion `int()` wird adas ergebnis in eine ganze Zahl umgewandelt. Dabei werden - im Unterschied zum runden - die stellen nach dem Komma einfach weggeschnitten.

Die gleichen Operationen werden mit einer negativen Zahl mit Nachkommastellen durchgeführt.

#### 4.1.6 Winkelfunktionen

Im Modul `math` finden Sie u. a. die trigonometrischen Funktionen `sin()`, `cos()`, und `tan()`.

```py
# Modul math
inport math

# Trigonometrische Funktionen
x = 30
xbm = math.radians(x)
print("Sinus", x, "Grad:", math.sin(xbm))
print("Cosinus", x, "Grad:", math.cos(xbm))
print("Tangens", x, "Grad:", math.tan(xbm))
```
```
Sinus 30 Grad: 0.49999..
Cosinus 30 Grad: 0.866925..
Tangens 30 Grad: 0.5773..
```
Nach dem Import des Moduls `math` werden der Sinus, der Kosinus und der Tangens des Winkels 30 Grad berechnet.
Alle Funktionen beziehen sich auf eine Angabe des Winkels im Bogenmaß. Daher wird der Winkel zuvor mithilfe der Funktion `radians()` von Grad in Bogenmaß umgewandelt. Die funktion `degrees()` ermöglicht die umgekerhte Umwandlung, also von Bogenmaß in Grad.

#### 4.1.7 Weitere mathematische Funktionen

Ebenfalls im Modul `math` finden Sie einige Funktionenen und Konstanten, von denen Sie einige auch von IHrem Taschenrechner kennen.

```py
import math

a = 4.75
print("Variable a: ", a)
print("Quadratwurzel von a:", math.sqrt(a))

print("Natürlicher Logartihmus von a:", math.log(a))
print("e hoch a:", math.exp(a))
print("10er-Logarithmus von a:", math.log10(a))
print()

b = 34
print("Ganzzahlige Quadratwurzel:", math.isqrt(b))
print()

print("Kreiszahl pi:", math.pi)
print("Eulersche Zahl e:", math.e)
print()

t = 3, 2, -7
print("Produkt:", math.prod(t))
print("Fakultät von 5:", math.factorial(5))
print("Größter gem. Teiler von 60 und 135:", math.gcd(60,135))
print("Rest:", math.remainder(10.8, 2.5))
print("Rest:", math.remainder(11.8, 2.5))
print()

if math.isclose(3, 2.96, rel_tol=0.01):
    print("Nahe dran")
else:
    print("Nicht nahe dran")
```
```
Variable a:  4.75
Quadratwurzel von a: 2.179449471770337
Natürlicher Logartihmus von a: 1.55814461804655
e hoch a: 115.58428452718766
10er-Logarithmus von a: 0.6766936096248666

Ganzzahlige Quadratwurzel: 5

Kreiszahl pi: 3.141592653589793
Eulersche Zahl e: 2.718281828459045

Produkt: -42
Fakultät von 5: 120
Größter gem. Teiler von 60 und 135: 15
Rest: 0.8000000000000007
Rest: -0.6999999999999993

Nicht nahe dran
```

Zunächst werden die Funktion `sqrt()`zur Berechnung der Quadratwurzel einer positiven Zahl,
`log()` und die Funktion `log10()` zur Berechnung der Logarithmen einer positiven Zahl zur Basis e und zur Basis 10
und die Funktion `exp()` zur Berechnung von e^x aufgerufen.

Seit Python 3.8 können Sie mithilfe der Funktion `isqrt()` die ganzzahlige Quadratwurzel einer Zahl berechnen. Das ist der größte ganzzahlige Wert, der kleiner ist als die eigentliche Quadratwurzel einer Zahl.

Zudem gibt es die mathematischen Konstanten `pi` und `e`. Solche Konstanten stehen für unveränderbare Werte. Sie werden eingesetzt, weil man sich den Namen einer Konstanten meist besser merken kann als ihren Wert.

Seit Python 3.8 lässt sich mithilfe der Funktion `prod()` das Produkt der Elemente eines iterierbaren Objekts ermitteln, hier eines Tupels. Mehr zum Thema Tupel finden Sie in Abschnitt 4.4. Der Wert der Fakultät darf mathematisch und mithilfe der Funktion `factorial()` nur von positiven ganzen Zahlen berechnet werden.

Seit Python 3.5 gibt es die Funktion `gcd()`. Sie ermittelt den größten gemeinsamen Teiler (GGT, englisch greatest common divisor) zweier ganzer Zahlen. Das ist die größte Zahl, durch die sich beide Zahlen ohne Rest teilen lassen.

Seit Python 3.7 lässt sich mithilfe der Funktion `remainder()` der Rest einer Division gemäß dem IEEE-754-Standard berechnen. Dabei handelt es sich um die Differenz zur nächsten ganzen Zahl. Was bedeutet das? Im vorliegenden Beispiel werden 10.8 bzw. 11.8 durch 2.5 geteilt. Das mathematische Ergebnis liegt jeweils zwischen den beiden ganzen Zahlen 4 (4x 2.5 = 10) und 5 (4x 2.5 = 12.5). Im Fall von 10.8 liegt der Wert 10 näher, daher liefert die Funktion `remainder()` den Wert 0.8 (= 10.8 - 10). Im Fall von 11.8 liegt der Wert 12.5 näher, daher liefert die Funktion `remainder()`den Wert -0.7 (= 11.8 - 12.5).

Seit Python 3.5 können Sie mithilefe der Funktion `isclose()` feststellen, ob zwei Zahlen einander nahe sind. In den beiden obigen Beispielen wird mit hilfe der relativen Toleranz `0.01` festgestellt, ob die beiden Zahlen -um maximal 1% voneinander abweichen. Sie können einen von zwei benannten Parametern nutzen. Neben `rel_tol` gibt es auch `abs_tol`für die Messung mit einer absoluten Tolleranz.

#### 4.18 Bitoperatoren

Sämtliche Daten, ob nun Zahlen oder Zeichenketten, setzten sich auf der Hardwareebene aus Bits und Bytes zusammen. Auf dieser Ebene können Sie mit Dualzahlen (siehe 4.1.1),, der Funktion `bin()` und den sogenannten Bitoperatoren arbeiten.

```py
# Nur 1 Bit gesetzt
bit0 = 1        # 0000 0001
bit3 = 8        # 0000 1000
print(bin(bit0), bin(bit3))

# Bitweises AND
a = 5           # 0000 0101
bit0 = 1        # 0000 0001
erg = a & bit0  # 0000 0001
if erg:
    print(a, "ist ungerade")

# Bitweises OR
erg = 0             # 0000 0000
bit0 = 1            # 0000 0001
erg = erg | bit0    # 0000 0001
bit3 = 8            # 0000 1000
erg = erg | bit3    # 0000 1001
print("Bits nacheinander gesetzt:", erg, bin(erg))

# Bitweises Exclusive-OR
a = 21              # 0001 0101
b = 19              # 0001 0011
erg = a ^ b         # 0000 0110
print("UngleicheBits:", erg, bin(erg))

# Bitweise Inversion, aus x wird -(x+1)
a = 11              # 0000 1011
erg = ~a            # 1111 0100
print("Bitweise Inversion:", erg, bin(erg))

# Bitweise schieben
a = 11              # 0000 1011
erg = a >> 1        # 0000 0101
print("Um 1 nach rechts geschoben:", erg, bin(erg))
erg = a << 2        # 0010 1100
print("Um 2 nach links geschoben:", erg, bin(erg))
```

Zunächst werden die beiden Variablen `bit0` und bit `bit3` eingeführt, die bei einigen der nachfolgenden Berechnungen benötigt werden. Sie haben die werte 1 und 8. Am ende der Programmzeile sehen Sie sie als Dualzahl, also mithilfe von 8 Bit (= 1 Byte) notiert. Das letzte Bit eines Bytes wird als Bit 0 genannt, das vorletzte Bit ist Bit 1 usw. Die Werte der beiden Variablen `bit0` und `bit3` sind so gewählt, dass jeweils nur ein Bit gesetzt ist (=1), die restlichen Bits sind nicht gesetzt (=0).

Sie können sich auch eine Reihe von acht Leuchtioden vorstellen, die entweder an oder aus sind. Diese Information kann innerhalb eines Bytes gespeichert werden. Falls eines Bits gesetzt ist, ist die betreffende LED an, ansonsten aus. Zur Verdeutlichung werden die beiden Variablen `bit0` und `bit3` mithilfe der Funktion `bin()` als Dualzahl ausgegeben.

Sie können den Bitoperator `&` zur bitweisen Und-Verknüpfung zweier Zahlen nutzen. ÄHnlich wie beim logischen Operator `and` wird ein bestimmtes Bit im Ergebnis nur gesetzt, wenn diese Bit in beiden Zahlen gesetzt ist. Diese Operation wird für jedes einzelne Bit durchgeführt. 

Falls Sie wissen möchten, bo ein bestimmtes Bit innerhalb einer Zahl gesetzt ist, verknüpfen Sie diese Zahl mithilfe des Bitoperators & mit einer anderen Zahl, in der nun dieses eine gesuchte Bit gesetzt ist. Falls es sich um das Bit 0 handelt, wissen Sie darüber hinaus, ob die Zahl gerade (Bit 0 = 0) oder ungerade (Bit 0 = 1) ist.

Der Bitoperator `|` dient zut bitweisen Oder-Verknüpfung zweier Zahlen. Ähnlich wie beim logsichen Operator `or` wird ein bestimmtes Bit im Ergebnis gesetzt, wenn dieses Bit in einer der beiden Zahlen oder in beiden Zahlen gesetzt ist. Diese Operation wird auch für jedes einzelne Bit durchgeführt. 

Falls sie einzelne Bits einer Zahl setzen möchten, verknüpfen Sie diese Zahl mithilfe der Bitoperators `|` mit einer anderen Zahl, in der nur dieses eine gesuchte Bit gesetzt ist.

Der Bitoperator `^`  dient zur bitweisen Exklusiv-Oder-Verknüpfung zweier Zahlen. Ein bestimmtes Bit im Ergebnis wird gesetzt, wenn dieses Bit nur in einer der beiden zahlen gesetzt ist. Falls das Bit in beiden Zahlen gesetzt ist, wird das Ergebnis-Bit nicht gesetzt. Diese OPeration wird ebenfalls für jedes einzelne Bit durchgeführt.

Sie können den Bitoperator `~` zur bitweisen INversion einer Zahl nutzen. Dabei wird aus der Zahl x die Zahl -(x+1), aus 11 wird also die -12.

Die beiden Bitoperatoren `>>` und `<<` dienen zum Schieben von Bits innerhalb einer Zahl:
* Mithilfe von `>>` werden alle Bits um eine bestimmte Anzahl von Stellen nach rechts geschoben. Die Bits, die dabei nach rechts `Hinausfallen`, sind v erloren. Eine Verschiebung um n Bit nach rechts entspricht einer ganzzahligen Division durch 2^n. Eine Verschiebung um 1 Bit nach rechts entspricht also einer ganzahligen Division durch 2.
* Mithilfe von `<<` werden Alle Bits um eine bestimmte Anzahl von Stellen nach links geschoben. Eine Verschiebung um n Bit nach links entspricht also einer Multiplikation mit 2.

#### 4.1.9 Brüche

Python kann auch mit Brüchen rechnen bzw. Informationen über >Brüche zur Verfügung stellen. Dazu wird das Modul `fractions` genutzt:

```py
# Import des Moduls
import fractions

# Bruch
z = 12
n = 28
print("bruch:", z, "/", n)

# als Fraction

b1 = fractions.Faction(z,n)
print("Fraction:", b1)
print("Z, N:", b1.numerator, b1.denominator)
wert = b1.numerator / b1.denominator
print("Wert:", wert)
print()

# Umrechnen

x = 2.375
print("Zahl:", x)
b2 = fractions.Fraction(x)
print("Fraction:", b2)
```

Zunächst wird ein Beispielbruch in der bekannten FOrm dargestellt. Er wird gebildet aus zwei Zahlen: Zähler und Nenner.

Die Funktion `Fraction()` aus dem Modul `fractions` beitet verschiedene Möglichkeiten, einen Bruch zu erzeugen. Genauer gesatzt, handelt es sich bei `Fraction()` um den Konstruktor der Klasse `Fraction`. Damit wird eine Instanz (ein Objekt) der KLasse erzeugt und eine Referenz auf dieses Objekt zurückgeliefert. Klassen, Instanzen, Konstruktoren und andere Begriffe aus der objektorientierten Programmierung werden in Kapitel 6 genauer erkläutert.

Der Bruch `b1`, der aus 12/28 gebildet wird, wird bei der Erzeugung automatische auf 3/7 gekürzt.

Zähler und Nenner des Bruchs stehen in den Eigenschaften `numerator` und `denominator` einzeln zur Verfügung. Der Wert eines Bruchs lässt sich darüber berechnen: 3/7 = 0,428...

Umgekerht können Sie auch eine Zahl mit Nachkommastellen in einen Bruch umrechnen. Dazu übergeben Sie die Zahl der Konstruktormethode `Fraction()`: Aus 2.375 wird 19/8.

Im nachfolgenden Programm wird ein Bruch dazu genutzt, eine Zahl mit Nachkommastellen zu approximieren, also anzunähern. Dazu dient die Methode `limit_denominator()`.

```py
# Import des Moduls
import fractions

# untersuchte Zahl
x = 1.84953
print("Zahl:", x)

# als Bruck
b3 = fractions.Fraction(x)
print("Fraction:", b3)

# approximiert
b4 = b3.limit_denominator(100)
print("Approximiert auf Nenner max. 100:", b4)

# Genauigkeit
wert = b4.numerator / b4.denominator
print("Wert:", wert)
print("rel. Fehler:", abs((x-wert)/x))
```

