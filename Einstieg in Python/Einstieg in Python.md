# Einstieg in Python

Quelle: Buch: Einstieg in Python - Thomas Theis

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
    - [4.2 Zeichenketten](#42-zeichenketten)
      - [4.2.1 Eigenschaften](#421-eigenschaften)
      - [4.2.2 Operatoren](#422-operatoren)
      - [4.2.3 Operationen](#423-operationen)
      - [4.2.4 Funktionen](#424-funktionen)
      - [4.2.5 Umwandlung einer Zeichenkette in eine Zahl](#425-umwandlung-einer-zeichenkette-in-eine-zahl)
      - [4.2.6 Umwandlung einer Zahl in eine Zeichenkette](#426-umwandlung-einer-zahl-in-eine-zeichenkette)
      - [4.2.7 Datentyp "bytes"](#427-datentyp-bytes)
    - [4.3 Listen](#43-listen)
      - [4.3.1 Eigenschaften](#431-eigenschaften)
      - [4.3.2 Operatoren](#432-operatoren)
      - [4.3.3 Funktionen und Operationen](#433-funktionen-und-operationen)
    - [4.4 Tupel](#44-tupel)
      - [4.4.1 Eigenschaften](#441-eigenschaften)
      - [4.4.2 Operationen](#442-operationen)
      - [4.4.3 Tupel entpacken](#443-tupel-entpacken)
    - [4.5 Dictionarys](#45-dictionarys)
      - [4.5.1 Eigenschaften](#451-eigenschaften)
      - [4.5.2 Operatoren und Funktionen](#452-operatoren-und-funktionen)
      - [4.5.3 Views](#453-views)
      - [4.5.4 Vergleiche](#454-vergleiche)
    - [4.6 Mengen, Sets](#46-mengen-sets)
    - [4.6.1 Eigenschaften](#461-eigenschaften)
      - [4.6.2 Funktionen](#462-funktionen)
      - [4.6.3 Operatoren](#463-operatoren)
      - [4.6.4 Frozenset](#464-frozenset)
    - [4.7 Wahrheitswerte udn Nichts](#47-wahrheitswerte-udn-nichts)
      - [4.7.1 Wahrheitswerte True und False](#471-wahrheitswerte-true-und-false)
      - [4.7.2 Nichts, None](#472-nichts-none)
    - [4.8 Referenz, Identität und Kopie](#48-referenz-identität-und-kopie)
      - [4.8.1 Referenz und Identität](#481-referenz-und-identität)
      - [4.8.2 Ressourcen sparen](#482-ressourcen-sparen)
      - [4.8.3 Objekte kopieren](#483-objekte-kopieren)
  - [5 Weiterführende Programmierung](#5-weiterführende-programmierung)
    - [5.1 Allgemeines](#51-allgemeines)
      - [5.1.1 Kombinierte Zuweisungsoperatoren](#511-kombinierte-zuweisungsoperatoren)
      - [5.1.2 Programmzeile in mehreren Zeilen](#512-programmzeile-in-mehreren-zeilen)
      - [5.1.3 Eingabe mit Hilfestellung](#513-eingabe-mit-hilfestellung)
      - [5.1.4 Anweisung `pass`](#514-anweisung-pass)
      - [5.1.5 Funktionen `eval()` und `exec()`](#515-funktionen-eval-und-exec)
    - [5.2 Ausgabe und Formatierung](#52-ausgabe-und-formatierung)
      - [5.2.1 Funktion `print()`](#521-funktion-print)
      - [5.2.2 Formatierung mit String-Literalen](#522-formatierung-mit-string-literalen)
      - [5.2.3 Formatierung mit `format()`](#523-formatierung-mit-format)
      - [5.2.4 Formatierung wie in C](#524-formatierung-wie-in-c)
    - [5.3 Conditional Expression](#53-conditional-expression)
    - [5.4 Iterierbare Objekte](#54-iterierbare-objekte)
      - [5.4.1 Funktion `zip()`](#541-funktion-zip)
      - [5.4.2 Funktion `map()`](#542-funktion-map)
      - [5.4.3 Funktion `filter()`](#543-funktion-filter)
    - [5.5 List Comprehension](#55-list-comprehension)
    - [5.6 Fehler und Ausnahmen](#56-fehler-und-ausnahmen)
      - [5.6.1 Allgemeines](#561-allgemeines)
      - [5.6.2 Syntaxfehler](#562-syntaxfehler)
      - [5.6.3 Laufzeitfehler](#563-laufzeitfehler)
      - [5.6.4 Logsiche Fehler und Debugging](#564-logsiche-fehler-und-debugging)
        - [Einzelschrittverfahren](#einzelschrittverfahren)
        - [Weitere Möglichkeiten](#weitere-möglichkeiten)
      - [5.6.5 Fehler erzeugen](#565-fehler-erzeugen)
      - [5.6.6 Unterscheidung von Ausnahmen](#566-unterscheidung-von-ausnahmen)
    - [5.7 Funktionen](#57-funktionen)
      - [5.7.1 Variable Anzahl von Parametern](#571-variable-anzahl-von-parametern)
      - [5.7.2 Benannte Parameter](#572-benannte-parameter)
      - [5.7.3 Parameter mit Vorgabewerten](#573-parameter-mit-vorgabewerten)
      - [5.7.4 Mehrere Rückgabewerte](#574-mehrere-rückgabewerte)
      - [5.7.5 Übergabe von Kopieren und Referenzen](#575-übergabe-von-kopieren-und-referenzen)
      - [5.7.6 Lokal, global](#576-lokal-global)
      - [5.7.7 Rekursive Funktionen](#577-rekursive-funktionen)
      - [5.7.8 Lambda-Funktion](#578-lambda-funktion)
      - [5.7.9 Funktonsname als Parameter](#579-funktonsname-als-parameter)
    - [5.8 Eingebaute Funktionen](#58-eingebaute-funktionen)
      - [5.8.1 Funktionen `max()`, min()`, `sum()`](#581-funktionen-max-min-sum)
      - [5.6.2 Funktion `chr()` und `ord()`](#562-funktion-chr-und-ord)
      - [5.8.3 Funktionen `reversed()` und `sorted()`](#583-funktionen-reversed-und-sorted)
    - [5.9 Statistikfunktionen](#59-statistikfunktionen)
    - [5.10 Eigene Module](#510-eigene-module)
      - [5.10.1 Eigene Module erzeugen](#5101-eigene-module-erzeugen)
      - [5.10.2 Standard-Import eines Moduls](#5102-standard-import-eines-moduls)
      - [5.10.3 Import eines Moduls mit Umbenennung](#5103-import-eines-moduls-mit-umbenennung)
      - [5.10.4 Import von Funktionen](#5104-import-von-funktionen)
    - [5.11 Parameter der Kommandozeile](#511-parameter-der-kommandozeile)
      - [5.11.1 Übergabe von Zeichenketten](#5111-übergabe-von-zeichenketten)
      - [5.11.2 Übergabe von Zahlen](#5112-übergabe-von-zahlen)
      - [5.11.3 Beliebige Anzahl von Parametern](#5113-beliebige-anzahl-von-parametern)
    - [5.12 Programm `Bruchtraining`](#512-programm-bruchtraining)
      - [5.12.1 Der Ablauf des Programms](#5121-der-ablauf-des-programms)
      - [5.12.2 Hauptprogramm](#5122-hauptprogramm)
      - [5.12.3 Eine leichte Aufgabe](#5123-eine-leichte-aufgabe)
      - [5.12.4 Eine mittelschwere Aufgabe](#5124-eine-mittelschwere-aufgabe)
      - [5.12.5 Eine Schwere AUfgabe](#5125-eine-schwere-aufgabe)
  - [6 Objektorientierte Programmierung](#6-objektorientierte-programmierung)
    - [6.1 Was ist OOP?](#61-was-ist-oop)
    - [6.2 Klassen, Objekte und eigene Methoden](#62-klassen-objekte-und-eigene-methoden)
    - [6.3 Konstruktor und Destruktor](#63-konstruktor-und-destruktor)
    - [6.4 Besondere Methoden](#64-besondere-methoden)
    - [6.5 Operatormethoden](#65-operatormethoden)
    - [6.6 Referenz, Identität und Kopie](#66-referenz-identität-und-kopie)
    - [6.7 Vererbung](#67-vererbung)
    - [6.8 Mehrfachvererbung](#68-mehrfachvererbung)
    - [6.9 Datenklassen](#69-datenklassen)
    - [6.10 Enumerationen](#610-enumerationen)
    - [6.11 Spiel, objektorientierte Version](#611-spiel-objektorientierte-version)
  - [7 Verschiedene Module](#7-verschiedene-module)
    - [7.1 Datum und Zeit](#71-datum-und-zeit)
      - [7.1.1 Ausgabe der Zeit mit `localtime()`](#711-ausgabe-der-zeit-mit-localtime)
      - [7.1.2 Ausgabe der Zeit mit `strftime()`](#712-ausgabe-der-zeit-mit-strftime)
      - [7.1.3 Zeitangabe erzeugen](#713-zeitangabe-erzeugen)
      - [7.1.4 Mit Zeitangaben rechnen](#714-mit-zeitangaben-rechnen)
      - [7.1.5 Programm anhalten](#715-programm-anhalten)
      - [7.1.6 Spiel, version mit Zeitmessung](#716-spiel-version-mit-zeitmessung)
      - [7.1.7 Spiel, objektorientierte Version mit Zeitmessung](#717-spiel-objektorientierte-version-mit-zeitmessung)
    - [7.2 Warteschlangen](#72-warteschlangen)
      - [7.2.1 Klasse SimpleQueue](#721-klasse-simplequeue)
      - [7.2.2 Klasse LifoQueue](#722-klasse-lifoqueue)
      - [7.2.3 Klasse PriorityQueue](#723-klasse-priorityqueue)
      - [7.2.4 Klasse deque](#724-klasse-deque)
    - [7.3 Multithreading](#73-multithreading)
      - [7.3.1 Wozu dient Multithreading?](#731-wozu-dient-multithreading)
      - [7.3.2 Erzeugung eines Threads](#732-erzeugung-eines-threads)
      - [7.3.3 Identifizierung eines Threads](#733-identifizierung-eines-threads)
      - [7.3.4 Gemeinsame Daten und Objekte](#734-gemeinsame-daten-und-objekte)
      - [7.3.5 Threads und Exceptions](#735-threads-und-exceptions)
    - [7.4 Reguläre Ausdrücke](#74-reguläre-ausdrücke)
      - [7.4.1 Suchen von Teiltexten](#741-suchen-von-teiltexten)
      - [7.4.2 Ersetzen von Teiltexten](#742-ersetzen-von-teiltexten)
    - [7.5 Audioausgabe](#75-audioausgabe)
  - [Kapitel 8 Dateien](#kapitel-8-dateien)
    - [8.1 Dateitypen](#81-dateitypen)
    - [8.2 Öffnen und Schließen einer Datei](#82-öffnen-und-schließen-einer-datei)
    - [8.3 Sequenzielle Dateien](#83-sequenzielle-dateien)
      - [8.3.1 Sequenzielles Schreiben](#831-sequenzielles-schreiben)
    - [8.3.2 Sequenzielles Lesen](#832-sequenzielles-lesen)
      - [Beispiel 1](#beispiel-1)
      - [Beispiel 2](#beispiel-2)
      - [Beispiel 3](#beispiel-3)
      - [Beispiel 4](#beispiel-4)
      - [8.3.3 CSV-Datei schreiben](#833-csv-datei-schreiben)
      - [8.3.4 CSV-Datei lesen](#834-csv-datei-lesen)
    - [8.4 Dateien mit festgelegter Struktur](#84-dateien-mit-festgelegter-struktur)
      - [8.4.1 Formatiertes Schreiben](#841-formatiertes-schreiben)
      - [8.4.2 Lesen anbeliebiger Stelle](#842-lesen-anbeliebiger-stelle)
      - [8.4.3 Schreiben an beliebiger Stelle](#843-schreiben-an-beliebiger-stelle)
    - [8.5 Serialisierung](#85-serialisierung)
      - [8.5.1 Objekte in Datei schreiben](#851-objekte-in-datei-schreiben)
      - [8.5.2 Objekte aus Datei lesen](#852-objekte-aus-datei-lesen)
    - [8.6 Bearbeitung mehrer Datien](#86-bearbeitung-mehrer-datien)
        - [8.6.1 Funktion `glob.glob()`](#861-funktion-globglob)
      - [8.6.2 Funktion `os.scandir()`](#862-funktion-osscandir)
    - [8.7 Informationen über Dateien](#87-informationen-über-dateien)
    - [8.8 Dateien und Verzeichnisse verwalten](#88-dateien-und-verzeichnisse-verwalten)
    - [8.9 Beispielprojekt Morsezeichen](#89-beispielprojekt-morsezeichen)
      - [8.9.1 Morsezeichen aus Datei lesen](#891-morsezeichen-aus-datei-lesen)
      - [8.9.2 Ausgabe auf dem Bildschirm](#892-ausgabe-auf-dem-bildschirm)
      - [8.9.3 Ausgabe mit Tonsignalen](#893-ausgabe-mit-tonsignalen)
    - [8.10 Spiel, Version mit Highscore-Datei](#810-spiel-version-mit-highscore-datei)
      - [8.10.1](#8101)
      - [8.10.2 Aufbau des PRogramms](#8102-aufbau-des-programms)
      - [8.10.3 Code des Programms](#8103-code-des-programms)
    - [8.11 Spiel, objektorientierte Version mit Highscore-Datei](#811-spiel-objektorientierte-version-mit-highscore-datei)
  - [9 Internet](#9-internet)
    - [9.1 Laden und Senden von Internetdaten](#91-laden-und-senden-von-internetdaten)
      - [9.1.1 Daten Lesen](#911-daten-lesen)


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

Die Funktion `Fraction()` aus dem Modul `fractions` beitet verschiedene Möglichkeiten, einen Bruch zu erzeugen. Genauer gesatzt, handelt es sich bei `Fraction()` um den Konstruktor der Klasse `Fraction`. Damit wird eine Instanz (ein Objekt) der Klasse erzeugt und eine Referenz auf dieses Objekt zurückgeliefert. Klassen, Instanzen, Konstruktoren und andere Begriffe aus der objektorientierten Programmierung werden in Kapitel 6 genauer erkläutert.

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

Es wird die Zahl 1.84953 untersucht. Sie entspricht dem Bruch 184953/100000. Mithilfe der Methode `limit_denominator()` wird der Nenner auf die Zahl 100 begrenzt.

Dann wird der Bruch gesucht, der 
* einen Nenner mit dem maximal 100 hat und
* der Zahl 1,84953 am nächsten kommt.

Im vorliegenden Fall ist das der Bruch 172/93. Er hat den Wert 1,8494623655913978 und kommt der ursprünglichen Zahl recht nahe. Der relative Fehler zwischen diesem Wert und der untersuchten Zahl beträgt nur 3,65684301429 x 10^-5.

Er wird mithilfe der eingebauten Funktion `abs()` zur Berechnung des Betrags ermittelt. Beim Betrag handelt es sich um den Absolutwert einer Zahl, also der Zahl ohne das Vorzeichen.

Sollten Sie die Methode `gcd()`zur Ermittelung des größten gemeinsamen Teilers vermissen: Seit Python 3.5 gehört sie zum Modul `math` und wird im Modul `fractions` als veraltet bezeichnet.

### 4.2 Zeichenketten

Zeichenketten sind Sequenzen von einzelnen Zeichen - also Texte. Auch andere Objekttypen gehören zu den Sequenzen. Anhand von Zeichenketten folgt eine Einführung in die Sequenzen.

#### 4.2.1 Eigenschaften

Zeichenketten (Strings) sind Objekte des Datentyps `str`. Strings bestehen aus mehreren Zeichen oder Wörtern. Sie werden gekennzeichnet, indem man sie in einfache, doppelte oder dreimal doppelte Hochkommata setzt.

```py
t1 = "Hallo Welt"
t2 = 'Auch das ist eine Zeichenkette' 
t3 = """Diese Zeichenkette
        steht in
        mehreren Zeilen"""
t4 = 'Hier sind "doppelte Hochkommata" gespeichert'
print("Bittegeben Sie einen Text ein")
t5 = input()

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)
print("t5:", t5)

print("Typ:", type(t1))
```

```
[...]
t3: Diese Zeichenkette
steht in
mehreren Zeilen
[...]
Typ: <class 'str'>
```

Die Zeichenkette `t1` ist in doppelte Hochkommata, die Zeichenkette `t2` in einfachen Hochkommata und die Zeichenkette `t3` darf sich über mehrere Zeilen strecken. Sie wird auch so ausgegeben.

Die Zeichenkette `t4` verdeutlicht den Vorteil, den das Vorhandensein mehrerer Alternativen bietet: Die doppelten HOchkommata sind hier Bestandteil des TExts und werden auch ausgegeben.

Die eingebaute Funktion `input()` ist bereits bekannt. Sie dient zur Eingabe von Zeichenketten und liefert als Ergebnis den eingegebenen Text zurück. Er wird in der Variablen `t5` gespeichert. Mithilfe der Funktion `type()` wird für die Zeichenkette `t1` der Objekttyp ausgegeben.

#### 4.2.2 Operatoren

Die Operatoren `+` und `*` dienen zur Verkettung mehrer Sequenzen bzw. Vervielfachung einer Sequenz. Mithilfe des OPerators `in`stellen Sie fest, ob ein bestimmtes Element in einer Sequenz enthalten ist. Betrachten Sie das folgende Beispiel für diese Operatoren, angewendet für Strings:

```py
# Operatoren + und *
t1 = "Teil 1"
t2 = "Teil 2"
tgesamt = t1 + ", " + t2

t3 = "-ooo-"
t4 = "***"
tlinie = t4 + t3*3 + t4

print(tgesamt)
print(tlinie)

# Operator in
tname = "Robinson Crusoe"
print("Text:", tname)

if "b" in tname:
    print("b: ist enthalten")

if "p" not in tname:
    print("p: ist nicht enthalten")
```

Die Zeichenkette `tgesamt` wird mithilfe des Verkettungsoperators `+` aus drei Teilen zusammengesetzt: den beidne Zeichenketten `t1` und `t2` und dem Text mit KOmma und Leerzeichen.

Die Zeichenkette `tlinie` wird mithilfe des Verkettungsoperators `+` und des Vervielfachungsoperators `*` zusammengesetzt. Dabei wird der Ausdruck `"-ooo-"` dreimal hintereinander in `tlinie` gespeichert.

Mithilfe des Operators `in`wird festgestellt, ob das Element `b` in der Sequenzenthalten ist. Der logsiche Operator `not` dient (zusammen mit `in`) der Feststellung, ob das Element `p` nicht enthalten ist.

#### 4.2.3 Operationen
Teilbereiche von Sequenzen werden als `Slices` bezeichnet. Der Einsatz von Slices wird am Beispiel eines Strings verdeutlicht. Auf die gleiche Art und Weise sind Slices auch auf andere Sequenzen anwendbar.

Als Beispiel für eine Sequenz wird wiederum die Zeichenkette `Robinson Crusoe` in der Variablen `tname` gespeichert. Tabelle 4.1 stellt die einzelnen Elemente von `tname` mit dem zugehörigen index dar. Die Nummerierung beginnt bei 0; alternativ können Sie auch eine negative Nummeriung nutzen, die mit 1 endet (siehe unterste Zeile der Tabelle).

|Index  |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|
|-----  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Element|R|o|b|i|n|s|o|n| |C|r|u|s|o|e|
Negativer Index | 15 | 14|13|12|11|10|9|8|7|6|5|4|3|2|1|

Ein Slice wird durch die Angabe eines Bereichs in eckigen Klammern (`[]`) hinter der sequenziellen Variablen erzeugt. Er beginnt mit einem Start-index, gefolgt von einem Doppelpunkt und einem Endindex. Ein Slice, der nur aus einem einzelnen Zeichen besteht, wird druch die Eingabe eines einzelnen Index erzeugt.

Die eingebaute Funktion `len()` ermittelt die Anzahl der Elemente einer sequenz. IM Fall eines Strings spricht man hierbei auch von der Länge der Zeichenkette.

```py
# Beispielsequenz, hier Zeichenkette
tname = "Robinson Crusoe"
print("Text:", tname)

# Anzahl der Elemente
lg = len(tname)
print("Anzahl der Elemente:", lg)

# Teilbereiche, Elemente
ts = tname[5:8]
print("[5:8]:", ts)
ts = tname[:8]
print("[:8]:", ts)
ts = tname[9:]
print("[9:]:", ts)
ts = tname[9]
print("[9]:", ts)
ts = tname[9:-3]
print("[9:-3]:", ts)

# Elemente einzeln
for zeichen in tname[5:8]:
    print(zeichen)
```

Die LÄnge der Sequenz, aslo die Anzal der Zeichen in der Zeichenkette, wird mithilfe der Funktion `len()` ermittelt. Es folgen einige Slices:
* Slice [5:8]: Der Bereich erstreckt sich von dem Element, das durch den Startindex gekennzeichnet wird, bis vor das Element, das durch den Endindex gekennziechnet wird. Ergebnis: son
* Slice [:8]: Wenn der Startindex weggelassen wird, beginnt der Bereich bei 0. Ergebnis: Robinson
* Slice [9:]: Wenn der Endindex weggelassen wird, endet der Bereich am Ende der Zeichenkette. Ergebnis: Crusoe
* Slice [9]: Wird nur ein Index angegeben, besteht der Bereich nur aus einem einzelnen Element. C
* Slice [9:-3]: Wird ein Index mit einer negativen Zahl angegeben, wird vom Ende aus gemessen, beginnend bei 1. Cru

Eine for-Schleife kann genutzt werden, um eine ganze Zeichenkette oder einen Teil der Zeichenkette Zeichen für Zeichen durchzugehen.

Anhand des nachfolgenden Beispiels sehen Sie, dass Strings nicht veränderbar sind. Es können keine einzelnen Zeichen oder Bereiche aus Strings durch andere Zeichen oder Slices ersetzt werden:

```py
tname = "Robinson Crusoe"

try:
    tname[3] = "e"
except:
    print("fehler")

try: 
    tname[3.5] = "el"
except:
    print("fehler")
```

Die einzige Möglichkeit zur Veränderung eines Strings ist die Erzeugung eines neuen String-Objekts.

#### 4.2.4 Funktionen

Neben der eingebauten funktion `len()` gibt es für Objekte des Datentypes `str` eine REihe von nützlichen Funktionenen zur Bearbeitung udn Analyse von Zeichenketten. Anhand des folgenden Beispiels werden einige FUnktionen zum Suchen von Teiltexten verdeutlicht:

```py
test = "Das ist ein Beispielsatz"
print("Text:", test)

# Anzahl der Suchtexte

such = "ei"
anz = test.count(such)
print("count: Der String", such, "kommt", anz, "mal vor.")

# Erste Position des Suchtextes 
anfpos = test.find(such)
print("find 1: Zum ersten am lan Position", anfpos)

# Weitere Position des Suchtextes
nextpos = test.find(such, anfpos+1)
print("find 2: Ein weiteres Mal an Position", nextpos)

# Letzte Position des Suchtextes
endpos = test.rfind(such)
print("rfind: Zum letzten Mal an Position", endpos)

# Suchtext nicht gefunden
such = "am"
pos = test.find(such)
if pos == -1:
    print("find 3:", such, "wurd nicht gefunden")
else:
    print("find 3:", such, "an Position", pos, "gefunden")

# Ersetzen von Text

test = test.replace("ist", "war")
print("replace", test)
```

Die Funktion `count()` ergibt die Anzahl der Vorkommen eines Suchtexts (hier in der Variablen `such`) innerhalb des analysierten Texts.

Die Funktion `find()` ergibt die Position, an der ein Suchtext innerhalb eines analysierten Texts vorkommt. Zur Erinnerung: Das erste Element einer Sequenz hat die POsition 0.

Bei der Funktion `find()` können Sie optional einen zweiten Parameter angeben. Dieser Parameter bestimmt die Position, ab der gesucht wird. Im vorliegenden Fall ist das die Position des Zeichens hinter der ersten Fundstelle. Diese Technik wird häufig verwendet, um mithilfe einer Schleife alle Vorkommen eines Suchtexts zu finden.

Die Funktion `rfind()` ergibt die Position des letzten Vorkommens des Suchtexts innerhalb des analysierten Texts. Falls der gesuchte Text nicht vorkommt, liefert `find()` bzw. `rfind()` den Wert `-1` zurück.

Die Funktion `replace()` ersetzt einen gesuchten Teiltext durch einen anderen und liefert den geänderten Text zurück.

Das nachfolgende Beispiel zeigt hauptsächlich Funktionen zum Zerlegen von Texten in Teiltexte:

```py
# Beispielsatz
test = "Das ist ein Beispielsatz"
print("Test:", test)

# Beginn, Ende

if test.startswith("Das"):
    print("Text beginnt mit Das")

if not test.endswith("Das"):
    print("Text endet nicht mit Das")

# Zerlegung

teile = test.partition("ei")
print(teile)
print("vor der 1. Teilung:", teile[0])
print("nach der 1. Teilung:", teile[2])

teile = test.rpartition("ei")
print("vor der 2. Teilung:", teile[0])
print("nach der 2. Teilung:", teile[2])

# Zerlegung in Liste
wliste = test.split()
print(wliste)
for i in range(0,3):
    print("Element:", i, "-", wliste[i])
```

Mithilfe der Funktion `startswith()` und `endswith()` untersuchen Sie, ob eine Zeichenkette mit einem bestimmten TExt beginnt oder endet. Beide Funktionen liefern einen Wahrheitswert (`true` or `false`), daher kann der Rückgabewert direkt als Bedingung genutzt werden.

Die Funktion `partition()` und `rpartition()` zerlegen eine Zeichenkette in einzelne Teile anhand eines TEilungstexts. Diese Teile werden in einem Tupel geliefert.
* Das erste Element des Tupels (element 0) enthält den Text bis zum Teilungstext, 
  das zweite Element (element 1) enthält den teilungstext selbst und 
  das dritte Element (element 2) enthält den Text hinter dem Teilungstext.
* Die Funktion `partition()` sucht den Teilungstext ausgehend vom Beginn der Zeichenkette, die Funktion `rpartition()` sucht ihn ausgehend vom Ende der Zeichenkette.
* Wird der Teilungstext nicht gefunden, steht die gesamte Zeichenkette im ersten Element des Tupels.
* Weiter Informationen zu den Tupeln erhalten sie in Abschnitt 4.4.
  
Die Funktion `split()` zerlegt einen Text in einzelne Teile, die in einer Liste gespeichert werden. Das Leerzeichen wird dabei als Trennzeichen angesehen. Zur Verduetlichung werden im voranliegenden Beispiel die drei ersten Elemente der Liste zusammen mit der laufenden Nummer innerhalb der Liste ausgegeben (weitere Informationen zu Listen gibt es in Abschnit 4.3).

Falls sie bei der Funktion `split()` ein anderes Trennzeichen verenden möchten, wie z. B. das Semikolon oder das Rautezeichen, übergeben Sie dieses Trennzeichen als Parameter an die FUnktion, zB.: `split(";")`.

#### 4.2.5 Umwandlung einer Zeichenkette in eine Zahl

Enthält eine Zeichenkette eine Zahl, etwa eine vom Benutzer eingegebene Zeichenkette oder einen Kommandozeilenparameter (siehe Abschnitt 5.11, Parameter der Kommandozeile), muss diese Zeichenkette zunächst konvertiert werden.

Zur Umwandlung in eine ganze Zahl oder in eine Zahlmit Nachkommastellen dienen die beiden Funktionen `int()` bzw. `float()`. Anschließend kann mit deiser Zahl gereichnet werden.

Das folgende Beispiel verdeutlicht den Unterschied in der Behandlung von Zahlen un Strings:

```py
# Erste Zeichenkette
x = "15.3"

ergebnis = x * 2
print(ergebnis)

x = float(x)
ergebnis = x * 2
print(ergebnis)

# Zweite Zeichenkette
x = "17"
ergebnis = x * 2
print(ergebnis)

x = int(x)
ergebnis = x * 2
print(ergebnis)
```
In der ersten Zeichenkette steht `15.3`. Wird diese Zeichenkette mit 2 *multipliziert*, ergibt sich die Zeichenkette `15.315.3`. Wird die Zeichenkette dagegen mithilfe von `float()` in eine Zahl mit Nachkommasetellen verwandelt, kann mit ihr gerechnet werden. Eine Multiplikation mit 2 ergibt mathematisch korrekt die Ausgabe `30.6`.

Ähnlich sieht es bei der Umwandlung in eine ganze Zahl aus. In der zweiten Zeichenkette steht `17`. Wenn diese Zeichenkette mit 2 *multipliziert*  wird, ergibt sich die Zeichenkette `1717`. Wird die Zeichenkette dagegen mithilfe von `int()` in eine ganze Zahl verwandelt, aknn mit ihr gerechnet werden. Eine Multiplikation mit 2 ergbit in diesem Fall mathemathisch korrekt 34.

Falls versucht wird, eine Zeichenkette, die keine gültige Zahl enthält, in eine Zahl umzuwandeln, tritt eine Ausnahme auf. Daher sollten Sie die Umwandlung von Benutzereingaben oder KOmmandzeilenparametern in eine Ausnahmebehandlung einbetten:

```py
# Fehler abfangen
x = "15.3p"

try:
    x = float(x)
    print(x*2)
except:
    print("Zeichenkette kann nicht umgewandelt werden")
```

In der Zeichenkette steht eine nicht gültiges Zeichen(hier das `p`). Dies führt zu einer Ausnahme, und es erscheint eine Fehlermeldung.

#### 4.2.6 Umwandlung einer Zahl in eine Zeichenkette

Muss eine Zahl in eine Zeichenkette umgewandelt werden, etwa zur Ausgabe der Zahl in eine Datei (siehe 8.3.1 - Sequenzielles Schreiben) könnnen Sie die FUnktion `str()` verwenden.
```py
a = 23
b = 7.5
c = a + b

# 1. Ausgabe
print(a, "+", b, "=", c)

# 2. Ausgabe
print(str(a) + "+" + str(b) + "=" + str(c))
```
```
23 + 7.5 = 30.5
23+7.5=30.5
```

Die erste Ausgabe erfolgt wie gewohnt. Sie setzt sich aus den einzelnen Variablen und den verbindenden TExten zusammen. Nach jedem Teil der Ausgabe wird automatisch ein  Leerziechen eingefügt.

Für die zweite Ausgabe werden die Zahlen zunächst mithilfe der Funktion `str()` in Zeichenketten umgewandelt. Abschließend werden die verschiedenen Zeichenketten mit dem Verkettungsoperator `+` verbunden. In der Ausgabe kommen keine Leerzeichen mehr vor.

Eine weiter Möglichkeit zur Gestaltung von Ausgaben zeige ich Ihnen im Abschnitt 5.2.2, Formatierung mit String-Literalen.

#### 4.2.7 Datentyp "bytes"

Objekte des Datentyps `bytes` bestehen aus Zeichen, deren Zeichencode im Bereich von 0 bis 255 liegt. Jedes Zeichen kann mithilfe eines Bytes gespeichert werden. Sie können `bytes`-Objekte mithilfe von Byte-LIteralen erzeugen oder mithilfe der eingebauten FUnktion `bytes()`. Im Unterschied zu `bytes`-Objekten werden die üblichen Zeichenketten, also `str`-Objekte aus Unicode-Zeichen gebildetet.

Byte-Literale beginnen mit einem `b` oder einem `B`. Dies ist bei der Eingabe oder Zuweisung zu beachten. Bei der Ausgabe wird ein `b` vorangestellt.

```py
# Datentyp str
st = "Hallo"
print(st, type(st))

# Datentyp bytes
by = b'Hallo'
print(by, type(by))

# Umwandlung von str in bytes
by = bytes("Hallo", "UTF-8")
print(by, type(by))

# Umwandlung von bytes in str
by = b'Hallo'
st = by.decode()
print(st, type(st))
```


Zunächst werden ein `str` Objekt und ein bytes Objekt per Zuweisung erzeugt und asugegeben. Beachten Sie beim Byte Literal das vorangestellt b, zu Umwanldung eines str Objekts in ein bytes Objekt wird die eingebaute Funktion `bytes()` genutzt. Dabei wird die Codierung des `str`-Objekts angegeben, hier UTF-8. Zur Umwnadlung eines bytes-Objekts in ein str-Objekt wird die Methode `decode()` verwendet.

### 4.3 Listen

Eine Liste ist eine Sequenz von Objekten in ihrer allgemeinsten Form. Sie kann Elemente utnerschiedlichen Objekttyps enthalten. Eine Liste bietet vielfältige Möglichkeiten, u. a. die Funktionalität von ein- und mehrdimensionalen Feldern (Arrays), wie man sie aus anderen Programmiersprachen kennt.

#### 4.3.1 Eigenschaften

Eine Liste ist im Gegensatz zu einem String veränderbar. Davon abgesehen ist ein String, vereinfacht gesagt, nur eine Liste zur Speicherung von einzelnen Zeichen. Einige Beispiele für Listen:

```py
# Liste von Zahlen 
z = [3,6,12.5,-8, 5.5]
print (z)       # gesamt Liste
print(z[0])     # ein Element
print(z[0:3])   # Slice

# Liste von Zeichenketten
s = ["Hamburg", "Augsburg", "Berlin"]
print(s)

# Anzahl Elemente
print("Anzahl:", len(s))
```

```
[3, 6, 12.5, -8, 5.5]
3
[3, 6, 12.5]
['Hamburg', 'Augsburg', 'Berlin']
Anzahl: 3
```

Listen werden innerhalb von eckigen Klammern angegeben. Darin listen Sie die einzelnen Elemente durch KOmmata getrennt auf.

Die Variable `z` enthält eine Liste von Zahlen. Wie bei STrings ermitteln Sie ein Einzelnes Element einer LIste durch Angabe eines Index (hier z[0]). Einen Teilbereich erhalten Sie mithilfe eines Slices (hier: z[0:3]).

Die Variable `s` enthält eine Liste von Zeichenketten. Die Länge einer Sequenz, also auch einer Liste, ermitteln Sie mit der Funktion `len()`. 

Im nachfolgenden Beispiel sehen Sie eine mehrdimensionale Liste. Eine LIste kann Elemente unterschiedlicher Objekttypen enthalten. Diese Elemente können wiederum Listen sein.

```py
# mehrdimensionale Liste, utnerschiedliche Objekte
x = [["Paris", "Fr", 3500_000], ["Rom", "It", 4200_000]]
print(x)

# Teilliste
print(x[0])

# einzelne Elemente
print(x[0][0], "hat", x[0][2], "Einwohner")
print(x[1][0], "hat", x[1][2], "Einwohner")

# Teile von Elementen
print(x[0][1][:1])
```
```
[['Paris', 'Fr', 3500000],['Rom', 'It', 4200000]]
['Paris', 'Fr', 3500000]
Paris hat 3500000 Einwohner
Rom hat 4200000 Einwohner
F
```

Die Variable `x` enthält zwei Listen. Innerhalb jeder Teilliste (oder eingebetteten Liste) sind zwei Zeichenketten und eine Zahl gespeichert. Eine oder mehrere eingebettete Listen erreichen Sie über die Angabe eines einzelnen Index oder eines Slices.

Einzelne Elemente von eingebetteten LIsten erreichen Sie durch Angabe mehrer Indizes oder Slices. Die erste Angabe in eckigen Klammern kennzeichnet hier die eingebettete Liste mit dem Index 0, die zweite Angabe in eckigen KLammern kennzeichnet das Element mit dem Index 2 innerhalb dieser eingebetteten Liste.

Einzelne Elemente der Liste sind wiederum Sequenzen, falls es sich um Zeichenketten handelt. Daher können Sie z. B. das erste Zeichen des Elements `x[0][1]` miothilfe von `x[0][1][:1]` ermitteln.

#### 4.3.2 Operatoren

Die Operatoren `+` und `*` können Sie bei Sequenzen, also auch bei Listen zur Verkettung oder Vervielfachung einsetzen. Außerdem werden Listen, zusammen mit dem Operator `in` häufig zur Erstellung einer `for` Schleife genutzt. Ein gemeinsames Beispiel für die Beiden genannten Fälle:

```py
# zwei Listen
fr = ["Paris", "Lyon", "Marseille"]
it = ["Rom", "Pisa"]

# Listen zusammensetzen
stadtliste = fr + it * 2
print(stadtliste)

# Liste teilweise durchlaufen
for stadt in stadtliste[3:6]:
    print(stadt)
```

```
['Paris', 'Lyon', 'Marseille', 'Rom', 'Pisa', 'Rom', 'Pisa']
Rom
Pisa
Rom
```

In den beiden Listen `fr` und `it` werden einige Zeichenketten gespeichert.

Die Liste `stadtliste` ist eine neue Liste. Sie enthält die Elemente der Liste `fr` und zweimal nacheinander die Elemente der liste `it`. Sie wird als vollständige Liste ausgegeben.

Anschließend wird ein Teil der Liste mithielfe einer `for`-Schleife und eines Slices Element für Element ausgegeben.

#### 4.3.3 Funktionen und Operationen

Listen können, im Gegensatz zu Strings, verändert werden. Sie können aber nicht nur Elemente oder Teilbereche auswählen, sondern auch:
* Elemente oder Teilbereiche am Ende oder am Anfang hinzufügen
* vorhandene Elemente oder Teilbereiche verändern
* Elemente oder Teilbereiche innerhalb der Liste einfügen
* Elemente oder Teilbereiche löschen

Falls Sie ein einzelnes Element durch einen Teilbereich ersetzen, wird eine neue eingebettete Liste erzeugt. Es folgt ein Programm mnit einigen Listenoperationen, die Elemente oder Teilbereiche betreffen. Das Schlüsselwort `del` dient zum Löschen:

```py
# Originalliste

fr = ["Paris", "lyon", "Marseille", "Bordeaux"]
print("Original:")
print(fr)

# Ersetzen eines Elements durch ein Element
fr[2] = "Lens"
print("Element ersetzt:")
print(fr)

# Ersetzen eines Teilbereiches durch eine Liste
fr[1:3] = ["Nancy", "Metz", "Gap"]
print("Teil ersetzt:")
print(fr)

# Entnehmen eines Teilbereiches
del fr[3:]
print("Teil entnommen:")
print(fr)

# Ersetzen eines Elements durch eine Liste
fr[0] = ["Paris-Nord", "Paris-Sud"]
print("Element durch Liste ersetzt:")
print(fr)
```

```
Original:
['Paris', 'lyon', 'Marseille', 'Bordeaux']
Element ersetzt:
['Paris', 'lyon', 'Lens', 'Bordeaux']
Teil ersetzt:
['Paris', 'Nancy', 'Metz', 'Gap', 'Bordeaux']
Teil entnommen:
['Paris', 'Nancy', 'Metz']
Element durch Liste ersetzt:
[['Paris-Nord', 'Paris-Sud'], 'Nancy', 'Metz']
```

Die Originalliste, bestehend aus vier Zeichenketten, wird erstellt. Ein einzelnes Element wird durch eine andere Zeichenkette ersetzt. Ein Teilbereich wird durch eine Liste ersetzt. Ein Teilbereich wird mithilfe von `del` aus der Liste gelöscht. Ein Element wird durch eine Lsite ersetzt; dadruch wird eine neue eingebettete Liste erzeugt.

Im nachfolgenden Programm wird eine Reihe von weiteren Funktionen zur Analyse und Bearbeitung von Listen verdeutlicht:

```py
# Originalliste
fr = ["Paris", "Lyon", "Marseille"]
print("Original:")
print(fr)

# Einsetzen eines Elements
fr.insert(0, "Nantes")
print("Nach Einsetzen:")
print(fr)

# Sortieren der Elemente
fr.sort()
print("Nach Sortierung der Elemente")
print(fr)

# Umdrehen der Liste
fr.reverse()
print("Nach Umdrehen:")
print(fr)

# Entfernen eines Elements
fr.remove("Nantes")
print("Nach Entfernen:")
print(fr)

# Ein Element am Ende hinzufügen
fr.append("Paris")
print("Ein Element hinzu:")
print(fr)

# Anzahl bestimmter Elemente
print("Anzahl Elemente Paris:", fr.count("Paris"))

# Suchen bestimmter Elemente
print("Erste Position Paris:", fr.index("Paris"))
```
```
Original:
['Paris', 'Lyon', 'Marseille']
Nach Einsetzen:
['Nantes', 'Paris', 'Lyon', 'Marseille']
Nach Sortierung der Elemente
['Lyon', 'Marseille', 'Nantes', 'Paris']
Nach Umdrehen:
['Paris', 'Nantes', 'Marseille', 'Lyon']
Nach Entfernen:
['Paris', 'Marseille', 'Lyon']
Ein Element hinzu:
['Paris', 'Marseille', 'Lyon', 'Paris']
Anzahl Elemente Paris: 2
Erste Position Paris: 0
```

Die Originalliste, bestehend aus drei Zeichenketten, wird erstellt. Anschließend wird ein Element mit der Funktion `insert()` an Position 0 eingefügt, also zu Beginn der Liste.

Die Liste wird mit der Funktion `sort()` intern sortiert. Falls es sich um eine Liste von Zeichenketten handelt, wird alphabetisch sortiert. Eine Liste von Zahlen wird nah der Größe sortiert. Bei anderen listenelementen oder bei gemsichen Listen ist der Einsatz der Funktion `sort()` nur bedingt sinnvoll.

Die Liste wird mit der Funktion `reverse()` intern umgedreht.

Ein bestimmtes Element (hier: Nantes) wird innerhalb der Liste gesucht. Falls es vorhanden ist, wird das erste Vorkommen dieses Elements mit der Funktion `remove()` gelöscht. Falls es nicht vorhandne ist, wird eine Ausnahme ausgelöst.

Ein Element wird am ende der Liste mit `append()` angefügt.

Die Anzahl der Vorkommen eines bestimmten Elements (hier `Paris`) wird mit der Funktion `count()` ermittelt.

Die POsition des ersten Vorkommens eines bestimmten Elements (hier: `Paris`) wird mit der Funtion `index()` ermittelt. Ist das Element nicht vorhanden, wird eine Ausnahme ausgelöst.

### 4.4 Tupel

In diesem Abschnitt werden Tupel und ihre besonderen Eigenschaften sowie Operationen mit Tupeln erläutert.

#### 4.4.1 Eigenschaften

Der Unterschied zwischen einem Tupel und einer Liste: Eine Tupel kann nicht verändert werden. Ansonsten gelten die gleichen Regeln, und es können die gleichen Operationen und Funktionen auf Tupel wie auf Listen angewendet werden, sofern sie keine Veränderung des Tupels hervorrufen.

#### 4.4.2 Operationen

Einige Beispiele und Besonderheiten:
```py
# Tupel mit und ohne Klammer
z = (3, 6, -8, 5.5)
print("Tupel 1:", z)

z = 6, 8, -3
print("Tupel 2:", z)

# mehrdimensionales Tupel, unterschiedliche Objekte
x = (("Paris", "Fr", 3500000),["Rom", "It", 4200000])
print("mehrdimensionales Tupel")
print(x)

# Ersetzen
try:
    x[0][0] = "Lyon"    # nicht erlaubt, weil Tupel
except:
    print("Fehler")

x[1][0] = "Pisa"        # erlaubt, weil Liste
print("Listenelement ersetzt:", x[1]) 

# Tupel bei For-Schleife:
for i in 4,5, 12:
    print("i:", i)

# Zuweisung mit Tupel
x,y = 2,18

print("x:", x, "y:", y)
```

Tupel können mit runden Klammern (statt eckiger Klammern bei Listen) oder ganz ohne Klammern erzeugt werden. Sie können gleichzeitig Zahlen, Zeichenketten und andere Objekte enthalten.

Durch Einbettung können sie mehrdimensionale Tupel erzeugen. Hier ist dies das Tupel `x`, bestehend wiederrum aus einem Tupel und einer Liste.

Die versuchte Veränderung des inneren Tupels erzeugt eine Ausnahme. Erlaubt ist dagegen die Veränderung der inneren Liste, die in ein Tupel eingebettet ist (hier für `x[1][0]`).
Die `for`-Schleifen in diesem Buch werden meist mithielfe von Tupeln geschrieben, ohne dass dieser Begriff bisher gesondert erwähnt wurde.

Mithilfe eines TUpels können Sie mehrere Werte gleichzeitig zuweisen. Im vorliegenden Beispiel werden die Werte 2 und 18 den Einzelvariablen x bzw. y zugewiesen. Mehr dazu folgt im nächsten Abschnitt.

#### 4.4.3 Tupel entpacken

Innerhalb eines Tupels sind mehrere unveränderliche Werte gespeichert. Mithilfe eines Tupels kann eine mehrfache Zuweisung erfolgen. Dabei werden in einer Anweisung gleichzeitig mehreren Veriablen Werte zugewiesen, was Ihnen Schreibarbeit erspart. Hier sind einige Besonderheiten zu beachten, die das folgende Programm verdeutlicht:

```py
# 1: Mehrfache Zuweisung
x, y, z = 3, 5.2, "Hallo"
print("Mehrfache Zuweisung:", x, y, z)

# 2: Auswirkungen erst danach
a = 12
b = 15
c = 22
a, b, c, = c, a, a+b
print("Auswirkung:", a, b, c)

# 3: Verpacken eines Tupels
p = 3, 4
print("Verpackt:", p)

# 4 Entpacken eines Tupels
m, n = p
print("Entpackt: m:", m, "n:", n)

# 5 Falsche Zuweisung eines Tupels
try:
    s, t = 3, 4, 12
except:
    print("Fehler")

# 6: Rest in Liste
print()
x, *y, z = 3, 5.2, "hallo", 7.3, 2.9
print(x)
print(y)
print(z)

# kein Rest, Liste leer
print()
x, *y, z = 3, 5.2
print(x)
print(y)
print(z)
```

```
Mehrfache Zuweisung: 3 5.2 Hallo
Auswirkung: 22 12 27
Verpackt: (3, 4)
Entpackt: m: 3 n: 4
Fehler

3
[5.2, 'hallo', 7.3]
2.9

3
[]
5.2
```

Zu 1: Bei der mehrfachen Zuweisung erhält die Variable `x` den Wert `3`, die Variable `y` den Wert `5.2` und die Variable `z` den wert `hallo`. Die Anweisungen auf drei Zeilen verteilt würde dasselbe bewirken, aber drei Programmzeilen statt einer beanspruchen.

Zu 2: Die Änderung eines Variablenwerts hat keine Auswirkungen innerhalb derselben Mehrfachzuweisung. Die Variable `a` erhält den alten (und neuen) Wert von `c`(=22), die Variable `b` den alten Wert von `a` und die Variable `c` die Summe der alten Werte von `a` und `c`. Die Änderung der Variblen wirkt sich erst in der nächsten Anweisung aus. Die folgenden Anweisugnen hätten zu ganz anderen Ergebnissen geführt, da a und b bereits neue werte erhalten hätten.

Zu 3: Steht auf der linken Seite der Zuweisung nur eine Variable (im Beispiel p), während auf der rechten Siete mehrere Werte oder Ausdrücke stehen (im Beispiel 3 und 4), handelt es sich um die Erzeugung(Verpackung) eines Tupels.

Zu 4: Ein Tupel kann wieder entpackt werden. Dabei sollte die Anzahl der Variablen auf der linken Seite der Zuweisung der Anzahl der Elemente des Tupels auf der rechten Seite entsprechen.

Zu 5: Es werden mehrere Werte zugewisen, aber es steht nicht die gleiche Anzahl an Variablen oder nur eine einzelne Variable zur Verfügung. Es erfolgt eine Ausnahme, da die Werte weder einen Tupel noch in einer einzelnen Variablen eindeutug zugeordnet werden können.

Zu 6: Falls die Anzahl der Tupelwerte nicht mit der Anzahl der Variablen übereinstimmt, können Sie einer der Variablen das Zeichen `voranstellen. In dieser gesternten (engl: starred) Variablen wird der Rest des Tupels gespeichert, der nicht einer einzelnen Variablen zugewiesen werden kann. Im Beispiel werden der erste und der letzte Wert einer einzelnen Variablen zugewiesen. Die mittleren Werte landen als Liste in der mittleren Variablen.

### 4.5 Dictionarys

Ein Dictionary ist mit einem Wörterbuch zu vergleichen. In einem Wörterbuch finden Sie unter einem Schlüsselbegriff die zugeordnete Information. So steht etwa in einem english-deutsch Wörterbuch unter dem Eintrag house der zugeordnete deutsche Begriff Haus.

#### 4.5.1 Eigenschaften

In Python stellen Dictionarys veränderliche Objekte dar und bestehen aus mehreren Paaren. Jedes Paar besteht aus einem eindeutigen schlüssel und einem zugeordneten Wert. Über den Schlüssel greifen Sie auf den Wert zu. Als Schlüssel werden meistens Strings verwendet, es können aber auch andere unveränderliche Objekte (Zahlen, Tupel) benutzt werden. Die Reihenfolge der Schlüssel bei der Ausgabe eines Dictionarys wird durch die Reihenfolge beim Einfügen bestimmt.

Im folgenden Beispiel werden die Namen und Altersangaben mehrerer Personen in einem Dictionary erfasst und bearbeitet. Der Name dient als Schlüssel. Darüber kann auf die Altersangabe (also auf den Wert des Schlüssels) zugegriffen werden.

```py
# Erzeugung eines Dictionarys
alter = {"Peter":31, "Julia":28, "Werner":35}
print(alter)

# Ersetzen eines Werts
alter["Julia"] = 27
print(alter)

# Ein Element hinzu
alter["Moritz"] = 22
print(alter)

# Ausgabe
print("Julia:", alter["Julia"])
```
```
{'Peter': 31, 'Julia': 28, 'Werner': 35}
{'Peter': 31, 'Julia': 27, 'Werner': 35}
{'Peter': 31, 'Julia': 27, 'Werner': 35, 'Moritz': 22}
Julia: 27
```

Es wird das Dictionary `alter` mit drei Informationspaaren erzeugt und ausgegeben. Dictionarys werden mithilfe von geschweiften Klammern (`{}`) erzeugt. Die Paare werden durch Kommata voneinander getrennt, ein Paar wird in der folgenden Form notiert: `Schlüssel:Wert`.

Auf ein einzelnes Element greifen Sie über den Schlüssel in eckigen Klammern zu. Dies wird hier für Zuweisung und Ausgabe genutzt.

Elemente sind veränderlich. In diesem Beispiel wird die Altersangabe von `"Julia"` verändert. Es können auch Elemente hinzugefügt werden. Hier wird dem Dictionary das Paar `"Moritz":22` hinzugefügt, da bisher kein Element mit dem Schlüssel `"Moritz"` vorhanden ist.

#### 4.5.2 Operatoren und Funktionen

Es gibt eine Reihe von Operatoren und Funktionen zur Bearbeitung von Dictionarys. Einige werden im folgenden Programm verdeutlicht:

```py
# Erzeugung
alter = {"Peter":31, "Julia":28, "Werner":35}
print(alter)

# Element enthalten?
if "Julia" in alter:
    print(alter["Julia"])

# Entfernen eines Elements
del alter["Julia"]

# Element enthalten?
if "Julia" not in alter:
    print("Julia ist nicht enthalten")

# Anzahl Elemente
print("Anzahl:", len(alter))

# Aktualisierung mit zweitem Dictionary
ualter = {'Moritz': 18, 'Werner': 29}
alter.update(ualter)
print(alter)
print(ualter)
```

```
{'Peter': 31, 'Julia': 28, 'Werner': 35}
28
Julia ist nicht enthalten
Anzahl: 2
{'Peter': 31, 'Werner': 29, 'Moritz': 18}
```

Ein einzeles Element löschen Sie mithilfe de Schlüsselworts `del` aus der Liste. Die Existenz eines Elements prüfen Sie mithilefe des Operators `in`. Die Anzahl der Elemente ermitteln Sie mithilfe der Funktion `len()`.

Sie können Ein Dictionary mithilfe der Funktion `update()` mit den Intahlten eines anderen Ditionarys aktualisieren. Daei erhalten vorhandene Elemente einen neuen Wert, neue Elemente werden angehängt. Die beiden Dictionarys werden also zusammengeführt.

#### 4.5.3 Views

Die Funktionen `keys()`, `items()` and `values()` erzeugen sogenannte dynamische Views eines Dictionarys. Diese Views verändern sich unmittalbar, falls sie das zugeordnete Dictionary verändert. 


```py
# Erzeugung
alter = {"Peter":31, "Julia":28, "Werner":35}

# Werte
w = alter.values()
print("Werte/Values:", w)
print("Anzahl Werte:", len(w))
for x in w:
    print(x)
if 31 in w:
    print("31 ist enthalten")
alter["Peter"] = 41
if 31 not in w:
    print("31 ist nicht enthalten")
print()

# Keys
k = alter.keys()
print("Keys:", k)
print("Anzahl Keys:", len(k))
for x in k:
    print(x)
if "Werner" in k:
    print("Werner ist enthalten")
del alter["Werner"]
if "Werner" not in k:
    print("Werner ist nicht enthalten")
print()

# Items
i = alter.items()
print("Items:", i)
alter["Franz"] = 35

print("Anzahl Items:", len(i))
for x in i:
    print(x)
if ("Julia", 28) in i:
    print("Julia, 28 ist enthalten")
```
```
Werte/Values: dict_values([31, 28, 35])
Anzahl Werte: 3
31
28
35
31 ist enthalten
31 ist nicht enthalten

Keys: dict_keys(['Peter', 'Julia', 'Werner'])
Anzahl Keys: 3
Peter
Julia
Werner
Werner ist enthalten
Werner ist nicht enthalten

Items: dict_items([('Peter', 41), ('Julia', 28)])
Anzahl Items: 3
('Peter', 41)
('Julia', 28)
('Franz', 35)
Julia, 28 ist enthalten
```

Mithilfe der Funktion `values()` wird eine View der Werte des Dictionarys erzeugt. Den Inhalt der View können Sie mithilfe einer `for`-Schleife und des Operators `in` ausgeben. Sie können -w iederrum mithilfe des Operators `in` - prüfen, ob ein bestimmter Wert in der View exisitert.

Der Wert eines Dictionary_Elements wird verändert. Das wirkt sich sofort auf die zugehörige View aus. Diese muss also nicht neu erzeugt werden. Der ursprüngliche Wert des Dictionary-Elements wird nach der Änderung nicht mehr gefunden.

Mithilfe der Funktion `keys()` wird eine View der Keys des Dictionarys erzeugt. Den Inhalt der Views können Sie mithilfe einer `for`-Schleife und des Operators `in`ausgeben. Sie können - wiederum mithilfe des Operators `in` - prüfen, ob ein bestimmter Key in der View existiert.

Ein Dictionary-Element wird gelöscht. Dies wirkt sich soofrt auf die zugehörige View aus. Das ursprünglich vorhandene Dictionary-Element wird nach dem Löschen nicht mehr gefunden.

Mithilfe der Funktion `items()` wird eine View der Elemente des Dictionarys erzeugt. Den Inhalt der View können Sie mithilfe einer `for`-Schleife un `in` ausgeben. Sie können - wiederrum mit `in` - prüfen, bo ein bestimmtes Element, also ein Schlüssel-Wert-Kombination, in der View existiert.

#### 4.5.4 Vergleiche

Dictionarys können miteinander verglichen werden. Mithilfe des Operators == stellen Sie fest, ob alle Elemente, also alle Schlüssel-Wert-Kombinationen, übereinstimmen. Allerdings können Sie nicht prüfen, ob ein Dictionary kleiner oder grlößer als ein anderes Dicionary ist.

```py
# Zwei Dictionarys
alter1 = {"Julia":28, "Peter":30}
alter2 = {"Peter":30, "Julia":28}

# Vergleich

if alter1 == alter2:
    print("Gleich")

try:
    if alter1 < alter2:
        print("1 < 2")
    else:
        print("nicht 1 < 2")
except:
    print("Fehler")
```

Die beiden Dictionarys werden in unterschiedlicher Reihenfolge erstellt. Mithilfe von `==` wird festgestellt, dass sie dennoch den gleichen Inhalt haben. Der Vergleich mit < oder > ist nicht möglich.

### 4.6 Mengen, Sets

Mengen(engl: *sets*) unterscheiden sich von Listen und Tupeln dadurch, dass jedes Element nur einmal exisitiert. Außerdem sind Mengen ungeordnet, daher ist auch die Reihenfolge bei der Ausgabe eines gesamten Sets nicht festgelegt. Einzelne Elemente knnen also nicht anhand eines Slices bestimmt werden. Allerdings können Sie mit Mengen einige interessante Operatorionen durchführen, die aus der Mengenlehre bekannt sind.

### 4.6.1 Eigenschaften

Zum besseren Verständnis erzeugen wir ein Set und eine Liste und vergleichen einige ihrer Eigenschaften:

```py
# Liste
li = [8, 2, 5, 5, 5] 
print("Liste:", li)

# Set
s1 = set([8, 2, 5, 5, 5])
print("Set:", s1)
print("Anzahl:", len(s1))

# Elemente
for x in s1:
    print("Elemente:", x)
if 5 in s1:
    print("5 ist enthalten")
```
```
Liste: [8, 2, 5, 5, 5]
Set: {8, 2, 5}
Anzahl: 3
Elemente: 8
Elemente: 2
Elemente: 5
5 ist enthalten
```

Eine Menge erzeugen sie mithilfe der Funktion `set()`. Als einziger Parameter wird der Funktion `set()` eine Liste oder ein anderes Objekt übergeben, das durchlafen werden kann. Der Unterschied zur Liste: In der Liste kann ein Objekt mehrmals vertreten sein, in der Menge nur einmal.

Die Funktion `len()` liefert die Anzahl der Elemente der Menge. Mithilfe einer `for`-Schleife und des Operators `in` können Sie die Menge durchlaufen.
Wiederum mit `in` prüfen Sie, ob ein bestimmtes Element in der Menge enthalten ist.

#### 4.6.2 Funktionen

Betrachten wir einige Funktionen, die Sie auf Mengen anweden können:

* Kopieren einer Menge mit `copy()`
* Hinzufügen von Elementen mit `add()`
* Entfernen von Elementen mit `discard()`
* Leeren einer Menge mit `clear()`

```py
#Set
s1 = set([8,15, "x"])
print("Original s1:", s1)

# Kopie
s2 = s1.copy()
print("Kopie s2:", s2)

# Element hinzu
s1.add("abc")
print("Element zu s1:", s1)
print("s2:", s2)

# Element entnehmen
s1.discard("x")
print("Element entnommen:", s1)
try:
    s1.discard("x") # löst keinen Fehler aus!
except:
    print("Fehler") 

# leeren
s1.clear()
print("geleert:", s1)
```
```
Original s1: {8, 'x', 15}
Kopie s2: {8, 'x', 15}
Element zu s1: {8, 'abc', 'x', 15}
s2: {8, 'x', 15}
Element entnommen: {8, 'abc', 15}
geleert: set()
```
Die Funktion `copy()` erzeugt eine neue Menge als Kopie der alten Menge. Mithilfe der Funktion `add()` fügen Sie ein Element hinzu. Die Funktion `discard()` dient zum Löschen eines bestimmten Elements. Die Funktion `clear()` befreit die Menge von allen Elementen.

#### 4.6.3 Operatoren

Mit den vier Operatoren `<`, `<=`, und `>`, `>=`stellen Sie fest, ob eine Menge eine Teilmenge oder eine echte Teilmenge einer anderen Menge ist.

```py
# Sets
s1 = set([8,2,5])
s2 = set([2,8])
s3 = set([2,5,8])

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# Teilmenge, echte Teilmenge
if s2 < s1:
    print("s2 ist echte Teilmenge von s1")
if s3 <= s1:
    print("s3 ist Teilmenge von s1")
```
```
s1: {8,2,5}
s2: {8,2}
s3: {8,2,5}
s2 ist echte Teilmenge von s1
s3 ist Teilmenge von s1
```

Die Menge `s2` ist eine echte Teilmenge der Menge `s1`: Alle Elemente von `s2`sind in `s1`enthalten, und `s2` hat weniger Elemente als `s1`.

Die Menge `s3` ist nur eine *normale* Teilmenge der Menge `s1`: Alle Elemente von `s3` sind in `s1` enthaltne, aber `s3` hat ebensoviele Elemente wie `s1`. Die Reihenfolge der Elemente bei der Erzeugung ist unerheblich.

Im nachfolgenden Programm werden mithilfe der Operatoren `|` (or), `&`, (und), `-` (minus) und `^`(hoch) einige Mengenoperationen durchgeführt.

```py
# Sets
s1 = set([8,15,"x"])
s2 = set([4, "x", "abc", 15])
print("s1:", s1)
print("s2:", s2)

# Vereinigungsmenge

s3 = s1 | s2
print("Vereinigungsmenge:", s3)

# Schnittmenge
s4 = s1 & s2
print("Schnittmenge:", s4)

# Differenzmengen

s5 = s1 - s2
print("Differenzmenge s1-s2:", s5)

s6 = s2 - s1
print("Differenzmenge s2-s1:", s6)

s7 = s1 ^ s2
print("Symmetrische Differenzmenge s1^s2:", s7)
```
```
s1: {8, 'x', 15}
s2: {'x', 'abc', 4, 15}
Vereinigungsmenge: {'x', 'abc', 4, 8, 15}
Schnittmenge: {'x', 15}
Differenzmenge s1-s2: {8}
Differenzmenge s2-s1: {'abc', 4}
Symmetrische Differenzmenge s1-s2: {4, 8, 'abc'}
```

Der Operator `|` (oder) dient zur Vereinigung zweier Mengen. Die entstehende Menge enthält alle Elemente, die in der ersten oder in der zweiten Menge enthalten sind. Auch in der neuen Menge ist jedes Element nach wie vor nur einmal enthalten.

Die Elemente, die in der ersten und in der zweiten Menge enthalten sind, bliden die Schnittmenge. Dies gelingt mithilfe des Operators `&` (und).

Bei einer Differenzmenge müssen Sie beachten, welche Menge von welcher Anderen Menge abgezogen wird. Mithilfe des Operators `-` (minus)  werden zwei verschiedene Differenzmengen erstellt. 
Die Operation `s1-s2` zieht von der Menge `s1` alle Elemente ab, die auch in `s2` enthalten sind. 
Bei der Operation `s2-s1` verhält es sich umgekerht.

Bei der symmetrischen Differenzmenge werden mit dem Operator `^` (hoch) die Elemente ermittelt, die nur in einer der beiden Mengen enthalten sind.

#### 4.6.4 Frozenset

Ein Sonderfall eines Sets ist ein Frozenset. Im Unterschied zu einem set ist es *eingefroren*, also unveränderlich.

```py
# Set 
s = set([8,15,"x", 8])
print("Set:", s)

# Frozenset
fs = frozenset([8, 15, "x", 8])
print("Frozenset:", fs)
for x in fs:
    print(x)

try:
    fs.discard("x")
except:
    print("Fehler")
```
```
Set: {8,'x', 15}
Frozenset: frozenset({8,'x', 15})
8
x
15
Fehler
```
Mithilfe der Funktion `frozenset()` wird ein Frozenset erzeugt. Wie bei einem Set kommt jedes Element nur einmal vor. Bei der Ausgabe wird das Frzoenset durch den Begriff `frozenset` und zusätzlichen Klamemrn besonders gekennzeichnet.

Die einzelnen Elemente geben Sie mithilfe von `for` und `in` wie gewohnt aus. Der Versuch, ein Frzoenset zu verändern, führt zu einem Fehler.

### 4.7 Wahrheitswerte udn Nichts

Objete und Ausdrücke können wahr oder falsch sein, außerdem gibt es auch das Nichts-Objekt. Betrachten wir einige Zusammenhänge.

#### 4.7.1 Wahrheitswerte True und False

Besonders im Zusammenhang mit Bedingungsprüfung (`if`, `while`) wird der Wahrheitswert eines Ausdrucks benötigt.

Beispiel: Falls eine Zahl größer als 10 ist, sollen bestimmte Anweisungen ausgeführt werden. Der dabei benötigte Ausdruck `x > 10` ist wahr, wenn `x` einen Zahlenwert größer als 10 hat. Er ist falsch, wenn `x` einen Zahlenwert kleiner oder gleich 10 hat.

Diese Ausdrücke liefern eines der beiden Schlüsselwörter `True` oder `False`. Dies sind ie einzigen Objekte des Datentyps `bool`.

Es gibt außerdem die Funktion `bool()`, die den Wahrheitswert eines Ausdrucks oder eines Objekts zurückgibt. Alle Objekte in Python besitzen einen Wahrheitswert.

Folgende Objete sind wahr / `True`:
* eine Zahl ungleich 0, also größer als 0 oder kleiner als 0
* eine nicht leere Sequenz (String, Liste, Tupel)
* ein nicht leeres Dictionary
* eine nicht leere Menge

Folgene Objete sind falsch / `False`:
* Eine Zahl, die den Wert 0 hat
* eine leere Sequenz (String `""`, Liste `[]`, Tupel`()`)
* ein leeres Dictionary: `{}`
* eine leere Menge: `set()`, `frozenset()``
* die Konstante `None`(mehr dazu 4.7.2)

Entlosschleifen, die nur mit einem break verlassen werden können, werden gern mit `while 1` konstruiert. Diese Bedingung ist immer wahr. Sie können natürlich auch `while True` schreiben.

Gilt für eine Objektsammlung `len(x) == 0`, so ist das Objekt `x` falsch.

Im folgenden Programm wird der Wahrheitswert verschiedener Objekte an Beispielen dargestellt, überprüft und ausgegeben.

```py
# True and False
W = True
print("Wahrheitswert:", W)
W = False
print("Wahrheitswert:", W)
W = 5>3
print("5>3:", W)
W = 5<3
print("5<3:", W)
print()

# Datentyp

W = 5>3
print("Typ von 5>3:", type(W))
print()

# wahre Zahl
Z = 5 + 0.001 - 5
print("Zahl:", Z)
if Z:
    print("Zahl ist", bool(Z))

# nicht wahre Zahl
Z = 5.75 - 5.75
print("Zahl:", Z)
if not Z:
    print("Zahl ist", bool(Z))
print()

# String
S = "Kurt"
print("String:", S)
if S:
    print("String ist nicht leer, also", bool(S))

# Liste
L = [3,4]
print("Liste vorher:", L)
del L[0:2]
print("Liste nachher:", L)
if not L:
    print("Liste ist leer, also", bool(L))
print()

# Tupel
T = (5,8,2)
print("Tupel:", T)
if T:
    print("Tupel ist nicht leer, also", bool(T))
print()

# Dictionary
D = {"Julia":28, "Werner":32}
print("Dictionary vorher:", D)
del D["Julia"]
del D["Werner"]
print("Dictionary nachher:", D)
if not D:
    print("Dictionary ist leer, also", bool(D))
print()

# Set
S = set([5, 7.5, "abc"])
print("Set vorher:", S)
S.clear()
print("Set nachher:", S)
if not S:
    print("Set ist leer, also", bool(S))
```
```
Wahrheitswert: True
Wahrheitswert: False
5>3: True
5<3: False

Typ von 5>3: <class 'bool'>

Zahl: 0.001000000000000334
Zahl ist True
Zahl: 0.0
Zahl ist False

String: Kurt
String ist nicht leer, also True
Liste vorher: [3, 4]
Liste nachher: []
Liste ist leer, also False

Tupel: (5, 8, 2)
Tupel ist nicht leer, also True

Dictionary vorher: {'Julia': 28, 'Werner': 32}
Dictionary nachher: {}
Dictionary ist leer, also False

Set vorher: {5, 'abc', 7.5}
Set nachher: set()
Set ist leer, also False
```
Der Variablen W werden Wahrheitswerte bzw. Die Ergebnisse von Vergleichsausdrücken, also ebenfalls Wahrheitswerte, zugewiesen. Der Datentyp der Wahrheitswerte ist `bool`. Sobald das Ergebnis einer Berechnung von 0 abweicht, ergbit sich der Wahrhetiswert `True`.

String, Liste, Tupel, Dictionary und set ergeben `False`,  wenn sie leer sind, und `True`, wenn sie nicht leer sind. Dies können Sie zur Prüfung der betreffenden Objekte nutzen.

#### 4.7.2 Nichts, None

Das Schlüsselwort `None` bezeichnet das Nichts-Objekt. `None` ist das einzige Objekt des Datentyps `NoneType`.

Funktionen ohne Rückgabewert liefer `None` zurück. Dies kann ein Hinweis darauf sein,
* dass Sie eine Funktion falsch einsetzen, bei der Sie einen Rückgabewert werwarten, oder
* dass eine Funktion kein Ergebnis liefert, obwohl dies erwartet wird.

```py
# Funktion
def quotient(a,b):
    try:
        c = a/b
        return c
    except:
        print("Funktion meldet Fehler")

# liefert Ergebnis
erg = quotient(7,4)
if erg:
    print("Ergebnis:", erg)
print()

# liefert Fehler

erg = quotient(7,0)
if not erg:
    print("Programm meldet Fehler")
print("Ergebnis:", erg)
print("Typ des Ergebnisses:", type(erg))
print()

# Konstante None
Z = None
print("Z:", Z)
if Z is None:
    print("Objekt ist das Nichts, also", bool(Z))
```
```
Ergebnis: 1.75

Funktion meldet Fehler
Programm meldet Fehler
Ergebnis: None
Typ des Ergebnisses: <class 'NoneType'>

Z: None
Objekt ist das Nichts, also False
```

Die Funktion `quotient()` wird definiert. Sie berechnet den Quotienten aus zwei Zahlen. Sie kann nicht den Wert 0 als Ergebnis liefern.

* Falls der Quotient regulär berechnet werden kann, wird das Ergebnis mithilfe von `return` zurückgeliefert. Dies ist beim ersten Aufruf der Funktion der Fall.
* Falls ein Fehler auftritt, wird nichts zurückgeflierrt. Die Variable `erg` erhält also den Wert `None`. Dies können Sie abfragen und damit feststellen, dass die Funktion kein nutzbares Ergebnis geliefert hat.

Das Nichts-Objekt hat den Wahrheitswert `False`.

### 4.8 Referenz, Identität und Kopie

In diesem Abschnitt erläutere ich den Zusammenhang zwischen Objekten und Referenzen. Wir untersuchen die Identität von Objekten und erzeugen Kopen von Objekten.

#### 4.8.1 Referenz und Identität

Der Name eines Objekts ist eigentlich eine Referenz auf ein Objekt.
Weißen Sie diese Referenz einem anderen Namen zu, erzeugen Sie eine zweite Referenz auf dassele Objekt. Mithilfe des Identitätsoberators `is` stellen Sie fest, dass beide Referenzen auf dasselbe Objekt verweisen.

Wird das Objekt über die zweite Referenz geändert, zeigt sich eine der beiden folgenden Verhaltensweisen:
* Im Fall eines einfachen Objekts wie Zahl oder String wird ein zweites Objekt erzeugt, in dem der neue Wert gespeichert wird. Die beiden Referenzen verweisen danach auf zwei verschiedene Objekte.
* Im Fall eines nicht einfachen Objekts wie Liste, Dictionary usw. wird das Originalobjekt geändert. Es gibt nach wie vor ein Objekt mit zwei verschienden Referenzen.

Mithilfe des Operators `==` stellen Sie fest, ob zwei Objekte den gleichen Inhalt haben, ob also z.B. zwei Listen die gleichen Elemente enthalten.

Im folgenden Beispiel werden nacheinander eine Zahl, ein String und eine Liste erzeugt und zweimal referenziert. Anschließend wird der zweiten Referenz jeweils ein neuer Inhalt zugewiesen. identität und Inhalt werden anhand der eiden Operatoren `is` und `==` festgestellt.

```py
# Kopie einer Zahl
print("Zahl:")
x = 12.5
y = x
print("Dasselbe Objekt:", x is y)
y = 15.8
print("Dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Kopie eines Strings
print("String:")
x = "Robinson"
y = x
print("dasselbe Objekt:", x is y)
y = "Freitag"
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Zweite Refernz auf eine Liste
print("Liste:")
x = [23, "hallo", -7.5]
y = x
print("dasselbe Objekt:", x is y)
y[1] = "welt"
print("dasselbe objekt:", x is y)
print("gleicher Inhalt:", x == y)
```
```
Zahl:
Dasselbe Objekt: True
Dasselbe Objekt: False
gleicher Inhalt: False

String:
dasselbe Objekt: True
dasselbe Objekt: False
gleicher Inhalt: False

Liste:
dasselbe Objekt: True
dasselbe objekt: True
gleicher Inhalt: True
```
Die Ausgabe zeigt, dass die Objekte zunächst jeweils identisch sind.

Bei einer Zahl oder einem String wird durch die Zuweisung eines neuen Werts jeweils ein neues Objekt erzeugt. Die Inhalte sind nach der Zuweisung natürlich unterschiedlich.

Die Liste(hier stellvertretend auch für andere Objekte) existiert insgesamt nur einmal, auch wenn einzelne Elemente der Liste verändert werden. Sie können über beide Referenzen auf diesselbe Liste zugreifen.

#### 4.8.2 Ressourcen sparen
Python spart gern Ressourcen. Dies kann zu einem ungewöhnlichen Verhalten führen: Wenn einem Objekt über eine Referenz ein Wert zugewiesen wird *und* auf denselben Wert bereits von einer anderen Referenz verwiesen wird, kann es geschehen, dass die beiden Referenzen anschließend auf dasselbe Objekt verweisen. Python spart also Speicherplatz.

Das Schlüsselwort `del` dient zur Löschung von nicht mehr benötigten Referenzen. Ein Objekt, auf das zwei Referenzen verweisen, wird druc da Löschen der ersten Referenz nicht gelöscht.

```py
# Ein Objekt, zwei Referenzen
x = 42
y = 42
print("x:", x, "y:", y, "identisch:", x is y)

# Zweites Objekt
y = 56
print("x:", x, "y:", y, "identisch:", x is y)

# Ressourcen sparen
y = 42
print("x:", x, "y:", y, "identisch:", x is y)

# Entfernen, Schritt 1
del y
print("x", x)

# Entfernen, Schritt 2
del x
try:
    print("x:", x)
except:
    print("Fehler")
```
```
x: 42 y: 42 identisch: True
x: 42 y: 56 identisch: False
x: 42 y: 42 identisch: True
x 42
Fehler
```
Zunächst erhalten die Referenzen `x` und `y` denselben Wert. Wir stellen fest: Es handelt sich um ein Objekt mit zwei Referenzen. Anschließend wird der Wert von `y` geändert. Damit gibt es zwei Refrenzen auf zwei verschiedene Objekte. Zuletzt wird der Wert von `y` auf den alten Wert zurückgesetzt. Nun gibt es wieder nur noch ein Objekt.

Die Referenz `y` wird gelöscht. Das Obejkt existiert weiterhin und kann über die Referenz `x`erreicht werden. Anschließend wird die Referenz `x` gelöscht. Die Ausgabe über diese Referenz fürht zu einem Fehler, da der Name nicht mehr existiert.

#### 4.8.3 Objekte kopieren
Echte Kopien von nicht einfachen objekten können Sie durch das Erzeugen eines leeren Objekts und Anhängen oder Hinzufügen der einzelnen Elemente erzeugen. Für umfangreiche Objekte, die wiederum andere Objekte enthalten, können Sie sich auf die Funktion() `deepcopy()` aus dem Modul `copy` bedienen. Beides wird in folgendem Programm gezeigt.

```py
# Modul copy
import copy

# Kopie einer Liste, Methode 1
x = [23, "hallo", -7.5]
y = []
for i in x:             # Elemente einzeln kopieren
    y.append(i)
print("Dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Kopie einer Liste, Methode 2
x = [23, ["Berlin", "Hamburg"], -7.5, 12, 67]
y = copy.deepcopy(x)    # Funktion zur Tiefenkopie
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
```
```
Dasselbe Objekt: False
gleicher Inhalt: True

dasselbe Objekt: False
gleicher Inhalt: True
```
Die Ausgabe zeigt, dass in beiden Fällen jeweils ein neues Objekt erzeugt wird. Die Inhalte der beiden Objekte sind allerdings gleich.

## 5 Weiterführende Programmierung

In diesem Kapitel werden die Kenntnisse aus dem Programmierkurs im Zusammenhang mit den verschiedenen Objekttypen durch nützliche Praxistipps erweitert.

### 5.1 Allgemeines
Im ersten Teil des Kapitels erläutere ich einige nützliche Techniken, die keinen bestimmten Thema zuzuordnen sind.

#### 5.1.1 Kombinierte Zuweisungsoperatoren

Neben der einfachen Zuweisung eines Werts zu einer Variablen gibt es auch die kombinierten Zuweisungsoperatoren. Diese verbinden die normalen Operatoren für Zahlen oder Zeichenketten mit der Zuweisung eines Werts. Die betreffende Variable wird also unmittelbar um den genannten Wert verändert. Dies ist besonders bei umfangreichen Ausdrücken oder bei längeren Variabelnamen sinnvoll. Ein Beispiel:

Der Ausdruck `TemperaturInCelsius += 5` ist überschaubarer als der Ausdruck `TemperaturInCelsius = TemperaturInCelsius + 5`. Beide Ausdrücke erhöhen den Wert der Variablen `TemperaturInCelsius` um 5.

Es folgt ein Beispiel in dem kombinierte Zuweisungsoperatoren für Zahlen und für Zeichenketten eingsetzt werden.

```py
# Kombinierte Zuweisungsoperatoren für Zahlen
x = 12
print(x)
x += 3      # erhöhen um
print(x)
x -= 9      # reduzieren um
print(x)
x **= 2     # Quadrieren
print(x)
x *= 3      # Multiplizieren
print(x)
x //= 7     # Ganzzahliges Teilen von x
print(x)
x /= 4      # Teilen von x
print(x)
x %= 2      # Dividieren, Rest berechnen
print(x)

# Kombinierte Zuweisungsoperatoren für Zeichenketten
t = "hallo"
print(t)
t += "python"   # Anhängen an t
print(t)
t *= 3          # Verdreifachen von t
print(t)
```
```
12
15
6
36
108
15
3.75
1.75
hallo
hallopython
hallopythonhallopythonhallopython
```
Die Variable `x`erhält zunächst den Zahlenwert 12. Durch die nachfolgende Anweisung wird ihr Wert jedesmal verändert. Der wert wird als Erstes um 3 erhöht (=15), snchließend um 9 vermindert (=6), anschließend hoch 2 gerechnet (=36) und mit 3 multipliziert (=108). Es folgt eine Ganzzahldivision, dabei werden die Nachkommastellen abgeschnitten. Die verbleibende Zahl (15) wird durch 4 geteilt (= 3.75). Zuletzt wird der Rest der Divison durch 2 berechnet ( = 1.75).

Die Variable t erhält den Zeichenkettenwert `"hallo"`. Anschließend wird sie verlängert und vervielfacht.

Bei all diesen Operationen ist darauf zu achten, dass die betreffende Variable vorher bereits einen Wert hat, sonst trifft ein Fehler auf.

#### 5.1.2 Programmzeile in mehreren Zeilen
In Abschnitt 2.3.6 wurde erläutert, wie sie eine längere Zeichenkette bei Einsatz der Funktion `print()` über mehrere Zeilen verteilen. In diesem Abschnitt zeige ich, wie Sie lange Programmzeilen allgemein zerlegen können, u. a. mithilfe des Zeichens `\`. Ein Beispiel:

```py
print("umrechnung von Celcsius in Fahrenheit")

# Trennung einer Zeichenkette
print("Bitte geben Sie eine"
      "Temperatur in Celsius ein:")
TemperaturInCelsius = float(input())

# Trennung eines Ausdrucks
TemperaturInFahrenheit = TemperaturInCelsius \
                         * 9 / 5 + 32

# Trennung nach einem Komma
print(TemperaturInCelsius, "Grad Celsius entsprechen",
      TemperaturInFahrenheit, "Grad Fahrenheit")
```
Zunächst wird eine Zeichenkette in gewohnter Weise zerlegt und in zwei Zeilen notiert. Jeder Teil der Zeichenkette wird in Anführungszeichen gesetzt. Ein trennendes Leerzeichen zwischen den beiden Teilen muss von Hand eingegeben werden.

Eine längere Programmzeile mit einer berechnung wird mithilfe des Zeichens `\` zerlegt. Dieses Zeichen zeigt an, dass die Programmzeile in der nächsten Zeile fortgesetzt wird.

Einfacher ist die Zerlegung der Programmzeile, wenn darin Kommata auftreten, wie z.B. beim Aufruf einer Funktion mit mehreren Parametern oder bei der Zuweisung einer Liste. Hier können Sie einfach nach einem Komma trennen.

#### 5.1.3 Eingabe mit Hilfestellung

Die eingebaute Funktion `input()` zur Eingabe von Zeichenketten hat einen optionalen Parameter. Dabei handelt es sich ebenfalls um eine Zeichenkette mit einer möglichst hilfreichen Information für die Eingabe. Dies spart eine Zeile mit er Funktion `print()`.

Im folgendenBeispiel wird zunächst die Summe aus drei eingegebenen Zahlen berechnet. Anschließend wird der Benutzer aufgefordert, den Namen der Hauptstadt eines Landes einzugeben

```py
# Berechnung einer Summe
summe = 0
for i in range (1,4):
    fehler = True
    while fehler:
        zahl = input(str(i) + ". Zahl eingeben: ")
        try:
            summe += float(zahl)
            fehler = False
        except:
            print("Das war keien Zahl")
            fehler = True
print("Summe:", summe)
print()

# Geografiespiel

hauptstadt = {"Italien":"Rom", "Spanien":"Madrid", "Portugal":"Lissabon"}
hs = hauptstadt.items()
for land, stadt in hs:
    eingabe = input("Bitte die Hauptstadt von " + land + " eingeben: ")
    if eingabe == stadt:
        print("richtig")
    else:
        print("falsch, richtig ist:", stadt)
```

Bei der Eingabe zur Berechnung einer Summe wird als Hilfestellung die laufendeNummer der einzugebenen Zahl ausgegeben. Diese Nummer muss in eine Zeichenkette umgewandelt und mit dem restlichen Text verketten werden. 
Aufgrund der Ausnahmebehandlung muss eine fehlerhafte Eingabe wiederholt werden. In diesem Fall wird wieder dieselbe laufende Nummer als Hilfestellung ausgegeben.

Bei der Zeichenketteneingabe wird das Land mit ausgegeben. Der Benutzer gibt die Hauptstadt ein und erhält als Rückmeldung, ob seine Eingabe richtig oder falsch ist.

#### 5.1.4 Anweisung `pass`

Die Anweisung `pass` bewrikt, dass nichts ausgeführt wird Wozu existiert sie überhaupt? Einige mögliche Einsatzzwecke sind:

* Sie enwickeln ein Programm, in dem u.a. eine Funktion aufgerufen wird. In der ersten Entwcklungsphase soll da Hauptprogramm geschrieben werden.
Der Funktionsaufruf soll aus Gründen der Übersichtlichkeit bereits an der richtigen Stelle platziert werden, aber noch keine Auswirkungen haben. Die Funktionsdefinition enthält in diesem Fall nur die Anweisung `pass`.
* Das Programm enthält eine einfache oder mehrfache Verzweigung, bei der in einem bestimmten Zweig nichts ausgeführt werden soll. Dieser Zweig soll aber dennoch erscheinen, um den Programmablauf klarer zu machen.

```py
# Funktions-Dummy
def QuadraturDesKreises():
    pass

# Funktionsaufruf
QuadraturDesKreises()

# Nur else-Zweig interessant

a = -12
b = 6
c = 6.2

if a >= 0 and b >= 0 and c >= 0:
    pass
else:
    print("eine der Zahlen ist negativ")

# Ein Zweig nicht interessant

if a == 1:
    print("Fall 1")
if a == 2:
    print("Fall 2")
if a < 0:
    pass
else:
    print("Ansonsten")
```
Die Funktion `QuadraturDesKreises()` dient zunächst nur als Dummy und wird in einem späteren Zeitpunkt mit INhalten gefüllt. Sie ist aber bereits im Programm eingebaut und kann aufgerufen werden.

Bei der einfachen Verzweigung erfolgt im `else`-Zweig eine Ausgabe. Bei der mehrfachen Verzweigung erfolgt ur eine Ausgabe, falls der untersuchte wert größer oder gleich 0 ist.

#### 5.1.5 Funktionen `eval()` und `exec()`

Die Funktionen `eval()` und `exec()` dienen zum zusammensetzen von Python-Code. Mit diese Funktionen lassen sich Anweisungen dynamsich aus Zeichenketten bilden:

* Die Funktion `eval()` evalueirt den zusammengesetzten Ausdruck, ermittelt also den Wert des Ausdrucks.
* Die Funktion `exec()` führt eine zusammengesetzte Anweisung aus.

```py
import math

# Zwei Funktionen

def mw1(a,b):
    c = (a+b)/2
    return c

def mw2(a,b):
    c = math.sqrt(a*b)
    return c

# eval
for i in 1,2:
    t = "mw" + str(i) + "(3,4)"
    c = eval(t)
    print(c)
print()

# exec
for i in 1,2:
    t = "print(mw" + str(i) + "(3,4))"
    exec(t)
```
Es werden zunächst die Funktionen `mw1()` zur Ermittelung des arithmetrsichen Mittelwerts und die FUnktion `mw2()` zur Ermittelung des geometrischen Mittelwerts zweier Zahlen definiert. Die Namen der beiden Funktionen, `mw1` und `mw2`, unterscheiden sich in der Ziffer.

Für den Aufruf von `eval()`werden zwei Ausdrücke jeweils in einer Zeichenkette zusammengesetzt: "mw1(3,4)" und "mw2(3,4)". Damit können die beiden Aufrufe erfolgen: `c = mw1(3,4)`und `c = mw2(3,4)`. Der Rückgabewert wird in der Variablen `c` gespeichert, die anschließend ausgegeben wird.

Für den Aufruf von `exec()` werden zwei Anweisungen jeweils in einer Zeichenkette zusammengesetzt: `"print(mw1(3,4))"`und `"print(mw2(3,4))"`. Beide Anweisungen werden ausgeführt. Der Rückgabewert wird unmittelbar ausgegeben.

### 5.2 Ausgabe und Formatierung

In diesem Abschnitt erläutere ich einige MÖglichkeiten zur Ausgabe mit hilfe der Funktion `print()`

#### 5.2.1 Funktion `print()`

Die Funktion `print()` haben wir bereits mehrfach eingestzt. Sie beitet noch weitere Möglichkeiten:

* Der Seperator, der die ausgegebenen Objekte voneinander trennt, kann verändert werden. Er wird mit  `sep` bezeichnet. Normalerweise wird ein Leerzeichen zur Trennung ausgegeben.
* Das Zeilenende, das normalerweise nach einer ausgabe folgt, kann verändert werden. Es wird mit `end` bezeichnet.

```py
# Berechnung
a = 23
b = 7.5
c = a + b

# normale Ausgabe
print("Ergebnis:", a, "*", b, "=", c)

# Ausgabe ohne Zeilenende und Leerzeichen
print("Ergebnis:", end="")
print(a, "+", b, "=", c, sep="")

# Neue Zeile
print()

# Liste
stadt = ["Hamburg", "Berlin", "Augsburg"]
for x in stadt:
    print(x)

for x in stadt:
    print("Stadt:", x, sep="=>", end="#")
```
```
Ergebnis: 23 * 7.5 = 30.5
Ergebnis:23+7.5=30.5

Hamburg
Berlin
Augsburg
Stadt:=>Hamburg#Stadt:=>Berlin#Stadt:=>Augsburg#
```
Zunächst wird die normale Ausgabe einer Berechnung mit Leerzeichen zwischen den einzelnen Elementen erzeugt.

Es folgen zwei Anweisungen, jeweils mit dre Funktion `print()`. Bisher führt dies dazu, dass zwei ausgabe zeilen erzeugt werden:
* Weise n sie allerdings dem Parameter `end` eine leere Zeichenkette zu, wird am Ende der Zeile nichts ausgegeben. Die nächste Ausgabe erfolgt anschließen in derselben Zeile.
* Bei der nächsten Ausgabe wir dem Parameter `sep` eine leere Zeichenkette zugewiesen. Dies führt dazu, dass die Ausgaben ohne Leerzeichen direkt hintereinanderstehen.
Es folgt die Ausgabe der Elemente einer Liste zunächst in gewohnter Form. In der zweiten version werden sowohl der Separator als auch das Zeilenende verändert.

#### 5.2.2 Formatierung mit String-Literalen

Es gibt in Python mehrere Möglichkeiten, Zahlen und Zeichenketten einheitlich formatiert auszugeben. Seit Python 3.6 gibt es zu diesem Zweick die formatierten String-Literale. Sie nutzen die gleichen Formate wie die eingebaute Funktion `format()`. Die Ausdrücke mit String-Literalen sind aber kürzer und besser lesbar. In Abschnitt 5.2.3 sehen Sie die Unterschiede zur Fuunktion `format()` im Einzelnen.

Eine einheitliche Formatierung dient z.B. einer übersichtlichen Ausgabe in Tabellenform. Sie können u.a. Folgendes bestimmen:
* die Mindestausgabebreite der Zahlen
* die Anzahl der Nachkommastellen

Die Anzahl der Nachkommastellen:

```py
# Zahl mit Nachkommastellen
x = 100/7
y = 2/7

print("Zahlen:", x, y)
print()

# Format f
print(f"Format f, Standard:    {x:f} {x:f} {y:f}")
print(f"Format f, nach Komma:  {x:.25f}")
print(f"Format f, gesamt:      {x:15.10f}")
print()

# Format e
print(f"Format e, Standard:    {x:e}")
print(f"Format e, nach Komma:  {x:.3e}")
print(f"Format e, gesamt:      {x:12.3e}")
print()

# Format %
print(f"Format %, Standard:    {y:%}")
print(f"Format %, nach Komma:  {y:.3%}")
print(f"Format %, gesamt:      {y:12.3%}")
```
```
Zahlen: 14.285714285714286 0.2857142857142857

Format f, Standard:    14.285714 14.285714 0.285714
Format f, nach Komma:  14.2857142857142864755815026
Format f, gesamt:        14.2857142857

Format e, Standard:    1.428571e+01
Format e, nach Komma:  1.429e+01
Format e, gesamt:         1.429e+01

Format %, Standard:    28.571429%
Format %, nach Komma:  28.571%
Format %, gesamt:           28.571%
```

Zunächst erzahlten die Variablen x und y die Werte von 100/7 bzw 2/7. Sie werden zum Vergleich unformatiert ausgegeben.

Mithilfe des Buchstabens `f` vor der Zeichenkette wird festgelegt, dass ein formatiertes String_literal folgt. Die formatierten Bestandteile der Zeichenkette werden mithilfe von geschweiften Klammern gebildet. Darin stehen die Variablen oder Werte, gefolgt von einem Doppelpunkt und den Formatierungszeichen.

Das Formatierungszeichen `f` steht für die Ausgabe einer Zahl mit eine rAnzahl von Nachkommastellen, standartmäßig sechs. Die Angabe `.25f` erzeugt 25 Nachkommastellen. Die Angabe `15.10f` steht für rechtsbündige Ausgabe einer Zahl auf einer Gesamtbreite von 15 Stellen, davon 10 nach dem Komma. Ein solches Format ist besonders für Tabellen geeignet.

Das Formatierungszeichen `e` steht für die Ausgabe einer Zahl im Exponentialformat, standardmäßig mit sechs Nachkommastellen und Exponent. Die Angabe `12.3e` steht für die rechtsbündige Ausgabe auf einer Gesamtbreite von 12 Stellen, davon 3 nach dem Komma.

Das Formatierungszeichen steht für die Ausgabe einer Zahl im Prozentformat, standardmäßig mit sechs Nachkommastellen und einem Prozentzeichen. Die Zahl wird nun für die Ausgabe mit 100 multipliziert, intern bleibt sie unverändert. Die Angabe `.3%` erzeugt drei stellen nach dem Komma. Die Angabe `12.3%` steht für die rechtsbündige Ausgabe auf einer Gesamtbreite von 12 Stellen, davon 3 nach dem Komma.

Im nachfolgenden Programm sehen Sie die Ausgabe von ganzen Zahlen und Zeichenketten mithilfe von formatierten String-Literalen:

```py
# Formatierung von Zeichenketten
print(f"{'dez':>4}{'dual':>9}{'oct':>4}{'hex':>4}")

# Formatierung ganzer Zahlen
for z in range(59,69):
    print(f"{z:4d}{z:9b}{z:4o}{z:4x}")
print()

# Tabelle mit verschiedenen Objekten
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis= {23:2.95, 8:1.45, 42:3.03}

print(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'Einzel':>13}{'Summe':>13}")
for x in 23, 8, 42:
    print(f"{x:04d}{artname[x]:>12}{anzahl[x]:4d}{epreis[x]:8.2f} Euro{anzahl[x]*epreis[x]:8.2f} Euro")
```
```
 dez     dual oct hex
  59   111011  73  3b
  60   111100  74  3c
  61   111101  75  3d
  62   111110  76  3e
  63   111111  77  3f
  64  1000000 100  40
  65  1000001 101  41
  66  1000010 102  42
  67  1000011 103  43
  68  1000100 104  44

  Nr        Name Anz       Einzel        Summe
0023       Apfel   1    2.95 Euro    2.95 Euro
0008      Banane   3    1.45 Euro    4.35 Euro
0042    Pfirsich   5    3.03 Euro   15.15 Euro
```

Sie können die Formatierung nicht nur für Variablen, sondern auf für Werte nutzen. Standardmäßig werden Zahlen rechtsbündig ausgegeben und Zeichenketten linksbündig. Zeichenketten werden in geschweiften Klammern innerhalb von einfachen Anführungsstrichen notiert.

Das Formatierungszeichen `>` steht für eine rechtsbündige Ausgabe, die nachfolgende Zahl für die Gesamtbreite der Ausgabe. Das Zeichen `<` steht analog für linksbündig.

Es folgt eine einheitliche formatierte Zahlentabelle. Die Zahlen von 59 bis 68 werden nacheinander ausgegeben als:
* Dezimalzahl - Formatierungsziechen `d`
* Dualzahl - Formatierungszeichen `b`
* Oktalzahl - Formatierungszeichen `o`
* Hexadezimalzahl - Formatierungszeichen `x`

Sie können die Formatierung auch für berechnete Ausdrücke nutzen. Beispiele dafür sehen sie in der Artikeltabelle, die auf den drei Dictionarys für den Artikelnamen, die Anzahl und den Einzelpreis basiert. Die Elemente der Dictionarys werden, zusammen it dem ermittelten Gesamtpreis, einheitlich ausgegeben.

Steht vor der Angabe der Gesamtbreite eine `0`, wird die Zahl mit führerenden Nullen aufgefüllt.(`{x:04d} => 000x`) Dies ist bei der ersten Spalte der Fall. Bei der Aufteilung eines einzelnen String-Literals eines einzelnen String-Literals auf mehrere String_literale müssen Sie das führende `f` vor jeder Zeichenkette notieren. 

#### 5.2.3 Formatierung mit `format()`

Die Formatierung in den beiden Programmen aus Abschnitt 5.2.2 wird in den beiden nachfolgenden Programmen mithilfe der eingebauten Funktion `format()` erzeugt. Die Ausgaben sind gleich. Es werden nur die Unterschiede erläutert.

Zunächst Ausschnitte aus dem ersten Programm:
```py
...
print("Format f, Standard:    {0:f} {0:f} {1:f}".format(x,y))
print("Format f, nach Komma:  {0:.25f}".format(x))
print("Format f, gesamt:      {0:15.10f}".format(x))
...
print("Format e, Standard:    {0:e}".format(x))
print("Format e, nach Komma:  {0:.3e}".format(x))
print("Format e, gesamt:      {0:12.3e}".format(x))
...
print("Format %, Standard:    {0:%}".format(y))
print("Format %, nach Komma:  {0:.3%}".format(y))
print("Format %, gesamt:      {0:12.3%}".format(y))
```

Die Zeichenkette dient als Objekt, auf dass die Funktion `format()` angewendet wird. Vor dem Doppelpunkt innerhalb der geschweiften Klammern stehen Nummern. Diese Nummern stehen für die Parameter der Funktion `format()`. Sie werden, beginnend mit 0, nummeriert.

Im ersten Beispiel wird zweimal die Variable `x` für die Nummer 0 und einmal die Variable `y` für die Nummer 1 eingesetzt. In den restlichen Beispielen wird nur de Wert einer Variablen formatiert, daher steht vor dem Doppelpunkt jeweils eine 0.

Es folgt das zweite Programm:

```py
# Formatierung von Zeichenketten
print("{0:>4}{1:>9}{2:>4}{3:>4}".format("dez", "dual", "okt", "hex"))

# Formatierung ganzer Zahlen
for z in range(59,69):
    print("{0:4d}{0:9b}{0:4o}{0:4x}".format(z))
print()

# Tabelle mit verschiedenen Objekten
fm = "{0:04d}{1:>12}{2:4d}{3:8.2f} Euro{4:8.2f} Euro"
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis= {23:2.95, 8:1.45, 42:3.03}

print("{0:>4}{1:>12}{2:>4}{3:>13}{4:>13}".format("Nr", "Name", "Anz", "Einzel", "Summe"))
for x in 23, 8, 42:
    print(fm.format(x, artname[x], anzahl[x], epreis[x], anzahl[x] * epreis[x]))
```

In der Überschrift der ersten Tabelle werden die vier Texte, denen die Parameternummern 0,1,2,3 zugeordnet sind, rechtsbündig formatiert. In der ersten Tabelle selbst wrid die Variable `z` (0), viermal genutzt.

In der Variablen `fm` wird die Zeichenkette inklusive der Nummern der Parameter gespeichert. Auf diese Weise könnte sie mehrfach verwendet werden. In der Überschrift der zweiten Tabelle werden die fünf Texte, denen die Parameternummern 0 bis 4 zugeordnet sind, rechtsbündig formatiert. In der zweiten Tabelle selbst werden die Werte für die formatierte Zeichenkette in der Variablen `fm` gespeichert.

#### 5.2.4 Formatierung wie in C

Die Formatierung in den beidne Programmen aus Abschnitt 5.2.2 wird in den beiden nachfolgenden Programmen mithilfe einer Formatierung erzeugt, die Sie möglicherweise aus dr Programmiersprache C kennen. Sie wurde aus Python 2 übernommen und ist in vielen Programmen noch anzutreffen. Allerdings ist sie veraltet und wird zukünftig nicht mehr unterstützt. Die Ausgaben sind gleich. Es werden nur die Unterschiede erläutert.
Zunächst Auschnitte aus dem ersten Programm:

```py
print("Format f, Standard:     %f %f %f" % (x, x, y))
print("Format f, nach Komma:   %.25f" % (x))
print("Format f, gesamt:       %15.10f" %(x))
...
print("Format e, Standard:     %e" % (x))
print("Format e, nach Komma:   %.3e" % (x))
print("Format e, gesamt:       %12.3e"% (x))
...
print("Format %%, Standard:    %f%%" % (y*100))
print("Format %%, nach Komma:  %.3f%%" % (y*100))
print("Format %%, gesamt:      %12.3f%%" % (y*100))
```

Ein Audruck setzt sich aus einer Zeichenkette, dem Prozentzeichen und einer Reihe von Variablen oder Werten innerhalb von runden Klammern zusammen. Diese Variablen oder Werte werden der Reihe nach für die Formatierungszeichen, die sich innerhalb der Zeichenkette befinden, eingesetzt. Die Anzahl der Formatierungszeichen muss immer der Anzahl der Variablen oder Werte entsprechen.

Ein Formatierungszeichen beginnt immer mit dem Prozentzeichen. Die Formatierungszeichen `%f` und `%e` haben dieselbe Bedeutung wie bei den String-Literalen aus Abschnitt 5.2.2. Dasselbe gilt für die Angaben zur Anzahl der Nachkommastellen und zur Gesamtbreite. Ein Prozentzeichen wird durch zwei aufeinanderfolgende Prozentzeichen ausgegeben. Die Multiplikation des Werts mit der Zahl 100 muss *von Hand*  vorgenommen werden.

Es folgt das zweite Programm:

```py
# Formatierung von Zeichenketten
print("%4s%4s%4s" % ("dez", "okt", "hex"))

# Formatierung ganzer Zahlen
for z in range(59,69):
    print("%4d%4o%4x" % (z,z,z))
print()

# Tabelle mit verschienen Objekten
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}

print("%4s%12s%4s%13s%13s" % ("Nr", "Name", "Anz", "E-Preis", "Summe"))
for x in 23, 8, 42:
    print("%4d%12s%4d%13d%13d" % (x, artname[x], anzahl[x], epreis[x], epreis[x]*anzahl[x]))
```

Das Formatierungszeichen `%s`wird für Zeichenketten genutzt. Die Angabe `%-12s` würde zu einer linksbündigen Ausgabe führen. Für Dualzahlen gibt es kein Format, daher sind sie nicht im Programm enthalten. Die Formatierungszeichen `%d`, `%o` und `%x` haben dieselbe Bedeutung wie bei den String-Literalen aus Abschnitt 5.2.2.

### 5.3 Conditional Expression
Eine *Conditional Expression* (bedingter Ausdruck) kann als Schreibabkürzung für eine einfache Verzweigung dienen. Sie müssen selbst entscheiden, welche Version für Sie besser lesbar ist. Ein Programm mit zwei Beispielen:

```py
x = -12
y = 15

# Ausdruch zur Zuweisung

maximum = x if x>y else y
print(maximum)

# Ausdruck zur Ausgabe
print("positiv" if x>0 else "negativ oder 0")
```
Das Programm erzeugt die Ausgabe:
```
15
negativ oder 0
```

Die erste Anweisugn mit dem bedingten Ausdruck liest sich wie folgt:
Die Variable `maximum` enthält den Wert von `x`, falls `x > y`; andernfalls erhält die Variable `maximum` den wert von `y`.

Die zweite Anweisung mit dem bedingten Ausdruck liest sich so: Gib die Zeichenkette `positiv` aus, falls `x` größer als 0 ist, ansonten gib `negativ oder 0` aus.

### 5.4 Iterierbare Objekte

Ein Objekt, das aus einer Abfolge von Objekten besteht, die z.B. in einer `for`-Schleife durchlafuen werden kann, wird allgemein *iterierbares Objekt* genannt oder kurz *iterable*. `Listen`, `Zeichenketten`, `Tupel`, `Dictionary`, und andere Objekte sind iterierbar. Iteratoren ermöglichen einen schnellen Durchlauf durch iterierbare Objekte.

Es gibt eine Reihe von Funktionen, die mit iterierbaren Objekten arbeiten. Sie können dem Entwickler viel Arbeit abnehmen. Als Beispiele erläutere ich im Folgenden die Funktionen `zip()`, `map()` und `filter()`.

Python ist eine sehr vielseitige Programmiersprache. Sie nutzt auch Prinzipien der funktionalen Programmierung, und zwar beim Einatz der nachfolgenden Funktionen bzw. Technik. 
* der Funktion `map()` siehe 5.4.2
* der Funktion `filter()` siehe 5.4.3
* Der *List Comprehension* siehe 5.5
* der *Lambda-Funktion* 5.7.8

#### 5.4.1 Funktion `zip()`

Di Funktion `zip()` verbindet Elemente aus verschiendenen iterierbaren Objekten. Sie liefert wiederum einen Iterator, der aus den verbundenen Objekten besteht. Ein Beispiel:

```py
# Mehrere iterierbare objekte
plz = [49808, 78224, 55411]
stadt = ["Lingen", "Singen", "Bingen"]
bundesland = ["NS", "BW", "RP"]

# Verbinden
kombi = zip(plz, stadt, bundesland)

# Ausgabe
for element in kombi:
    print(element)

```
```
(49808, 'Lingen', 'NS')
(78224, 'Singen', 'BW')
(55411, 'Bingen', 'RP')
```
Zunächst werdne verschiedene iterierbare Objekte Erzeugt - in diesem Fall drei Listen, welche die Postleitzahl, die Namen und die zugehörigen Bundesländer dreier Städte enthalten.

Die Funktion `zip()` erhält als Parameter die drei iterierbaren Objekte. In der Funktion werden sie miteinander verbunden. Es wird das Objekt `kombi` zurückgeliefert. Die Elemente dieses Objekts sind (thematisch zusammengehörige) Tupel. Sie werden mithilfe einer `for`-Schleife ausgegeben.

#### 5.4.2 Funktion `map()`

Mithilfer der Funktion `map()` können Sie eine Funktion mehrfach aufrufen, jedesmal mit einem anderen Parameter. Die Funktion liefert einen Iterator, der aus den Funktionsergebnissen besteht.

```py
# Funktion mit einem Parameter

def quad(x):
    erg = x * x
    return erg

# Funktion mit mehr als einem Parameter
def summe(a,b,c):
    erg = a + b + c
    return erg

# Funktion mit einem Parameter mehrmals aurufen

z = map(quad, [4, 2.5, -1.5])

# Jedes Ergebnis ausgeben
print("Quadrat:")
for element in z:
    print(element)
print()

# Funktion mit mehr als einem Parameter mehrmals aufrufen
z = map(summe, [3, 1.2, 2], [4.8, 2], [5,0.1,9])

# Jedes Ergebnis ausgeben
print("Summe:")
for element in z:
    print(element)
```
```
Quadrat:
16
6.25
2.25

Summe:
12.8
3.3000000000000003
```
Zunächst werden zwei FUnktionen definiert:
* Die Funktion `quad()` hat einen Parameter und liefert das Quadrat dieses Werts zurück.
* Die Funktion `summe()` hat drei Parameter und liefert die Summe dieser drei Werte zurück.

Die Funktion `map()` wird zunächst mit Zwei Parametern aufgerufen:
* Der erste Parameter ist der Name der Funktion, die für die verschiedenen Werte aufgerufen wird.
* Der zweite Parameter ist ein iterierbares Objekt, in dem die Werte stehen, für die die Funktion aufgerufen wird.
* Es wird das Objekt `z` zurückgeliefert. Die Elemente des Objekts `z`sind die FUnktionsergebnisse, also die Rückgabewerte der Funktion für die verschiedenen Aufrufe.
* Diese ERgebnisse werden mithilfe einer `for`-Schleife ausgegeben.

Die Funktion `map()` wird dann mit mehr als zwei Parametern aufgerufen:
* Der erste Parameter ist nach wie vor der Name der FUnktion, die für die verschiedenen Werte aufgerufen wird.
* Der zweite und alle folgenden Parameter sind iterierbare Objekte, in denen die Werte stehen, für die die Funktion aufgerufen wird.
* Für die Bildung der ersten Summe wird aus jedem iterierbaren Objekt das erste Element (hier: 3, 4.8 und 5) verwendet. Für die Bildung der zweiten Summe wird aus jedem iterierbaren Objekt das zweite EElement (hier 1.2, 2 und 0.1) verwendet usw.
* Das kürzeste iterierbare Objekt (hier (`[4.8, 2]`)) bestimmt die Anzahl der Aufrufe. Die Funktion wird also niemals mit zu wenigen Parametern aufgerufen.
Es wird das Objekt `z` zurückgeliefert. Die Elemente des Objekts `z` sind die Funktionsergebnisse, also die RÜckgabewerte der Funktion für die verschiedenen Aufrufe.
* Diese Ergebnisse werden mithilfe einer `for`-Schleife ausgegeben.

#### 5.4.3 Funktion `filter()`

Die Funktion `filter()` untersucht Elemente eines iterierbaren Objekts mithilfe einer Funktion. Sie liefert diejenigen Elemente, für die die Funktion den Wahrheitswert `True` zurückleifert. Ein Beispiel:

```py
# Funktion, die True oder False liefert
def test(a):
    if a>3:
        return True
    else:
        return False

# Funktion mehrmals aufrufen
z = filter(test, [5,6,-2,0,12,3,-5])

# Ausgabe der werte, die True ergeben
for element in z:
    print("True:", element)
```
Der erste Parameter der Funktion `fliter()` ist der Name der Funktion, die für einen untersuchten Wert `True` oder `False` liefert. Der zweite Parameter ist das iterierbare Objekt, in diesem Fall eine Liste. Es wird ein iterierbares Objekt zurückgeliefert: die Liste `z`. Darun stehen nur noch die Elemente, für die die Funktion `True` ergibt.

### 5.5 List Comprehension
Mithilfe von *List Comprehension*  erzeugen Sie auf einfache Art und Weise eine Liste aus einer anderen Liste.

Dabei können Sie die Elemente der ersten Liste filtern und verändern.

In insgesamt drei Beispielen wird die herkömmliche Technik der Technik der List Comprehension gegenübergestellt:

```py
# Zwei Beispiellisten
xliste = [3,6,8,9,15]
print(xliste)

yliste = [2, 13, 4, 8, 4]
print(yliste)
print()

# beispiel 1: Version ohne List Comprehension
aliste = []
for item in xliste:
    aliste.append(item+1)
print(aliste)

# Beispiel 1: Version mit List Comprehension
aliste = [item + 1 for item in xliste]
print(aliste)
print()

# Beispiel 2: Version ohne List Comprehension
bliste = []
for item in xliste:
    if item > 7:
        bliste.append(item + 1)
print(bliste)

# Beispiel 2: Version mit List Comprehension
bliste = [item + 1 for item in xliste if item > 7]
print(bliste)
print()

# Beispiel 3: Version ohne List Comprehension

cliste = []
for i in range(len(xliste)):
    if xliste[i] < 10 and yliste[i] < 10:
        cliste.append(xliste[i] * 10 + yliste[i])
print(cliste)

# Beispiel 3: Version mit List Comprehension

cliste = [xliste[i]*10 + yliste[i]
          for i in range(len(xliste))
              if xliste[i] < 10 and yliste[i] < 10]
print(cliste)
```

Zunächst werden zwei Beispiellsiten gebildet. Für die Nutzung innerhalb des dritten Beispiels ist es wichtig, dass sie gleich groß sind.

In Beispiel 1 wird zunächst ohne List Comprehension gearbeitet. Es wird eine leere Liste erstellt. Anschließend wird innerhalb einer `for`-Schleife, die über jedes Element iteriert, die Ergebnislsite mithilfe der Funktion `append()` gefüllt.

Das Gleiche erreichen Sie auch mit einem einigen Schritt. der Ausdruck `aliste = [item+1 for item in xliste]` bedeutet: Liefere den Wert von `item+1` für jedes einzelne Element in `xliste`, dabei sit `item` der Name eines einzelnen Elements.

In Beispiel 2 sehen Sie, dass sie eine Liste auch filtern können. Es werden nun die Elmeente übernommen, deren Wert größer als 7 ist. Der Ausdruck `bliste = [item+1 for item in xliste if item > 7]` bedeutet: Liefer den Wert von `item+1` für jedes einzelne Element in `xliste`, aber nur, wenn der Wert des einzlenen Elements größer als 7 ist.

Beispiel 3 zeigt, dass Sie natürlich auch eine `for`-Schleife mit `range` verwenden können. Die einzelnen Listenelemente werden über einen Index angesprochen. Im Beispiel wird eine Liste aus zwei anderen, gleich langen Liste gebildet. Dabei wird eine Filterung vorgenommen.


### 5.6 Fehler und Ausnahmen

Dieser Abschnitt bietet weitergehende Erläuterungen und Programmiertechniken im Zusammenhang mit Fehler und Ausnahmen.

#### 5.6.1 Allgemeines

Während Sie ein Programm entwickeln und testen, treten häufig Fehler auf. Das ist normal und auch wichtig für den Lernprozess. Es gibt drei Arten von Fehlern: Syntaxfehler, Laufzeitfehler und logsiche Fehler:
* Syntaxfehler bemerken Sie spätestens beim Start eines Programms.
* Laufzeitfehler, also Fehler zur Laufzeit des Programms, die einen Programmabsturz zur Folge haben, können Sie mit einem `try-except` Block behandeln.
* Logische Fehler treten auf, wenn dasProgramm richtig arbeitet, aber nicht die erwarteteten Ergebnisse liefert.  Hier hat der Entwickler den Ablauf nicht richtig durchdacht. Diese Fehler sind erfahrungsgemäßg am schwersten zu finden. Dabei bietet das Debugging eine gute Hilfestellung.

#### 5.6.2 Syntaxfehler
Syntaxfehler treten zur Entwicklungszeit des Programms auf und haben ihre Ursache in falch oder unvollständig gechriebenem Programmcode. Spätestens beim Start eines Programms macht Python auf Syntaxfehler aufmerksam. Der Programmierer erhält eine MEldung und einen Hinweis auf die Fehlerstelle. Da Programm wird nicht weiter ausgeführt. Ein Beispiel für einen fehlerhaften Code:

```py
x 12

if x > 10
    print(x)
```
Nach dem Programmstart erscheint die Fehlermeldung `invalid syntax`. Im Code wird die 12 markiert, da an dieser Stelle das Gleichheitszeichen erwartet wird. Das Prgoramm läuft nicth weiter.

Nach der Verbesserung des Programms wird es erneut gestartet. Es erscheint eine weitere Fehlermeldung: Der bereich nach dem `x>10` wird markiert, da an dieser Stelle der Doppelpunkt erwaretet wird.

Nach erneuter Verbesserung des Programms wird es wieder gestartet. Es erscheint noch einmal die gleiche FEhlermeldung. Die Zeile mit `print(x` wird markiert, da als Nächstes die schließende KLammer und nicht da Ende der Datei (EOF - End of File) erwartet wird.

Erst nachdem auch der letzt Fehlerbeseitigt ist, läuft das Programm fehlerfrei bis zum Ende.

#### 5.6.3 Laufzeitfehler

Ein `try-except` Block dient zum Abfangen von Laufzeitfehlern, wie bereits in Abschnitt 3.6 >Fehler und Ausnahmen< angesprochen. Laufzeitfehler treten auf, wenn da Programm versucht, eine unzulässige Operation durchzuführen bspw. eine Division durch 0 oder das Öffnen einer nicht vorhandenen Datei. Natürlich wäre es besser, Laufzeitfehler von Anfang an zu unterbinden. Dies ist allerdings unmöglich, da es Vorgänge gibt, auf die der Entwickler keinen Einfluss hat, etwa die fehlerhafte Eingabe eines Benutzers oder eine nicht ovrhandene Datei mit Eingabedaten. Weitere Möglichkeiten zum Abfangen von Laufzeitfehlern werden in Abschnitt 5.6.6 >Unterscheidung von Ausnahmen< erläutert.

#### 5.6.4 Logsiche Fehler und Debugging

Logische Fehler treten auf, wenn eine Anweindung zwar ohne syntaxfehler übersetzt und ohne Laufzeitfehler ausgeführt wird, aber nicht das geplante Ergebnis liefert. Ursache hierfür ist ein fehlerhafter Aufbau der Programmlogik.

Die Ursache logischer Fehler zu finden ist oft schwierig und erfordert intensives Testen und Analysieren der Abläufe und Ergebnisse. Die Entwicklungsumgebung IDLE stellt zu diesem Zweck einen einfachen Debugger zur Verfügung.

##### Einzelschrittverfahren

Sie können ein Programm im Einzelschrittverfahren ablaufen lassen. Bei jedem dieser Einzelschritte können Sie sich die aktuellen Inhalte von Variablen anschauen. Als Beispiel dient ein einfaches Programm mit einer Schleife und einer Funktion:

```py
def summe(a,b):
    c = a + b
    return c

for i in range(5):
    erg = summe(10,i)
    print(erg)
```

Dieses Programms chreibt ancheinander die Zahlen von 10 bis 14 auf den Bildschirm. Öffnen Sie die Python Shell und von dort aus das Programmfenste rmit dem obigen Programm.

Sie starten den Debugger, indem Sie in der `Python Shell` im Menü `Debug` den Menüpunkt `Debugger` aufrufen. Es erscheint das Dialogfenster `Debug Control` und in der `Python Shell` die Meldung `[DEBUG ON]`.

Starten Sie nun as Programm wie gewohnt im Programmfenster über den Menüpfad `Run - Run Module` oder die Taste `F5`. Im Dialogfehld `Debug Control` wird auf die erste Zeile des Programms hingewiesen.

Jetzt können Sie auch die Schaltflächen im Dialogfeld `Debug Control` betätigen. Mit der Schaltfläche `Step` gehen Sie schrittweise dur das Programm. Mit dem nächsten Schritt gelangen Sie direkt hinter die Funktionsdefinition zur ersten ausgeführten Prorammzeile. Die Funktion wird erst beim Aufruf durchlaufen.

Durch wiederholtes Drücken der Schaltfläche `Step` können Sie nun die Schleife mehrmals durchlaufen. Dabei wird jedes Mal auch die FUnktion `summe()` durchlaufen. Im unteren Bereich des Dialogfelds `Debug Control` sehen Sie die jeweils gültigen Variablen und ihre sich ständig verändernden Werte. Befinden Sie sich im Hauptprogramm ind er Schleife, sehen Sie die Werte von `i` und `erg`.

Wenn Sie sich in der Funktion `summe()` beindne, sehen Sie die Werte von `a` und `b` und `c`.

In dr Python Shell werden parallel dazu die ersten Ergebnisse ausgegeben.

Nach dem Durchlauf der letzten Programmzeile wird noch der Hinweis `[DEBUG ON]` in der Python shell ausgegeben. IDLE befindet sich nach wie vor im Debug-Modus, aber die Schaltflächen können Sie erst nach einem erneuten Programmstart wieder betätigen.

##### Weitere Möglichkeiten
Um das Programm in etwas größeren Schritten zu durchlaufen, klicken Sie die Schaltfläche `Over`. Die Funktionen werden in diesem Fall nicht in Einzelschritten, sondern als Ganzen durchlaufen. Der Debugger sprint also über die Funktionen hinweg.

Sie können auch zwischen den beiden Möglichkeiten (Schaltfläche `Step` und schaltfläche`Over`) felxibel hin und her wechseln -  je nachdem, welchen Programmteil Sie sich ganz genau ansehen möchten.

Wenn Sie sich gerade in Einzelschritten durch eine Funktion bewegen, führt die Bestätigung der Schaltfläche `Out` dazu, dass der Rest der Funktion übersprungen und mit dem ersten Schritt anch dem Funktionsaufruf fortgefahren wird.

Die Schaltfläche `Go` lässt das PRogramm, das Sie gerade debuggen, in einem Schritt bis zum Ende laufen. Die Schaltfläche `Quit` bricht den Lauf des Programms sofort ab, ohne es zu Ende laufen zu lassen. In beiden FÄllen ist er Debug-Modus noch eingeschaltet.

Der Debug Modus lässt sich an derselben Stelle ausschalten, an der Sie ihn eingechaltet haben: In der `Python Shell` im Menü `Debug - Debugger`. In der Schell erscheint anschließend die Meldung `[DEBUG OFF]`.

Auf weniger elegante Weise können Sie den Debugger beenden, indem Sie das Dialogfeld `Debug Control` einfach schließen.

Andere Entwicklungsumgebungen für Python beiten weiter Möglichkeiten. Das setzen von `Breakpoints` (Haltepunkte) ist sehr nützlich. Diese Haltepunkte werden auf bestimmte Programmzielen gesetzt. Das Programm läuft dann in einem Zug bis zu einer solchen Programmzeile, und Sie können die aktuellen Werte überprüfen. Anschlißend durchlaufen Sie entweder im Einzelchrittverahren einen Programmbereich, in dem Sie Fehler vermuten, oder gehen direkt zum nächsen vorher gesetzten Haltepunkt.

#### 5.6.5 Fehler erzeugen

`Wieso sollte man Fehler erzeugen?`, werden Sie sich angesichts dieser Überschrift fragen. Hierfür gibt es, besonders im Zusammenhang mit der Eingabe von Daten durch einen Anwender, durchaus sinnvolle Gründe.

Im folgenden Beispiel wird der Anwender dazu aufgefordert, eine Zahl einzugeben, deren Kehrwert anschlißend berechnet wird. Diese Zahl soll allerdings positiv sein. Diese Einschränkung kann mithilfe der Anweisung `raise` bearbeitet werden:

```py
# Wiederholte Eingabe
fehler = True
while fehler:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl < 0:
            raise
        kw = 1.0 / zahl
        fehler = False
    except:
        print("Fehler")

# Ausgabe
print("Der Kehrwert von", zahl, "ist", kw)
```
Ist die eingegebene Zahl kleiner als 0, wird die Anweisung `raise` ausgeführt. Dadurch wird eine Ausnahme erzeugt, so als ob der Anwender einen der anderen möglichen Fehler gemacht hätte. Das Programm verzweigt unmittelbar zur Anweisung `except`und führt die dort angegebene Anweisung aus.

In diesem Fall handelt es sich zwar nur um einen logsichen Eingabefeheler, aber er wird genauso behandelt wie ein Fehler im Programm. Der Anwender wird somwie veranlasst, nur positive Zahlen einzugeben. Das folgene Listing zeigt eine mögliche Eingabe, zunächst dreimal mit Fehler, anschließend richtig:
```
Eine positive Zahl: 0
Fehler
Eine Postiive Zahl: abc
Fehler
Eine positive Zahl: -6
Fehler
eine positive Zahl: 6
Der Kehrwert von 6.0 ist 0.166666666666
```
Der Benutzer macht verschiedene Fehler:
* Er gibt die Zahl 0 ein. Dies führt bei der Berechnung des Kehrwerts zu einem Laufzeitfehler, einem ZeroDivisionError.
* Er gibt einen Text ein. Dies führt beim Aufruf dre Funktion `float()` zu einem Laufzeitfehler, einem `ValueError`.
* Er gibt einen negative Zahl ein. Dies führt wegen der vorgenommenen Einschränkung zu einem Laufzeitfehler.

Mithilfe der Anweisung `try`, `raise` und `except` lassen sich also auch nicht sinnvolle Eingaben des Anwenders abfangen und behandeln. Die vorgeführt Methode hat den Nachteil, dass alle Fehler gleichbehandelt werden und die Information für den Anwender im Fehlerfall noch nicht sehr genau sind. Dies wird im nächsten Abschnitt verbessert.

#### 5.6.6 Unterscheidung von Ausnahmen
Im folgenden Programm werden unteschiedliche Arten von Fehlern spezifisch abgefangen. Damit erfährt der Benutzer mehr über den Fehler, und es wird eine komfortablere Programmbedienung ermöglicht. Wiederum wird der Kehrwert einer eingegebenen Zahl ermittelt:

```py
# Wiederholte Eingabe
fehler = True
while fehler:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl == 0:
            raise RuntimeError("Zahl gleich 0")
        if zahl < 0:
            raise RuntimeError("Zahl zu klein")
        kw = 1.0 / zahl
        fehler = False
    except ValueError:
        print("Fehler: keine Zahl")
    except ZeroDivisionError:
        print("Fehler: Zahl 0 eingegeben")
    except RuntimeError as e:
        print("Fehler:", e)

# Ausgabe
print("Der Kehrwert von", zahl, "ist", kw)
```

Das Programm enthält zu einem Versuch (Anweisung `try`) mehrere spezifische Abfangmöglichkeiten (Anweisung `except`). Nachfolgend wird eine mögliche EIngabe gezeigt - zunächst dreimal mit Fehler, anschließend richtig:
```
Eine positive Zahl: 0
Fehler: Zahl gleich 0
Eine positive Zahl: abc
Fehler: keine Zahl
Eine positive Zahl: -6
Fehler: Zahl zu klein
Eine positive Zahl: 6
Der Kehrwert von 6.0 ist 0.1666666666666666666
```

Der Benutzer macht veschiedene Fehler:
* Er gibt die Zahl 0 ein. Dies führt wegen der vorgenommenen Einschränkung zu einem Laufzeitfehler. Dieser wird als allgemeiner `RuntimeError` abgefangen mit der Meldung `Fehler: Zahl gleich 0`.
* Würde die Eingabe von 0 nicht auf diese Weise abgefangen, käme es später bei der Berechnung des Kehrwerts zu einem Laufzeitfehler, einem `ZeroDivisionError`. Dieser würde abgefangen mit der Meldung `Fehler: Zahl 0 eingegeben`. Zu Demonstationszwecken wird der Fehler zweimal abgefangen.
* Der Benutzer gibt einen Text ein. Dies führt beim Aufruf der Funktion `float()` zu einem Laufzeitfehler, einem `ValueError`. Dieser wird abgefangen mit der Meldung `Fehler: keine Zahl`.
* Er gibt eine engative Zahl ein. Dies führt wegen der zweiten Einschränkung wiederrum zu einem Laufzeitfehler. Dieser wird auch als allgemeiner `RuntimeError` abgefangen mit der Meldung `Fehler: Zahl zu klein`.
* Beim Erzeugen des Fehlers mit der Anweisung `raise` werden ein Fehler (`RuntimeError`) und eine Meldung übergeben.
* Beim Abfangen dieses Fehlers mit der Anweisugn except wird ie Meldung mithilfe von `as` an die Variable `e` übergeben.

### 5.7 Funktionen

Python bietet zum Thema `Funktionen` noch einige sehr nützliche Erweiterungen, die in diesem Abschnitt erläutert werden.

#### 5.7.1 Variable Anzahl von Parametern

Bisher wird darauf geachtet, dass Reihenfolge und Anzahl der Funktionsparamter bei Definition und Aufruf miteinander übereinstimmen. Sie können aber auch Funktionen mit einer variablen Anzahl von Parametern definieren.

Bei der Definition einersolchen Funktion müssen Sie vor dem letzten (gegebenenfalls einzigen) Parameter einen `*` (Stern)  notieren. Dieser Parameter enthält ein Tupel mit den bis dahin nicht zugeordneten Werten der Parameterkette.

Im folgenden Beispiel wird eine Funktion definiert, die in der Lage ist, die Summe aller Parameter zu berechnen und auszugeben. Dies gilt unabhängig von der Anzahl der zu summierenden Werte.
```py
# Funktion
def summe(*summanden):
    print(len(summanden), "Zahlen")
    print(summanden)
    erg = 0
    for s in summanden:
        erg += s
    print("Summe:", erg)

# Aufrufe

summe(3, 4)
summe(3,8,12,-5)
```
Die (nunmehr flexiblere) Funktion wird mit zwei oder mit vier Werten aufgerufen, die zu summieren sind. ZU Demonstationszwecken weden Größe und Inhalt des Tupels ausgegeben. Die `for`-Schleife dient zur Summierung der Werte des Tupels. Die Summe wird ausgegeben.

#### 5.7.2 Benannte Parameter
Die definierte Reihenfolge der Parameter muss beim Aufruf nicht 

eingehalten werden, falls Parametermit ihrem Namen übergeben werden (benannte Parameter).

Im nachfolgenden Beispiel sind einige Variaten zum Aufruf der Funktion `volumen()` dargestellt. Diese Funktion berechnet das VOlumen eines Quaders und gibt es aus. Zudem wird die übergebene Farbe ausgegeben.

```py
# Funktion
def volumen(breite, laenge, tiefe, farbe):
    print("Werte:", breite, laenge, tiefe, farbe)
    erg = breite * laenge * tiefe
    print("Volumen:", erg, "Farbe:", farbe)

# Aufrufe
volumen(4, 6, 2, "rot")
volumen(laenge=2, farbe="gelb", tiefe=7, breite=3)
volumen(5, tiefe=2, laenge=8, farbe="blau")

# Fehler
# volumen(3, tiefe=4, laenge=5, "schwarz")
```
```
Werte: 4 6 2 rot
Volumen: 48 Farbe: rot
Werte: 3 2 7 gelb
Volumen: 42 Farbe: gelb
Werte: 5 8 2 blau
Volumen: 80 Farbe: blau
```
Der erste Aufruf findet in der bekannten Form, ohne Benennung von Parametern, statt. Die Werte werden den Parametern in der übergebenen Reihenfolge zugeordnet.

Beim zweiten Aufruf werden alle vier Paramter mit Namen übergeben. Die Reihenfolge beim Aufruf ist nicht wichtig, da die Parameter eindeutug zugeordnet werden.

Beim dritten Aufruf wird der erste Parameter über seine Stellung in der Parameterreihe zugeordnet, die anderen Parameter weren über ihre Namen zugeordnet. Es sind also auch Mischformen möglich.

Sobald allerdings das erste bennante Parameter beim Aufruf erscheint, müssen alle folgenden Paramter auch benannt sein. Daer würde beim vierten Aufruf ein Fehler bereits in der Syntax erkannt, obwohl die Zuordnung eigentlich eindeutig wäre.

#### 5.7.3 Parameter mit Vorgabewerten
Durch Vorgabewerte wird ebenfalls eine variable Parameterzahl ermöglicht. Zusätzlich können Sie benannte Parameter einsetzen. Dabei ist es wichtig, dass die nicht benannten Parameter vor den benannten Paramtern stehen.

Die Funktion zur Volumenberehcnung des Quaders wird in dieser Hinsicht geändert. Es müssen nur noch zwei Paramter angegeben werden. Die anderen beiden Parameter sind optional, es werden gegebenfalls die Vorgabewerte verwendet.

```py
# Funktion
def volumen(breite, laenge, tiefe=1, farbe="schwarz"):
    print("Werte:", breite, laenge, tiefe, farbe)
    erg = breite * tiefe * laenge
    print("Volumen:", erg, "Farbe:", farbe)

# Aufrufe
volumen(4,6,2,"rot")
volumen(2,12,7)
volumen(5,8)
volumen(4,7, farbe="rot")
```
```
Werte: 4 6 2 rot
Volumen: 48 Farbe: rot
Werte: 2 12 7 schwarz
Volumen: 168 Farbe: schwarz
Werte: 5 8 1 schwarz
Volumen: 40 Farbe: schwarz
Werte: 4 7 1 rot
Volumen: 28 Farbe: rot
```

Bei der unktionsdefinition besitzen die beiden Paramter `tiefe` und `farbe`jeweils einen Vorgabewert. Sie sind optional und müssen am Ende der Parameterreihe stehen. Es folgen die vier Aufrufe:
* Beim ersten Aufruf werden alle vier Parameter gesendet.
* Beim zweiten Aufruf wird nur einer der beiden optionalen Parameter(tiefe) gesendet. Der zweite optionale Parameter erhält deshalb den Vorgabewert.
* Beim dritten Aufruf wird keiner der opntionale Paramter gesendet. Daher erhalten beide den jeweiligen Vorgabewert.
Beim vierten Auruf wird nun der letzte optionale Parameter gesendet. Da dieser enzelne Parameter nicht mehr über die Reihenfolge zugeordnet werden kann, muss erbenannt werden.

#### 5.7.4 Mehrere Rückgabewerte

Im Unterschied zu vielen anderen Programmiersprachen können Funktionen in Python mehr als einen Rückgabewert liefern. Es kann z.B. ein Tupel oder eine Liste zurückgeliefert werden.

Im oflgenden Beispiel werden in der Funktion `geom()` die Fläche und der Umfang eines Rechtecks berechnet und als Tupel zurückgegeben.
```py
import math

# Funktion, die zwei Werte berehnet
def kreis(radius):
    flaeche = math.pi * radius * radius
    umfang = 2 * math.pi * radius
    return flaeche, umfang

# 1. Aufruf

f, u = kreis(3)
print("Fläche:", f)
print("Umfang:", u)

# 2. Aufruf

x = kreis(3)
print("Fläche:", x[0])
print("Umfang:", x[1])

# Fehler
# a, b, c = kreis(3)
```

Die Anweisung `return` liefert ein Tupel mit den beiden Ergebnissen der Funktion. An der Aufrufstelle muss ein Tupel passender Größe zum Empfang bereit stehen. Die verschiedenen Aufrufe:
* Im ersten Fall wird da Tupel zwei einzelnen Variablen zugeordnet.
* Im zweiten Fall wird da Tupel einer variablen zugeordnet, die damit zum Tupel wird.
* Der letzt Aufruf würde zu einem Laufzeitfehler führen, da die Größe des zurückgelieferten Tupels nicht passt.

#### 5.7.5 Übergabe von Kopieren und Referenzen

Werden Parameter, die an eine Funktion übergeben werden, innerhalb der Funktion verändert, wirkt sich dies im aufrufenden Programmteil unterschiedlich aus:
* Bei der Übergabe eines einfachen Objekts (Zahl oder Zeichenkette) wird eine Kopie des Objekts angelegt. Eine Veränderung der Kopie hat keine Auswirkungen auf da Original.
* Bei der Übergabe eines Objekts vom Typ Liste, Dictionary oderSet wird mit einer Referenz auf das Originalobjekt gearbeitet. Eine Veränderung über die Refernz verändret auch da Original.

Zur Verdeutlichung dieses Zusammenhangs werden im folgenden Beispiel insgesamt fünf Parameter an eine Funktion übergeben: eine Zahl, eine Zeichenkette, eine Liste, ein Dictionary und ein Set. Die Objekte weren jeweils dreimal ausgegeben:
* vor dem Aufruf der Funktion
* nach einer Veränderung innerhalb der Funktion
* nach der Rückkehr aus der Funktion

```py
# Funktion
def chg(v, zk, li, di, st):
    v = 8
    zk = "ciao"
    li[0] = 7
    di["x"] = 7
    st.discard(3)

    # lokale Ausgabe
    print("In Funktion:")
    print(v, zk)
    print(li,di,st)

# Startwerte
hv = 3
hli = [3,"abc"]
hzk = "hallo"
hdi = {"x":3, "y":"abc"}
hst = set([3, "abc"])

# Ausgabe vorher
print("vorher:")
print(hv, hzk)
print(hli, hdi, hst)

# Aufruf der Funktion
chg(hv, hzk, hli, hdi, hst)

# Ausgabe nachher
print("nachher:")
print(hv, hzk)
print(hli, hdi, hst)
```
```
vorher:
3 hallo
[3, 'abc'] {'x': 3, 'y': 'abc'} {'abc', 3}
In Funktion:
8 ciao
[7, 'abc'] {'x': 7, 'y': 'abc'} {'abc'}
nachher:
3 hallo
[7, 'abc'] {'x': 7, 'y': 'abc'} {'abc'}
```

Es zeigt sich, dass nur bei Liste, Dictionary und Set eine dauerhafte Veränderung durch die Funktion erfolgte. Dies ist je nach Problemstellung ein erwünschter oder ein unerwünschter Effekt.

Im nachfolgenden Programm wird auch die Veränderung von einfachen Objekten durch eine Funktion dauerhaft geamcht. Dabei wird die Tatsache ausgenutzt, dass Python-Funktionen mehr als einen Rückgabewert ahben können. Eine Funktion dient zum Sortieren von zwei Variablen. Sie werden als Tupel zurückgeliefert:

```py
#Sortierfunktion
def sortieren(eins, zwei):
    if eins < zwei:
        return zwei, eins
    else:
        return eins, zwei

# Beispiel 1
x = 24
y = 29

x,y = sortieren(x,y)
print("x =", x, "y =", y)

# Beispiel 2

x = 124
y = 29
x,y = sortieren(x,y)
print("x =", x, "y =", y)
```
```
x = 29 y = 24
x = 124 y = 29
```

An die Funktion werden zwei Variablen übergeben. Es wird geprüft, ob die zweite Variable größer als die erste Variable ist:
* Trifft das zu, werden beide Variablen in umgekerhter Reihenfolge an die aufrufende Stelle zurückgelieert.
* Falls nicht, stehen die beiden Variablen bereits in der gewünschten Reihenfolge und werden unverändert an die aufrufende Stelle zurückgeliefert.

An der Ausgabe erkennen Sie, dass `x` nacher in jedem Fall die größere Zahl enthält, also gegebenfalls verändert wurde.

#### 5.7.6 Lokal, global

Die Definition einer Funktion in Python erzeugt einen `lokalen` Namensraum. IN diesem lokalen Namensraum stehen alle Namen der Variablen, denen innerhalb der Funktion ein Wert zugewiesen wird, und die Namen der Variablen aus der Parameterliste.

Wird bei der Ausführung der Funktion auf eine Variable zugegriffen, so wird diese Variable zunächst im lokalen Namensraum gesucht. Wird der Name der Variablen dort nicht gefunden, wird in dem bisher bekannten globalen Namensraum gesucht, d.h. in den bisher bearbeiteten Programmzeilen außerhalb der Funktion. Wird die Variable auch dort nicht gefunden, tritt ein Fehler auf. Ein erstes Beispiel:

```py
# Testfunktion
def func():
    try: 
        print(x)
    except:
        print("Fehler")

# Hauptprogram
func()
x = 42
func()
```
```
Fehler
42
```
Der erste Aufruf von `func()` führt zu einem Fehler, da in der Funktion der Wert der Variablen `x` ausgegeben werden soll. Sie ist nicht im lokalen Namensrauf vorhanden, aber auch nicht in den bisher bearbeiteten Programmzeilen außerhalb der Funktion.

Der zweite Aufruf von `func()` führt nicht zu einem Fehler, denn die Variable `x` hat vorher außerhalb der Funktion einen Wert erhalten und ist somit im globalen Namensraum bekannt.

Das Schlüsselwort `global` dient dazu, eine Variable direkt dem globalen Namensraum zuzuordnen. Das ist im nachfolgenden Beispiel notwendig:

```py
# Erste Funktion
def eingabe():
    global x
    x = input("Zahl: ")
    x = float(x)

# Zweite Funktion
def ausgabe():
    print(x*2)

# Hauptprogramm
eingabe()
ausgabe()
```
In der Funktion `eingabe()` wird ein Wert für die Variable x eingelesen und in eine Zahl umgewandelt. Sie wird mithilfe des Schlüsselworts `global` direkt dem globalen Namensraum zugeordnet. Ansonsten wäre sie nur im lokalen Namensraum bekannt und würde daher in der Funktion `ausgabe()` weder im lokalen noch im globalen Namensraum gefunden werden. Die Zuordnung muss vor der Nutzung der Variablen erfolgen.

Testen Sie das Verhalten, indem Sie die Zeile mit dem Schlüsselwort `global` einmal kurzfirstig als Kommentar setzten.

#### 5.7.7 Rekursive Funktionen
Bestimmte Abläufe lassen sich am besten rekursiv programmieren. Eine rekursive Funktion ruft sich immer wieder selbst auf. Damit dies nicht zu einer endlosen Menge an Funktionsaufrufen führt, muss es eine Bedingung geben, die der Rekursion ein Ende setzt. Zudem wird ein erster Aufruf benötigt, der die Rekursion einleitet.

Das rinzip der Rekursion lässt sich bereits anhand des folgenden einfachen Programms verdeutlichen. Sie finden darin die rekursive Funktion `halbieren()`, die bei jedem Aufruf den ihr übergebenen Wert halbiert. Anschließend ruft sie sich selbst wieder auf, und zwar mit dem halbierten wert. Die Rekursion endet, wenn der Wert, der ständig halbiert wird, eine bestimmte Grenze unterschreitet. Der erste Aufruf der rekursiven Funktion erfolgt mit einem Startwert aus dem Hauptproram heraus.
```py
# Definition der Funktion
def halbieren(wert, i=0):
    i+= 1
    print(f"{i:3.0f}{wert:10.3f}")
    wert = wert / 2
    if wert >= 0.05:
        halbieren(wert, i)
    else:
        print(f"{i+1:3.0f}{wert:10.3f} - ENDE")

# Hauptprogramm
halbieren(10*10^10)
```
Der rekursive Aufruf erfolgt gemäßg der Bedingung `wert > 0.005`. OHne diese Bedingung würde die Rekursion endlos weiterlaufen.

#### 5.7.8 Lambda-Funktion
Die Lambda-Funktion bietet die Möglichkeit, eine Funktionsdefinition zu verkürzen. Sie können einer Lambda-Funktion Parameter übergeben. Sie liefert ihr Ergebnis als Ausdruck zurück, der in der gleichen Zeile stehen muss. Darin dürfen keine Mehrfachanweisungen, Ausgaben oder Schleifen vorkommen. Ein Beispielprogramm sieht wie folgt aus:
```py
#Funktions Definition
mal = lambda x,y: x*y
plus = lambda x,y: x+y

# Funktionsaufrufe
print(mal(5,3))
print(plus(4,7))
```
Die Lambda-Funktion `mal` hat zwei Paramter (x und y) . Das Ergebnis der Funktion ist die Multiplikation dieser beiden Paramter.

Die Lambda-Funktion 'plus' ist nach demselben Muster aufgebaut: `Ergebnis = lambda Parameterliste: Ausdruck.`

Eine Lambda-Funktion ermöglicht Ihnen zudem, eine Funktion mit Parametern an einer stelle zu übergen, an der eigentlich nur der Name einer Funktion übergeben werden darf. Dazu mehr im Abschnitt 11.3.2 - Ein einfacher Tschenrechner.

#### 5.7.9 Funktonsname als Parameter

Sie können einer FUnktion nicht nur Werte übergen, sondern auch den Namen einer anderen Funktion. Dadurch wird die erstgenannte Funktion flexibler. Ein Beispiel:

```py
# Funktion zu Berechnung einzelner Werte
def quadrat(x):
    return x * x

# Funktion zur Berechnung einzelner Werte
def hochdrei(x):
    return x * x * x

# Funktion zur Ausgabe von Funktionswerten
def ausgabe(unten, oben, schritt, f):
    for x in range(unten, oben, schritt):
        print(x, f(x))
    print()

# Aufruf, Funktionsname ist Parameter
ausgabe(2, 11, 2, quadrat)
ausgabe(1,6,1, hochdrei)
```

Zunächst werden die beiden herkömmlichen Funktionen `quadrat()` und `hochdrei()` definiert. Diese liefern jeweils als Ergebnis einen einzelnen Funktionswert zurück.

Die Funktion `ausgabe()` dien zur Ausgabe einer zweispaltigen Tabelle, die aus mehreren werten und den zugehörigen Funktionswerten besteht. Sie erwartet insgesamt vier Parameter. Die ersten drei Parameter dienen zur Steuerung der `for`-Schleife.

Der vierte Parameter gibtden Namen der Funktion an, die zur Berechnung des Werts verwendet wird, der in der zweiten Spalte der Tabelle erscheint.

Der Name der Funktion an, die zur Berechnung des Werts verwendet wird, der in der Zweiten Spalte der Tabelle erscheint. Der Name der Funktion wird ohne KLammern angegeben. IM ersten Fall handelt es sich um die FUnktion `quadrat()`, im zweiten Fall um die FUnktion `hochdrei()`.

### 5.8 Eingebaute Funktionen

Als Entwickler können Sie eine Reihe von eingebauten Funktionen ohne Einbindung eines Moduls verwenden. Die folgende Tabelle gibt eine üübersicht über die eingebauten Funktionen, die in diesem Buch behandelt werden.

|Name|Beschreibung|Beispiel in Abschnitt|
|--|--|--|
|abs()|Liefertt den Betrag einer Zahl| Abschnitt 4.1.9|
|bin()|Liefert eine binäre bzw. duale Zahl|Abschnitt 4.1.1|
|bytes()|Liefert ein Objekt des Datentyps `bytes`|Abschnitt 4.2.7 |
|chr()|Liefert ein Zeichen zu einer Unicode-Zahl|Abschnitt 5.8.2 |
|eval()|Liefert einen ausgeführten Python-Ausdruck|Abschnitt 5.1.5|
|exec()|Führt eine Anweisung aus|Abschnitt 5.1.5|
|filter()|Liefert die Elemente eines iterierbaren Objekts, für die eine FUnktion `true` ergibt|Abschnitt 5.4.3|
|float()|Liefert eine Zahlmit Nachkommestellen|Abschnitt 3.2.3|
|format()|Formatiert Zahlen und Zeichenketten|Abschnitt 5.2.2|
|frozenset()|Liefert ein unveränderliches Set|Abschnitt 4.6.4|
|hex()|Liefert eine hexadezimale Zahl|Abschnitt 4.1.1|
|input()|Wartet auf eine Eingabe des Benutzers.|Abschnitt 3.2.2|
|int()|Liefert eineganze Zahl|Abschnitt 3.2.3 |
|len()|Liefert die Anzahl der Elemente|Abschnitt 4.2.3 |
|map()|Liefert Funktionsergebnisse zu einer Reihe von Aufrufen|Abschnitt 5.4.2 |
|max()|Liefert da größte Element|Abschnitt 5.8.1|
|min()|Liefert das kleinste Element|Abschnitt 5.8.1|
|oct()|Liefert eine oktale Zahl|Abschnitt 4.1.1 |
|open()|Öffnet eine Datei zum Lesen oder Schreiben|Abschnitt 8.2 |
|ord()|Liefert die Unicode-Zahl zu einem Zeichen|Abschnitt 5.8.2 |
|print()|Erzeugt eine Ausgabe|Abschnitt 5.2.1 |
|range()|Liefert ein iterierbares Objekt über einen Bereich|Abschnitt 3.4.5 |
|repr()|Liefert Informationen über ein Objekt| Abschnitt 6.4 |
|reversed()|Liefert ein iterierbares Objekt in umgekehrter Reihenfolge|Abschnitt 5.8.3 |
|round()|Liefert eine gerundete Zahl|Abschnitt 4.1.5 |
|set()|Liefert ein Set|Abschnitt 4.6 |
|sorted()|Liefert eine sortierte Liste|Abschnitt 5.8.3|
|str()|Liefert eine Zeihenkette|Abschnitt 4.2.6|
|sum()|Lieert eine Summe der Elemente| Abschnitt 5.8.1|
|type()| Liefert den Typ eines Objekts | Abschnitt 4.1.3|
|zip()| Verbindet Elemente aus iterierbaren Objekten | Abschnitt 5.4.1 |

#### 5.8.1 Funktionen `max()`, min()`, `sum()`

Falls die Funktionen `max()` und `min()` mit einem Parameter aufgerufen werden, sollte es sich um ein iterierbares Objekt handeln. 
Die Funktionen liefern anschließend den größten bzw. den kleinsten Wert aus dem iterierbaren Objekt zurück. Werden die Funktionen dagegen mit mehreren Parametern aufgerufen, liefern sie den Wert des größten bzw. des kleinsten Parameters zurück.

Die Funktion `sum()` liefert die Summe der Elemente eines iterierbaren Objekts. Ein Beispiel zu den drei Funktionen:

```py
t = 3, 2, -7
print("Tupel:", t)
print("Max. Wert:", max(t))
print("Min. Wert:", min(t))
print("Summe:", sum(t))

print("Max. Wert:", max(11, -5, 14, 1, 2))
print("Min. Wert:", min(11, -5, 14, 1, 2))
```

Der größte und der kleinste Wert des Tupels `t` werden ausgegeben. Im Anschluss wird die Summe der Werte des Tupels ausgegeben.

Beim zweiten Aufruf der Funktionen max() und min()  ist mehr als ein Parameter angegeben.

#### 5.6.2 Funktion `chr()` und `ord()`

Die Funktion `chr()` lieert das zugehörige Zeichen zu einer Unicode-Zahl.
Umgekehrt erhalten Sie mithilfe der Funktion `ord()` die Unicode-Zahl zu einem Zeichen.
```py
# Ziffern
for i in range(48,58):
    print(chr(i), end="")
print()

# große Buchstaben
for i in range(65, 91):
    print(chr(i), end="")
print()

# kleine Buchstaben
for i in range(97,123):
    print(chr(i), end="")
print()

# Codenummern
for z in "Robinson":
    print(ord(z), end="")
print()

# Verschoben
for z in "Robinson":
    print(chr(ord(z)+1), end="")
print()
```

Die Unicode-Zahlen von 48 bis 57 verweisen auf die Ziffern 0 bis 9. Mithilfe der Unicode-Zahlen von 65 bis 90 bzw. von 97 bis 122 erhalten Sie die großen und die kleinen Buchstaben.

Eine Zeichenkette ist eine iterierbares Objekt, daher können die einzelnen Elemente (sprich Zeichen) in einer for-Schleife durhclaufen werden. Es wird jeweils die zugehörige Unicode-Zahl ausgegeben.

Im letzten Teil des Programms wird jedes Zeichen einer Zeichenkette in das codemäßig folgende Zeichen umgewandelt. Die Zeichenkette wird `verschlüsselt`. Dazu werden beide genannten Funktionen eingestzt.

#### 5.8.3 Funktionen `reversed()` und `sorted()`

Die Funktionen `reversed()` liefert die Elemente eines iterierbaren objekts in umgekerhter Reihenfolge. MIthilfeder Funktion `sorted()` wird eine sortierte Litse der Elemente eines iterierbaren objekts erstellt und geliefert. Es folgt ein Beispiel, in dem beide FUnktionen jeweilse auf eine Zeichenktte, eineTupel und ein Dictionary angewendet werden:

```py
# Zeichenkette
z = "Robinson"
print(z)
r = reversed(z)
for x in r:
    print(x, end=" ")
print()

s = sorted(z)
print(s)
print()

# Tupel
t = 4, 12, 6, -2
print(t)
r = reversed(t)
for x in r:
    print(x, end=" ")
print()
s = sorted(t)
print(s)
print()

# Dictionary
d = {"Peter":31, "Julia":28, "Werner":35}
print(d)
r = reversed(d)
for x in r:
    print(x, end=" ")
print()
s = sorted(d)
print(s)
```
Die Funktion `reversed()` liefert einen Iterator, der die Elemente in umgekehrte Reihenfolge enthält. Sie können z. B. mithilfe einer `for`-Schleife ausgegeben werden.

Die Funktion `sorted()` erstellt eine Liste, die die Elemente einer Sequenz in sortierter Reihenfolge enthält. Bei Zahlen ist die Sortierung aufsteigend nach Wert, bei Zeichen aufsteigend nach der Codenummer.

### 5.9 Statistikfunktionen

Die Statistik dient dazu, große Mengen von Zahlenwerten zu analysieren und bestimmte repräsentative Informationen über diese Zahelnwerte zu ermitteln. DIese Mengen können z.B. aus Umfragen oder aus anderen Strichproben stammen. Python bietet dazu seit der Version 3.4 einige hilfreiche Funktionen innerhalb des Moduls `statistics`. Mit Python 3.6 und Python 3.8 sind noch einige Funktionen hinzugekommen.

Ein Beispielprogramm:

```py
import statistics

# Mittelwerte einer Liste

probe1 = [5,2,4,17]
print("Aritmetischer Mittelwert:", statistics.mean(probe1))
print("Geometrischer Mittelwert:", statistics.geometric_mean(probe1))
print("Harmonischer  Mittelwert:", statistics.harmonic_mean(probe1))
print()

# Median
print("Median:", statistics.median(probe1))
probe2 = [5,2,4,17,3]
print("Median:", statistics.median(probe2))
print()

# Unterer Median
print("Unterer Median:", statistics.median_low(probe1))
print("Unterer Median:", statistics.median_low(probe2))
print()
# Oberer Median

print("Oberer Median:", statistics.median_high(probe1))
print("Oberer Median:", statistics.median_high(probe2))
print()

# Modus
probe3 = [3,5,5,12,17,17]
print("Modus:", statistics.mode(probe3))
print("Multimodus:", statistics.multimode(probe3))
print()

# Tupel, Werte eines Dictionary
probe4 = 5,2,4,17
print("aus Tupel", statistics.mean(probe4))
probe5 = {"D":5, "NL":2, "CH":4, "F":17}
print("aus Dictionary:", statistics.mean(probe5.values()))
```
```
Aritmetischer Mittelwert: 7
Geometrischer Mittelwert: 5.1065457621381
Harmonischer  Mittelwert: 3.9650145772594754

Median: 4.5
Median: 4

Unterer Median: 4
Unterer Median: 4

Oberer Median: 5
Oberer Median: 4

Modus: 5
Multimodus: [5, 17]

aus Tupel 7
aus Dictionary: 7
```
Die werte der Zahlenmengekönnen ganzzahlig sein oder auch Nachkommastellen haben. Sie können aus einer Liste (wie hier), aber auch aus einem Tupel oder einem Dictionary stammen, siehe unten. Sie müssen nicht in sortierter Reihenfolge vorliegen.

Die Funktion `mean()` liefert den aritmetrischen Mittelwert, also die Summe der Werte, geteilt durch ihre Anzahl. Im vorliegenden Beispiel entspricht das:
`(5+2+4+17)/4`.

Seit Python 3.8 gibt es die Funktion `geometric_mean()`. Sie leifert den geometrischen Mittelwert. Er entspricht der n-ten Wurzel des Produkts von n werten. Im vorliegenden Beispiel entspricht das der vierten Wurzel aus (5 * 2 * 4 * 17).

Seit Python 3.6 gibt es die Funktion `harmonic_mean()`. Sie liefert den harmonischen Mittelwert. Er entspricht der Anzahl der Werte, geteilt durch die Summe der Kehrwerte der Werte. Im vorliegenden Beispiel entspricht das 4/(1/5 + 1/2 + 1/4 + 1/17).

Einige Anwendungsbeispiele für die verschiedenen Mittelwerte finden Sie über https://de.wikipedia.org/wiki/Mittelwert.

Die Funktion `median()` lieert den Median. Dieser wird auch Zentralwert genannt, da er im Zentromd er Zahlenmenge steht. Es gbit genauso viele Werte, die größer sind als der Median, wie werte, die kleienr sind als der median. Bei einer ungeraden Menge von Werten handelt es sich beim Median um da Element in der Mitte der Zahlenmenge. Bei einer geraden Menge von Werten handelt es sich um den aritmetischen MIttelwert der beiden Elemente in der Mitte der Zahlenmenge.

Die Funktion `median_low()` und `median_high()` liefern den unteren bzw oberen Median. Dabei handelt es sich in jedem Fall um Elmeente aus der Zahlenemenge. Bei einer ungeraden Menge von Werten ist es ds Element in der Mitte der Zahlenmenge. Bei einer geraden Menge von Werten handelt es sich um die beiden Elemente in der Mitte der Zahlenmenge.

Die Funktion `mode()` liefert denjenigen Wert, der in der Zahlenmenge am häufigsten vorkommt. Besitzen mehrere Werte die größte Häufigkeit, wird derjenige Wert genannt, der als erster vorkommt. Seit Python 3.8 gibt es die FUnktion `multimode()`. Sie liefert eine Liste mit allen Werten, die die größte Häufigkeit besitzen.

Die untersuchte Zahlenmenge kann auch aus einem Tupel oder, mithilfe der Methode `values()`, aus der Werte-View eines Dictionary stammen.

### 5.10 Eigene Module

Bisher werden die Funktion und das eigentliche Hauptprogramm in der gleichen Datei definiert. Bei spezifischen Funktionen, die auf ein bestimmtes Programm zugesnitten sind, ist dies auch sinnvoll.

Allerdings werden Sie bald feststellen, dass einige nützliche Funktionen immer wieder und von verschiedenen Programmen aus benötigt werden. Diese Funktionen sollten Sie in eigenen Modulen speichern. Die Erstellung und Nutzung von Modulen ist in Python sehr einfach und wird in diesem Abschnitt erläutert.

#### 5.10.1 Eigene Module erzeugen

Zur Erzeugung eines Moduls speichern Sie die gewünschte Funktion einfach in einer eigenen Datei. Der Name der Datei ist zugleich der Name des Moduls. Die Funktion erstellen Sie wie gewohnt:

```py
def quadrat(x):
    erg = x * x
    return erg
```

Anschließend können Sie die Funktion in jedem Programm nutzen. Voraussetzung dafür ist ihr Import aus dem betreffenden Modul. Es gibt verschiende Importmöglichkeiten, die ich im Folgenden Beschreibe.

#### 5.10.2 Standard-Import eines Moduls
Sie importieren das Modul we gewohnt.

```py
import modul_neu
z = modul_neu.quadrat(3)
```
Alle Funktionen des Moduls `modul_neu`, also der Datei modul_neu.py, werden mit der Anweisung `import` zugänglich gemacht. Die Funktion `quadrat()` wird wie folgt aufgerufen:

```py
Modulname.Funktionsname
```

#### 5.10.3 Import eines Moduls mit Umbenennung

Falls das Modul einen langen, unhandlichen Namen hat, können Sie es mithilfe von `as` in Ihrem Programm umbennen.

```py
import modul_neu as mn
z = mn.quadrat(3)
print(z)
```

Sie können auf das Modul `modul_neu` innerhalb dieses Programmes mithilfe von `mn` zugreifen.

#### 5.10.4 Import von Funktionen
Sie importieren nur die Funktionen mit der Aneisung `from`.
```py
from modul_neu import quadrat
z = quadrat(3)
print(z)
```

Die Funktion `quadrat()` wird Mithilfe der Anweisung `from` aus dem Modul `modul_neu` importiert. Sie können sie anschließend ohne den Modulnamen aufrufen, so als ob sie in der gleichen Datei definiert wäre.

Sie können auch alle Funktionen aus dem Modul `modul_neu` auf einmal importieren. Die Anweisung lautet dann:
```py
from modul_neu import *
```

Der Import mithilfe der Anweisung `from` wird nur der Vollständigkeit halber ewähnt. Diese Möglichkeit wird nicht mehr empfohlen und darf auch nicht in Funktionen, sondern nur auf Modulebene genutzt werden. Sie erweist sich außerdem als ungünstig, falls Sie mehrere Funktionen mit gleichem Namen aus unterschiedlchen Modulen importieren möchten.

*Hinweis*
In den Beispielen wird davon ausgegangen, dass sich die Datei des zu importierenden Moduls im selben Verzeichnis befindet.

### 5.11 Parameter der Kommandozeile
Ein Pyhon-Programm kann bekanntlich von der Kommandozeile des Betriebssystems aus aufgerufen werden. In Abschnitt 2.3.2 "Ausführen unter Windows"/2.3.3 "Ausführen unter Linux/macos" wird beschrieben, wie Sie zur Kommandozeile/Terminals gelangen.

Der Aufruf ähnelt dem Aufruf einer Funktion mit Parametern. Die einzelnen Parameter werden durch Leerzeichen voneinander getrennt. Sie stehen innerhalb des Programms in der Liste `argv` aus dem Modul `sys` zur Verfügung. Die Anzahl der Parameter könnten Sie mithilfe der eingebauten Funktion `len()` (Länge der Lsite) ermitteln.

#### 5.11.1 Übergabe von Zeichenketten

Dem folgenden Programm wird genau ein Wort als Parameter übergeben. Anschließend werden die Elemente de Liste `sys.argv` ausgegeben:

```py
import sys
print("Programmname: ", sys.argv[0])
print("Erster Parameter:", sys.argv[1])
```

Wird das Programm von der Kommandozeile aus wie folgt aufgerufen

```
python kommando_text.py hallo
```
lautet die Ausgabe:
```
Programmname: kommando_text.py
ErstesParameter: hallo
```

Das erste Element der Liste ist der Name des Programms. Die weitern Elemente sind die einzelnen Parameter.

#### 5.11.2 Übergabe von Zahlen

Im folgenden Programm werden zwei Zahlen addiert, die in dem Programm als Kommandozeilenparameter übergeben wreden. Dazu müssen die Parameter mithilfe der Funktion `float()` in Zahlen umgewandelt und eventuell auftretende Ausnahmen abgefangen werden.

```py
import sys

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = x + y
    print("Ergebnis:", z)
except:
    print("Parameterfehler")
```

Wird das Programm vom Betriebssystem aus wie folgt aufgerufen...
```
python kommando_zahl.py 3 6.2
```
... lautet die Ausgabe:
```
Ergebnis: 9.2
```

#### 5.11.3 Beliebige Anzahl von Parametern
Im folgenden Programm wird eine beliebige Menge von Zahlen adiert, die als Kommandozeilenparamter übergeben werden.

```py
import sys
summe = 0

try:
    for i in sys.argv[1:]:
        summe += float(i)
    print("Ergebnis:", summe)
except:
    print("Parameterfehler")
```
```
python kommando_variabel.py 3 10 6.2 5 1 23 5 123
```
```
('Ergebnis:', 176.2)
```
Bei `sys.argv` handelt es sich um eine Liste. Das erste Element (der Name des Programms) darf nicht in die Rechnung einfließen, daher die `Slice-Operation`.  Innerhalb der `for`-Schleife werden die einzelnen Parameter umgewandelt und zur Summe addiert.

### 5.12 Programm `Bruchtraining`

Diesen Abschnitt können Sie bei Bedarf überspringen. Als einziges neues Element wird die Funktion `choice()` aus dem Modul `random` eingeführt, die ein zufällig ausgewhältes Element aus einer Sequenz liefert. Das Programm pruchtraining.py beinhaltet ein Trainingsprogramm zur Bruchrechnung mit drei Schwierigkeitsgraden.

Es dient IHnen als Beispiel für das Zusammenspiel vieler bereits bekannter Elemente, wie z.B. mehrfache Verzweigungen, Schleifen, Ausnahmebehandlung, Tupel und Funktionen mit mehren Rückgabewerten. Sowohl der Zähler als auch der Nenner der vorkommenden Brüche können positiv oder negativ sein.

#### 5.12.1 Der Ablauf des Programms

Zur Verdeutlichung wird zunächst der Ablauf des Programms mithilfe von einigen Beispieleingaben erläutert:

```
Ihre Wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende
1
Ganze Zahl berechnen: 9/-1
Ergebnis: -9
Ihre Wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende
2
Bruch kürzen: -30/-70
Ergebnis: 3/7
Ihre Wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende
3
Ergebnis-Bruch Berechnen: -21 / 14 / -15 / 25
Ergebnis: 5 / 2
Ihre Wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende
0
```

Nach dem Start des Programms erscheint ein Menü für den Benutzer, mit dem eine leichte Aufgabe (Eingabe:1), eine mittelschwere Aufgabe oder eine schwere Aufgabe ausgewählt werden kann. Nach dem Bearbeiten einer Aufgabe erscheint wiederum das Menü. Hier kann der Benutzer entweder eine weitere Aufgabe auswhälen oder das Programm beenden.

Nach der Auswahl einer leichten Aufgabe wird ein Bruch angezeigt, der eine ganze Zahl ergibt. Der Bruchstrich wird durch einen Divisonsstrich zwischen Zähler und Nenner dargestellt. Der Benutzer rechnet, im KOpf oder auf dem Papier, die ganze Zahl aus, die das ERgebnis der Aufgabe darstellt. Nach dem Bestätigen der Taste `Enter` erscheint das richtige ERgebnis, mit dem der Benuetzer sein eigenes Ergebnis vergleicht. Stellt der Beneutzer fest, dass er zB. 20 leichte Aufgaben richtig lösen konnte, kann  er als Nächstes eine mittelschwere Aufgabe auswhälen.

Nach der Auswahl einer mittelschweren Aufgabe wird ein Bruch angezeigt, den der Benuetzer kürzen soll, und zwar auf den kleistmöglichen Bruch. Der Benuetzer rechnet, im KOpf oder auf dem papier, den gekürzten Bruch aus. Nach dem Betätigen der Taste Enter erscheint wiederum das richtige Ergebnis, mit dem der Benuetzer sein eigenes Ergebnis vergleicht. Stellt der Benuetzer fest, dass er zB. 20 mittelschwere Aufgaben richtig lösen konnte, kann er als nächstes eine schwere Aufgabe auswählen.


Nach der Auswahl einer schweren Aufgabe werden zwei Brücke angezeigt, die der Benuetzer entweder miteinander addieren, subtrahieren, dividieren oder multiplizieren soll. Das Ergebnis soll er anschließend kürzen. Der Beneutzer  rechnet auch hier, im Kopf oder auf dem Papier, den gekürzten Bruch aus. Nach dem Betätigen der Taste Enter erscheint auch hier das richtige ERgebnis, mit dem der Benuetzer sein eigenes Ergebnis vergleicht.

#### 5.12.2 Hauptprogramm

Das Programm wird in einzelnen Teilen erläutert. Zunächst folgt das Hauptprogramm, das am Ende der Datei steht:

```py
while 1:
    #Eingabemenü
    fehler = 1
    while fehler == 1:
        print()
        print("Ihre wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende")
        try:
            wahl = int(input())
            fehler = 0
            if wahl < 0 or wahl > 3:
                fehler = 1
                print("Bitte nur 0, 1, 2 oder 3 eingeben")
        except:
            print("Bitte nur 0,1,2 oder 3 eingeben")

    if wahl == 0:
        break
    elif wahl == 1:
        leicht()
    elif wahl == 2:
        mittel()
    else:
        schwer()
```
Das Menü für den Benutzer und seine Eingabe sind in einer äußeren Endlosschleife eingebettet, die nur mit der Eingabe von 0 verlassen werden kann.

Die Anzeige des Menüs ist in einer inneren Schleife eingebettet. Nimmt der Benutzer eine Eingabe vor, die nicht in eine ganze Zahl umgewandelt werden kann, erscheint dank einer Ausnahmebehandlung eine Fehlermeldung, und es wird wiederum das Menü angezeigt. Gibt der Benutzer eine Zahl ein, die keinem Wert im Menü entspricht, wird mithilfe der Variable `fehler` dafür gesorgt, dass eine Fehlermeldung erscheint, und es wird wiederum das Menü angezeigt.

Gibt der Benutzer eine hültige Zahl ein, wird eine der drei Funktionen `leicht()`, `mittel()`, `schwer()` aufgerufen oder es wird die äußere Endlosschleife verlassen.

#### 5.12.3 Eine leichte Aufgabe

Es folgt die Funktion `leicht()` zur Erstellung einer leichten Aufgabe. Das gesamte Programm benötigt zudem einen initialisierten Zufallsgenerator:

```py
import random
random.seed()
...

def leicht():
    ergw = random.randint(-10,10)
    an = 0
    while an == 0:
        an = random.randint(-10,10)
    az = ergw * an
    print("Ganze Zahl berechnen:", az, "/", an)
    input()
    print("Ergebnis:", ergw)
```

Der Zufallsgenerator liefert ganze Zahlen für as Ergebnis (ergw) und den Nenner des Bruchs (an). Der Zähler des Bruchs (az) wird dann mithilfe einer Multiplikation ermittelt. Ein Beispiel: Das zufällig ermittelte Ergebnis 3 und der zufällige ermittelte Nenner 5 erben den Zähler 15. Für den Benutzer wird also die Aufgabe 15 / 5 ermittelt und ausgegeben. Er soll das Ergebnis 3 berechnen.

Bei dem eingestellten Bereich von -10 bis 10 kann der Zufallsgenerator auch den Wert 0 liefern. Mithilfe einer `while`-Schleife wird dafür gesorgt, dass der Wert für den Nenner nicht 0 ist, weil eine Division durch 0 mathematisch nicht erlaubt ist.

#### 5.12.4 Eine mittelschwere Aufgabe

Es folgt die Funktion `mittel()` zur Erstellung einer mittelschweren Aufgabe. Sie benötigt die beiden Tupel `prim` und `prob` und die Hilfsfunktionen `produkt()`, `kuerzen()` und `ergebnis()`:

```py
prim = 2,3,5,7

prob = 2,2,2,2,3,3,3,5,5,7

def produkt(anzahl):
    wert = 1
    for i in range(anzahl):
        wert *= random.choice(prob)
    if random.randint(0,1) == 0:
        return wert
    else:
        return -wert

def kuerzen(ergz, ergn):
    for p in prim:
        while ergz%p == 0 and ergn%p == 0:
            ergz /= p
            ergn /= p
    if ergn < 0:
        ergz = -ergz
        ergn = -ergn
    return int(ergz), int(ergn)

def ergebnis(ergz, ergn):
    ergz, ergn = kuerzen(ergz, ergn)
    if ergn == 1:
        print("Ergebnis:", ergz)
    else:
        print("Ergebnis:", ergz, "/", ergn)

def mittel():
    ergz = produkt(3)
    ergn = produkt(3)
    print("Bruch kürzen:", ergz, "/", ergn)
    input()
    ergebnis(ergz, ergn)
```

Die Variablen `ergz` und `ergn` beinhalten den Zähler und den Nenner des gekürzten Bruchs: MIt diesem Bruch vergleicht der Benuetzer das ERgebnis seiner eigenen Berechnung.

Das Tupel `prim` beinhaltet als Elemente die vier kleinsten Priemzahlen. Primzahlen können nur duch sich selbst und durch 1 geteilt werden. Sie werden zum Kürzen des Bruchs benötigt, mehr dazu später.

Das Tupel `prob` beinhaltet zehn Elemente. Dabei handelt es sich ebenfalls um die vier kleinsten Primzahlen, allerdings mit unterschiedlicher Häfugkeit: Die 2 kommt zB. vier mal vor, die 7 nur einmal.

Der Zähler un der Nenner eines Bruchs werden jeweils mithilfe der Funktion `produkt()` erzeugt. Sie liefert einen wert der mithilfe des Zufallsgenerators erzeugt wird. Die `for` schleife wir dreimal durchlaufen. Bei jedem Durchlauf liefert die Funktion ` choice()` aus dem Modul `random`einen der Werte aus der Tupel `prob`. Dabei handelt es sich um einen der Werte 2,3,5,7, aber auch mit unterschiedlicher Wahrscheinlichkeit (probability). Auf diese Weise wird dafür gesorgt, dass die Aufgaben eher kleinere als größere Zahlen beinhalten.

Die drei Werte werden miteinander multipliziert. Anschließend wird, wiederum mithilfe des Zufallsgenerators das vorzeichen des ermittelten Produkts gesetzt. Liefert der Zufallsgenerator eine 0, bleibt da Produkt positiv. Liefert er eine 1, wird das Produkt mit -1 multipliziert.

Zur Anzeige des Ergebnisses wird die Funktion `ergebnis()` aufgerufen, die wiederum zunächst die FUnktion `kuerzen()` aufruft. Darin werden Zähler und Nenner nacheinander durch die Elemente des Tupels `prim` dividiert. Dabei werden sie jeweils so lange durch eine der Primzahlen dvidiert, wie der Rest der Divison 0 ist, die Division also eineganze Zahl ergibt. Da Zähler und Nenner nur PRodukte aus den vierZahlen des Tupels `prim` sind, ergibt sich am Ende der gekürzte Wert.

Ist das Ergebnis ein negativer Bruch, soll das Vorzeichen im Zähler stehen. Sind sowohl Zähler als auch Nenner negativ, soll der Bruch in den entsprechenden positiven Bruch umgewandelt werden. Ist also de Nenner negativ, werden Zälher undNenner mit -1 multipliziert. Zwei Beispiele: Aus 4/-3 wird -4/3, aus -4 / -3 wird 4/3.

Nach Rückkehr in die Funktion èrgebnis()` wird dafür gesorgt, dass das Ergebnis al ganze Zahl und nicht als Bruch angezeigt wird, falls der Nenner den Wert 1 besitzt.

#### 5.12.5 Eine Schwere AUfgabe

Es folgt die FUnktion `schwer()` zum Erstellung einer schweren Aufgabe. Sie benötigt zusätzlich das Tupel `ops`:

```py
ops = '+', '-', '*', '/'

def schwer():
    az = produkt(2)
    an = produkt(2)
    bz = produkt(2)
    bn = produkt(2)
    op = random.choice(ops)
    print("Ergebnis-bruch berechnen: ", az, "/", an," ", op," ", bz, "/", bn, sep="")

    if op == '+':
        ergz = az * bn + an * bz
        ergn = an * bn
    elif op == '-':
        ergz = az * bn - an * bz
        ergn = an * bn
    elif op == '*':
        argz = an * bz
        argn = an * bn
    else:
        ergz = az * bn
        ergn = an * bz

input()
ergebnis(ergz, ergn)
```

Das Tupel `ops` beinhaltet als Elemente vier einzelne Zeichen, nämlich die OPeratoren für die vier verschiedenen Berechnungen.

Der Zähler und Nenner der beiden Brücke, nennen wir sie A und B, werden mithilfe der bereits beschriebenen Funktion  `produkt()` erzeugt. Die rbruch A hat den Zähler `az` und den Nenner `an`, der Bruch B den Zähler `bz` und den Nenner `bn`. Die vier Werte sind jeweils das Produkt aus zwei zufälligen Zahlen. Der Poerator für die Aufgabe wird ebenfalls per Zufallsgenerator erzeugt. Anshließend wird die Aufgabe in der Form  `A Operator B` angezeigt.

Mithilfe einer mehrfachen Verzweigung wird das Ergebnis in Abhängigkeit des Operators gemäß den Regeln der Bruchrechnung ermittelt. Auch hier beinhalten die Variablen `ergz`und `ergn` den Zhäler und den Nenner des Ergebnisses.

Die Funktion `ergebnis()` und `kuerzen()` erfüllen dieselben Aufgaben wie im vorherigen Abschnitt.



## 6 Objektorientierte Programmierung

Dieses Kapitel bietet Ihnen eine Einführung in die objektorientierte Programmierung (OOP). Es erläutert die Möglichkeiten zur Erzeugung einer Kkassenhierarchie, mit der Sie große Softwareprojekte anhand von **Klassen**, **Objekten**, **Eigenschaften**, **Methoden** und des **Prinzips der Vererbung** bearbeiten können.

### 6.1 Was ist OOP?

Die *objektorientierte Programmierung* bietet zusätzliche Möglichkeiten zum verbesserten Aufbau und zur vereinfachten Wartung und Erweiterung von Programmen. Diese Vorteile erschließen sich besonders in großen Programmierprojekten.

Bei der objektorientierten Programmierung werden **Klassen** erzeugt, in denen die Eigenschaften von Objekten sowie die Funktionen festgeletzt werden, die auf diese Objekte angewendet werden können (sogenannte *Methoden*). 
Sie können verschiedene **Objekte** dieser Klassen erzeugen, den Eigenschaften unterschiedliche Werte zuweisen und die Methoden auf die Objekte anwenden. Die Definitionen aus der Klasse und die zugewiesenen Werte begleiten die Objekte über ihren gesamten *Lebensweg* während der Dauer des Programms.

Ein Beispiel: Es wird die Klasse `Fahrzeug` erschaffen, in der die Eigenschaften und die Methoden von Fahrzeugen bestimmt werden. Ein Fahrzeug hat u.a. die Eigenschaften `Bezeichnung`, `Geschwindigkeit` und `Fahrtrichtung`. Außerdem kann man ein Fahrzeug `beschleunigen` und `lenken`. INnerhalb des Programms können viele unterschiedliche Fahrzeuge erschaffen und eingesetzt werden.

Klassen können ihre Eigensahften und Methoden außerdem vererben. Eine solche Klasse fungiert als `Basisklasse`, ihre Erben nennt man `abgeleitete Klassen`. Damit kann die Definition von ähnlichen Objekten, die über eine Reihe von gemeinsamen Eigenschaften und Methoden verfügen, vereinfacht werden.

Ein Beispiel: Es werden die Klassen `PKW` und `LKW` geschaffen. Beide Klassen sind von der Basisklasse `Fahrzeug` abgeleitet und erben alle Eigenschaften und Methoden dieser Klasse. Zusätzlich verfügen sie über eigene Eigesncahften und Methoden, die bei der jeweiligen Klasse besonders wichtig sind. Ein `PKW` hat etwa eine bestimmte Anzahl von `Insassen`, und man kann `einsteigen` und `aussteigen`. Ein `LKW` hat eine `Ladung`, man kann ihn `beladen` und `entladen`.

### 6.2 Klassen, Objekte und eigene Methoden

Als Beispiel wird die Klasse `Fahrzeug` deiniert. Zunächst verfügt ein Objekt dieser Klasse nur über die Eigenschaft `Geschwindigkeit` und die MEthoden `beschleudigen()` und `ausgabe()`. Die Methode `ausgabe()` informiert den Anwender über den aktuellen Zustand des jeweiligen Fahrzeug-Objekts.

Die Definition der Klasse sieht wie folgt aus:
```py
# Definition der Klasse Fahrzeug

class Fahrzeug:
    geschwindigkeit = 0                 # Eigenschaft
    def beschleunigen(self, wert):      # Methode
        self.geschwindigkeit += wert
    def ausgabe(self):                  # Methode
        print("Geschwindigkeit:", self.geschwindigkeit)
```

Die Definiton der Klasse wird eingeleitet vom Schlüsselwort `class`, gefolgt vom Namen der Klasse und einem Doppelpunkt. Eingerückt folgt die eigentliche Definiton. Die Eigenschaft `geschwindigkeit` wird definiert und au den Wert `0` gesetzt.
Die Methoden sind Funktionen der Klasse, sie werden also mithilfe des Schlüsselworts `def` definiert. Methoden haben mindestens einen Parameter, nämlich das Objekt selbst. Häufig wird dieser Parameter `self` genannt - sie können aber auch einen anderen Namen wählen.

Die Methode `beschleunigen()` hat insgesamt zwei Paramter: Der erste Parameter ist das Objekt selbst. Der zweite Parameter ist der Wert für die Änderung der Geschwindigkeit. Innerhalb der Methode wird dieser Wert genutzt, um die Eigenschaft des Objekts zu ändern. Die Methode `ausgabe()`hat nur einen Paramter: das Objekt selbst. Sie dient zur Ausgabe er Geschwindigkeit des Objekts.

Bisher enthielt das Programm nur eine Klassendefinition, es führte noch nichts aus. Da Hauptprogramm hat folgendes Aussehen:

```py
# Objekte der Klasse Fahrzeug erzeugen

opel = Fahrzeug()
volvo = Fahrzeug()

# Objektmehtoden
volvo.ausgabe()
volvo.beschleunigen(20)
volvo.ausgabe()

# Objekt betrachten
opel.ausgabe()
```

Im Hauptprogramm werden zunächst zwei Objekte der Klasse  `Fahrzeug` erzeugt, hier mit den Namen `opel` und `volvo`. Diesen Vorgang nennt man auch: Instanzen einer Klasse erzeugen.

Beim anschließenden Aufruf der Methoden ist zu beachten, dass das Objekt selbst nicht mehr als Parameter angegeben wird. Eine Methode bekommt also beim Aufruf immer einen Paramter weniger übermittelt, als in der Definition angegeben ist. Dies leigt daran, dass die Methode *für* ein bestimmtes Objekt aufgerufen wird. Innerhalb der Methode ist daher bekannt, um welches Objekt es sich handelt.

Die Geschwindigkeit des Objekts `volvo` wird ausgegeben, einmal vor und einmal nach der Beschleunigung. Die Geschwindekeit es Objekts `opel` wird nu einmal ausgegeben. Zu Beginn, also nach ihrer Erzeugung, haben dieObjekte laut der Klassendefinition die Geschwindigkeit 0.

**Hinweis**
Die in diesem Kapitel dargestellten Programme sind ein Kompromiss, denn die Vorteile der objektorientierten Programmierung (OOP) kommen erst bei gröeßren Programmierprojekten zum Tragen. Bei einem kleinen Projekt ist die Frage berechtigt, warum für dieses einfache Ergebnis ein verhältnismäßig komplexes Programm geschrieben werden sollte. Anhand dier hier vorgestellten Programme können Sie sich aber die Prinzipien der OOP reschließen, ohne den Überblick zu verlieren.

### 6.3 Konstruktor und Destruktor

Es gbit zwei besondere Methoden, die im Zusammenhang mit einer Klasse definiert werden können:

* Die Konstruktormethode wird genutzt, um einem Objekt zum Beginn seiner *Lebensdauer* Anfangswerte zuzuweisen. Dabei können Sie mit Vorgabewerten(5.7.3) und benannten Parametern(5.7.2) arbeiten. Auf diese WEise können objekte ihre Anfangswerte auf unterschiedliche Art und WEise erhalten.
* Die Destruktor wird genutzt, um am Ende der *Lebensdauer* eines Objekts Aktionen auszulößen, zB. eine offene Datei zu schließen.

Die Klasse `Fahrzeug` wird wie folgt verändert: Ein Fahrzeug erhält neben der Eigenschaft `geschwindigeit` die Eigenschaft `bezeichnung`. Die Klasse erhält eine Konstruktormethode, um Anfangswerte für `geschwindigkeit` und `bezeichnung` festzulegen.

Das Programm sieht in seiner veränderten Form wie folg aus:

```py
# Definition der Klasse Fahrzeug

class Fahrzeug:
    # Konstruktormethode
    def __init__(self, bez="(leer)", ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    # Destruktormethode
    def __del__(self):
        print("Objekt", self.bezeichnung, "entfernt")

    # Methoden

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
        self.ausgabe()

    def ausgabe(self):
        print(self.bezeichnung, self.geschwindigkeit, "km/h")


# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)
ford = Fahrzeug("Ford Mondeo")
mercedes = Fahrzeug(ge=60)
# Objekte betrachten
opel.ausgabe()
volvo.ausgabe()
ford.ausgabe()
mercedes.ausgabe()
# Objektmethode
volvo.beschleunigen(20)
# Destruktor aufrufen
del opel
del volvo

# Aufruf nicht mehr gestattet
# opel.ausgabe()
```

Der festgelegte Name `__init__()` (mit doppeltem Unterstrich davor und danach) bezeichnet die Konstrutkromethode. Es werden zwei Parameter übergeben. Diese beiden Parameter werden genutzt, um die beiden Eigenschaften mit anfangswerten zu versorgen. Bei den Objekten `opel` und `volvo` werden Werte für beide Eigenschaften übergeben.

Beim Objekt `ford` wird nur ein Wert für die erste Eigenschaft übergeben. Die zweite Eigenschaft erhält den Vorgabewert. Beim Objekt `mercedes` wird nur ein Wert für die zweite Eigenschaft übergeben, mithilfe eines beanannten Parameters. In diesem Fall erhält die erste Eienshaft den Vorgabewert.

Der festgelegte Name `__del__()` bezeichnet die Destruktormethode. Sie wird mithilfe des Schlüsselwrots `del` aufgerufen. Anschließend existiert das Objekt nicht mehr.

Die Methode `ausgabe()` dient zur Ausgabe beider Eigenschaften. Sie wird in diesem Programm sowohla us dem Hauptprogramm als auch aus einer Objektmethode heraus aufgerufen. Innerhalb der Klassendefinition muss, wie bei der Zuweisung eines Eigenschaftswerts, das Objekt mit `self` angegeben werden.

Es werden zwei Objekte erzeugt. Dabei werden die Anfangswerte an den Konstruktor übergeben, hier die Werte `Opel Admiral` und `40` für das Objekt `volvo`.

Die Eigenschaften der Objekte werden verändert und ausgegeben.

**Hinweis**
Konstruktoren werden häufig eingesett. Sie ermöglichen eine gezieltere Erzeugung von Objekten. Destruktoren kommen seltener zum Einsatz.

Sollten Sie bereits mit anderen Programmiersprachen gearbeitet haben, ist dieser Hinweis interessant: Methoden können, wie auch Funktionen, in Python nicht überladen werden. Falls sie eine Methode mehrfach definieren, gegebenenfalls mit unterschiedlichen Parametern, so gilt nur die jeweils letzte Definition. Methoden können allerdings in abgeleiteten Klassen überschrieben werden, siehe Abschnitt 6.7 Vererbung.

### 6.4 Besondere Methoden

Die Methoden `__init__()` und `__del__()` gehören zu einer Reihe von besonderen Methodne, die für die eingebauten Objekttypen bereits vordefiniert sind. Sie können siefür eigene Objekttypen,a lso Klassen, selbst definieren. Im folgenden Beispiel sehen Sie zwei dieser Methoden:

```py
# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):    # Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):              # Ausgabemethode
        return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"
    def __repr__(self):             # Info-Methode
        return "Objekt: " + self.bezeichnung + " der Klasse Fahrzeug"
    

# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)

# Objekte ausgeben
print(opel)
print(volvo)

# Informationen zu Objekt
print(repr(opel))
print(repr(volvo))
```

Bei der Ausgabe einesObjekts mithilfe der Funktion `print()` wird die besondere Methode `__str__()` aufgerufen, falls sie definiert ist. Diese liefert standartmäßig eine Zeichenkette zur Ausgabe der Eigenschaften. Ist die Methode für die betreffende Klasse nicht definiert, ergibt sich keine sinnvoll nutzbare Ausgabe.

Sie können mithilfe der eingebauten Funktion `repr()` Informationen zu einem Objekt abrufen. Das Aussehen dieser Informationen können Sie selbst bestimmen, falls Sie innerhalb der Klassendefinition die besondere Methode `__repr__()` definieren.

### 6.5 Operatormethoden

Ähnlich wie die besonderen Methoden sind die Operatormethoden für die eingebauten Objekttypen bereits vordefiniert. Sie können auch die Operatormethoden für Ihre eigenen Objekttypen, also Klassen, selbst definieren. Nachfolgend werden insgesamt drei dieser Methoden zum Vergleich zweier Objekte und zur Subtraktion zweier Objekte genutzt:

```py
# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez="(leer)", ge=0):     # Konstruktor Methode
        self.bezeichnung = bez
        self.geschwindigkeit = ge
        
    def __gt__(self, other):                    # 1. Vergleichsmethode
        return self.geschwindigkeit > other.geschwindigkeit

    def __eq__(self, other):                    # 2. Vergleichsmethode
        return self.geschwindigkeit == other.geschwindigkeit

    def __sub__(self, other):                   # Rechenmethode
        return self.geschwindigkeit - other.geschwindigkeit

# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 60)
volvo = Fahrzeug("Volvo Amazon", 45)

# Objekte vergleichen
if opel > volvo:
    print("Opel ist schneller")
elif opel == volvo:
    print("Beide sind gleich schnell")
else:
    print("Volvo ist schneller")

# Objekte sutrahieren
differenz = opel - volvo
print("Geschindigkeitsdifferenz:", differenz, "km/h")
```

Die methoden `__gt__()`und `__eq__()` werden beim Objektvergleich durch die Benutztung der Vergleichsoperatoren `>` und `==` aufgerufen.
* Die Methode `__gt__()`liefert `True`, falls da Objekt `self` größer als das Objekt `other` ist. Für diese Klasse wird defineirt: Größer bedeutet hörere Gechwindigkeit.
* Die Methode `__eq__()` liefer True, falls die beiden Objekte gleich groß sind, hier also: gleich schnell.

Die Methode `__sub__()` wird beim Einsatz des Operators `-` (minus) aufgerufen. Sie liefert die Differenz zweier Objekte zurück, hier bezieht sich das sinnvollerweise auf die Differenz der Geschwindigkeiten der beiden Objekte. Der Aufruf der Methode lautet: `differenz = opel - volvo`.

Neben den Vergleichsoperatoren `>` greather then und `==` equal können Sie weitere nutzen:
* `>=` führt zu `__ge__()` - greater or equal
* `<` führt zu `__lt__()` - lower than
* `<=` führt zu `__le__()` - lower or equal
* `!=` führt zu `__ne__()` - not equal

Neben dem Rechenoperator `-` können Sie weitere nutzen, u.a.:
* `+` führt zu `__add__()`
* `*`  führt zu `__mul__()`
* `/` führt zu `__truediv__()`
* `//` führt zu `__floordiv__()` 
* `%` führt zu `__mod__()`
* `**` führt zu `__pow__()`

### 6.6 Referenz, Identität und Kopie

Wie Sie bereits in Abschnit 4.8, Referenz, Dientität und Kopie, erfahren haben, ist derr Name eines Objekts lediglich eine Referenz auf das Objekt. Bei Objekten von benutzerdefinierten Klassen erzeugt die Zuweisung dieser Refernz an einen anderen Namen lediglich eine zweite Referenz auf da selbe Objekt.

**Echte Kopien** von Objekten benutzerdefinierter Klassen können Sie durch Erzeugung eines neuen Objekts erstellen, dem Sie z.B. innerhalb des Konstruktors, die Werte eines anderen Objekts der gleichen Klasse zuweisen.

Für die Kopie von umfangreichen Objekten können Sie sich ebenfalls der Funktion `deepcopy()` aus dem Modul `copy` bedienen, siehe auch Abschnitt 4.8.3, Objekte Kopieren. Im nachfolgenden Programm sehen Sie Beispiele für die genannten Vorgänge. Es werden nacheinander erzeugt:
* Ein objekt
* Ein zweites Objekt als Kopie des ersten objekts mithilfe von Wert-zuweisung
* Ein dritten Objekt als Kopie des ersten Objekts mit `deepcopy()`
* eine zusätzliche Refernz auf das erste Objekt

```py
# Modul copy
import copy

# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    def __str__(self):
        return self.bezeichnung + " " + str(self.geschwindigkeit) + " km/h"

# Objekt der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)

# Kopie eines Objektes erzeugen
zweit_opel = Fahrzeug(opel.bezeichnung, opel.geschwindigkeit)
zweit_opel.beschleunigen(30)

# Tiefe Kopie
dritt_opel = copy.deepcopy(opel)
dritt_opel.beschleunigen(35)

# Zweite Referenz auf objekt erzeugen
viert_opel = opel
viert_opel.beschleunigen(20)

# Kontrollausgaben
print("Original:", opel)
print("1. Kopie:", zweit_opel)
print("2. Kopie:", dritt_opel)
print("2. Refferenz:", viert_opel)
print()

# Identisch
print("2:", opel is zweit_opel)
print("3:", opel is dritt_opel)
print("4:", opel is viert_opel)
```
```
Original: Opel Admiral 60 km/h
1. Kopie: Opel Admiral 70 km/h
2. Kopie: Opel Admiral 75 km/h
2. Refferenz: Opel Admiral 60 km/h

2: False
3: False
4: True
```
Das Objekt `opel` ist das Original. Das Objekt `zweit_opel` ist eine KOpie. Es handelt sich um ein eigenes Objekt, das mithilfe des Konstruktors und der Daten des Originalobjekts erzeugt wird. Das Objekt `dritt_opel` ist ebenfalls eine Kopie. Dieses Objekt wird mithilfe der Funktion `copy.deepcopy()` erzeugt.

Bei `viert_opel` handelt es sich um eine zusätzliche Referenz auf das Originalobjekt `opel`. Die Änderung einer Eigenschaft über diese Referenz ändert Das originalobjekt, wie die Ausgabe zeigt.

Die Vergleiche auf Identität mithilfe des Operators `is` zeien, dass nur die Objekte `opel` und `viert_opel` identisch sind.

### 6.7 Vererbung

Eine Klasse kann ihre Eigenschaften und Methoden an eine andere Klasse vererben. Dieser Mechanismus wird häufig angewendet. Sie erzeugen dadurch eine Hierarchie von Klassen, die die Darstellung von Objekten ermöglicht, die teilweise übereinstimmende, teilweise unterschiedliche Merkmale aufweisen.

Im folgenden Beispiel wird eine Klasse `PKW` definiert, mit deren Hilfe die Eigenschaften und Methoden von PKW's dargestellt werden. Bei der Erzeugung bedient man sich der bereits existierenden Klasse `Fahrzeug`.

Von der Klasse `PKW` aus gesehen ist die Klasse `Fahrzeug` eine Basisklasse. Von der Klasse `Fahrzeug` aus gesehen ist die Klasse `PKW` eine abgeleitete Klasse. Zunächst die Definition der Basisklasse `Fahrzeug`. Sie enthält drei methoden und zwei Eigenschaften:

```py
# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez="(leer)", ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigen(wert):
        self.geschwindigkeit += wert
    def __str__(self):
        return self.bezeichnung + " " + str(self.geschwindigkeit) + " km/h"
```

Es folgt die Definition der abgeleiteten Klasse `PKW`. Sie erbt von der Klasse `Fahrzeug` und enthält fünf Methoden und frei Eigenschaften:
* die eigene Konstruktor Methode `__init__()` und die eigene Ausgabemethode `__str__()`, die jeweils die gleichnamige Methode der basisklasse überschreiben
* die eigenen Methoden `einsteigen()` und `aussteigen()``
* die von der Klasse `Fahrzeug` geerbte Methode `beschleunigen()`
* die eigene Eigenschaft `insassen`
* die von der Klasse Fahrzeug geerbten Eigenschaften `bezeichnung` und `geschwindigkeit`

```py
# Definition der Klasse PKW
class PKW(Fahrzeug):
    def __init__(self, bez, ge, ins=0):
        Fahrzeug.__init__(self, bez, ge)
        self.insassen = ins
    def __str__(self):
        return Fahrzeug.__str__(self) + " " + str(self.insassen) + " Insassen"
    def einsteigen(self, anzahl):
        self.insassen += anzahl
    def aussteigen(self, anzahl):
        self.insassen -= anzahl
```

Wenn eine Klasse von einer anderen Klasse abgeleitet wird, so wird der Name der Basisklasse in Klammern hinter dem Namen der abgeleiteten Klasse angegeben.

Eine Methode einer Basisklasse kann in einer abgeleiteten Klasse über schrieben werden. Zum Aufruf einer Methode der Basisklasse müssen Sie den Namen dieser Klasse angeben.

Es folgt das Hauptprogramm, in dem ein Objekt der Klasse `PKW` erzeugt, verändert und ausgegeben wird:

```py
# Objekt der abgeleiteten Klasse PKW erzeugen
fiat = PKW("Fiat Marea", 50, 0)

# Eigene Methode anwenden
fiat.einsteigen(3)
fiat.aussteigen(1)

# Geerbte Methode anwenden
fiat.beschleunigen(10)

# Überschriebene methode anwenden
print(fiat)
```
```
Fiat Marea 60 km/h 2 Insassen
```

Es wird das Objekt `fiat` erzeugt, dabei wird der Konstruktor aufgerufen. Er wird unmittelbar in der zugehörigen Klasse `PKW` gefunden. Dieser Konstruktor ruft wiederum den Konstruktor der Basisklasse auf, der in der Lage ist, die Erzeugung von Objekten der Basisklasse durchzuführen. Diese abgestufte Vorgehensweise ist nicht zwingend vorgeschrieben, aber empfehlenswert. Anschließend wird die verbleibene Eigenschaft der abgeleiteten Klasse initialisiert.

Es werden die Methodne `einsteigen()` und `aussteigen()` aufgerufen. Diese wird nicht unmittelbar ind er Klasse PKW gefunden, daher wird ind er Basisklasse weitergesucht. Dort wird sie gefunden und dient zur Veränderung der Eigenscahft `geschwindigkeit`.

Es wir die Ausgabemethode `__str__()` aufgerufen. Diese wird unmittelbar in der Klasse PKW gefunden. Sie ruft wiederum die gleichnamige Methode der Basisklasse auf. Das Ergebnis dieses Aufrufs wird mit den restlichen daten aus der Klasse PKW zusammengesetzt und zurückgeliefert. Dies führt zur Ausgabe aller Daten des objekts `fiat`.

Eigenschaften und Methoden werden zunächst in der Klasse des Objekts gesucht. Falls sie dort nicht vorhanden sind, wird die Suche in der zugehörigen Basisklasse fortgesetzt.

### 6.8 Mehrfachvererbung

Eine abgeleitete Klasse kann wiederum Basisklasse für eine weitere Klasse sein. Dadurch ergib sich eine Vererbung über mehrere Ebenen. Eine Klasse kann außerdem von zwei Basisklassen gleichzeitig abgeleitet sein (Mehrfachvererbung), sie erbt in diesem Fall alle Eigenschaften und Methoden beider Basisklassen.

Im folgenden Beispiel werden die beiden Klassen `PKW` und `LKW` von der Klasse `Fahrzeug`abgeleitet. Außerdem wird die Klasse `Lieferwagen` erzeugt, die sowohl von der Klasse `PKW` als auch von der Klasse `LKW` erbt. Die Definitionen der Klassen `Fahrzeug` und `PKW`sind bereits aus Abschnitt 6.7 *Vererbung* bekannt.

Die abgeleitete Klasse `LKW` ähnelt im Aufbau der Klasse `PKW`, erbt von der Klasse `Fahrzeug` und enthält fünf Methoden und drei Eigenschaften:
* die eigenen Konstruktormethode `__init__()` und die eigene Ausgabemethode `__str__()`, die jeweils die gleichnamige Methode der Basisklasse überschreiben
* die eigene Methoden `beladen()` und `entladen()`
* Die von der Klasse `Fahrzeug` geerbte Methode `beschleunigen()`
* die eigene Eigenschaft `ladung()`
* die von der Klasse Fahrzeug geerbten Eigenschaften `bezeichnung` und `geschwindigkeit`

```py
# Definition der Klasse LKW
class LKW(Fahrzeug):
    def __init__(self, bez="(leer)", ge=0, la=0):
        Fahrzeug.__init__(self, bez, ge)
        self.ladung = la
    def __str__(self):
        return Fahrzeug.__str__(self) + " " + str(self.ladung) + " Tonnen Ladung"
    def beladen(self, wert):
        self.ladung += wert
    def entladen(self, wert):
        self.ladung -= wert
```

Die Klasse `Lieferwagen` erbt von zwei Klassen, die eine gemeinsame Basisklasse haben. Sie enthält sieben Methoden und vier Eigenschaften:
* die eigene Konstruktor Methode `__init__()` und die eigene Ausgabemethode `__str__()`, die jeweils die geerbten Methoden überschreiben
* die von der Klasse `Fahrzeug` geerbte Methode `beschleunigen()`
* die von der Klasse `PKW` geerbte Eigenschaft `insassen`
* die von der Klasse `LKW` geerbte Eigenschaft `ladung`
* die von der Klasse `Fahrzeug` geerbte Eigenschaft `bezeichnung` und `geschwindigkeit`

```py
# Definition der Klasse Lieferwagen
class Lieferwagen(PKW, LKW):
    def __init__(self, bez="(leer)", ge=0, la=0, ins=0):
        PKW.__init__(self, bez, ge, ins)
        LKW.__init__(self, bez, ge, la)
    def __str__(self):
        return PKW.__str__(self) + "\n" + LKW.__str__(self)
```

Im Hauptprogramm wir ein Objekt der Klasse `Lieferwagen` erzeugt, verändert und ausgegeben:

```py
# Objekt der abgeleiteten Klasse Leiferwagen erzeugen
toyota = Lieferwagen("Toyota Allround")
toyota.einsteigen(2)
toyota.beladen(3.5)
toyota.beschleunigen(30)
print(toyota)
```
```
Toyota Allround 30 km/h 2 Insassen
Toyota Allround 30 km/h 3.5 Tonnen Ladung
``` 
Es wird das Objekt `toyota` erzeugt, dabei wird der Konstruktor aufgerufen. Dieser wird unmittelbar in der zugehörigen Klasse `Lieferwagen` gefunden. Der Konstruktor ruft wiederum die beiden Konstruktoren der Basisklassen `PKW` und `LKW` auf. Diese rufen jeweils zum einen den Konstruktor der Basisklasse `Fahrzeug`auf und initialisieren zum anderen eine spezifishe Eigenschaft der Klasse (`insassen` oder `ladung`).

Die Methoden `einsteigen()`, `beladen()`und `beschleunigen()`werden aufgerufen. Sie werden in verschiedenen Basisklassen gefunden und verändern die Eigenschaften `insassen`, `ladung` und`geschwindigkeit`.

Die eigene Ausgabemethode `__str__()` wird aufgerufen. Sie ruft die gleichnamigen Methoden der Basisklassen auf.

**Hinweis**
Nur wenige objektorientierte Programmiersprachen bieten das Konzept der Mehrfachvererbung an, da es den Entwurf von Klassenbibliotheken komplex und unübersichtlich machen kann.

### 6.9 Datenklassen

Seit Python 3.7 haben Sie die Möglichkeit, zusammengehörige Werte auf einfache Weise mithilfe von Datenklassen gemeinsam zu speichern. Dabei handelt es sich um vereinfachte Klassen. Einige der besonderen Methoden sind für diese Klassen bereits vordefiniert, wie z.B. die Konstruktormethode `__init__()`, die Ausgabemehtode `__repr__()`und die Vergleichsmethode `__eq__()`. Im nachfolgenden Beispiel wird eine Datenklasse für zwei dimensionale Vektoren definiert und genutzt:

```py
import dataclasses, math, typing

@dataclasses.dataclass
class Vektor:
    x: float = 0.0
    y: typing.Any = 0.0

    def betrag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

va = Vektor(3.0, 4.5)
vb = Vektor(3.0, 4.0)

va.y = 4.0

if va == vb:
    print("Vektoren sind gleich")

print(va)
print("Betrag:", va.betrag())

vc = Vektor(1.8)
print(vc)

vd = Vektor(y=9.1)
print(vd)
```
```
Vektoren sind gleich
Vektor(x=3.0, y=4.0)
Betrag: 5.0
Vektor(x=1.8, y=0.0)
Vektor(x=0.0, y=9.1)
```
Die Klasse Vektor wird mithilfe des Dekorators `@dataclass` aus dem Modul `dataclasses` als Datenklasse gekennzeichnet. Ein OBjekt der Klasse `Vektor` besitzt die beiden Eigenschaften `x` und `y`. Sie stehen für die beiden Komponenten eines zweidimensionalen Vektors.

Die Eigenschaften einer Datenklasse werden mithilfe von *Type Hints* vereinbart, wie b.B. `int`, `float` oder `str`. Die Typhinweise der Eigenschaften werden jeweils nach einem Doppelpunkt notiert.
Beachten Sie zu diesem Thema auch Abschnitt 3.2.6. Der Grundregel folgend, dass python weiterhin eine dynamisch typisierte Sprache bleiben soll, wurde für die Komponente `y` der unspezifische Typhinweis `Any` aus dem Modul `typing`vereinbart.

Bei Datenklassen ist eine Konstruktormethode bereits vordefiniert. Sie führt zu einer Initialisierung der Eigenschaften mithilfe der Parameter. Wie bei Standardklassen (siehe Abschnitt 6.3) können Sie für die Eigenschaften einer Datenklasse Vorgabewerte vereinbaren und mit benannten Parametern arbeiten. IM Beispiel wure der Vorgabewert 0.0 für beide Eigenschaften notiert.

Die Methode `betrag()` berechnet den Betrag eines zweidimensionalen Vektors nach der folgenden mathematischen Regel: Der Betrag entspricht der Quadratwurzel der Summe der Quadrate der Komponenten.

Die beiden Objekte `va` und `vb` der Klasse `Vektor` werden mit Werten für beide Eigenschaften initialisiert. Bei der anschließenden Zuweisung wird auf die Eigenschaften eines Objekts mit der üblichen Punktschreibweise zugegriffen.

Bei Datenklassen ist die Vergleichsmethode ebenfalls bereits vordefiniert. Daher kann derVergleichsoperator `==` angewendet werden und führt standardmäßig zu einem Vergleich der einzelnen Eigenschaften.

Das Objekt `vc` der Klasse `Vektor` wird mit einem Wert für die Eigenscahft `x` initialisiert. Die Eigenschaft `y` behält den Vorgabewert 0.0. Das Objekt `vd` der Klasse `Vektor` wird mithilfe eines benannten Parameters mit einem Wert für die Eigenscahft `y` initialisiert. In diesem Fall behält die Eigenscahft `x` den Vorgabewert 0.0.

Die Ausgabemethode ist bei Datenklasen ebenfalls bereits vordefiniert. Sie führt standardmäßig zu einer Ausgabe des Namens der Klasse, gefolgt von den Namen der Eigenschaften des Objekts mit ihren jeweiligen Werten.

### 6.10 Enumerationen

Enumerationen sind Aufzählungen von Konstanten. Der Programmcode wird duch die Nutzung der Elemente einer Enumeration besser lesbar. Python bietet seit der Version 3.4 innerhalb des Moduls `enum` u.a. die Klasse `IntEnum` zur Erstellung einer ENumeration, deren Elemente als Konstanten für ganze zahlen stehen.

```py
# Definition einer Enumeration mit ganzen Zahlen
import enum

class Farbe(enum.IntEnum):
    rot = 5
    gelb = 2
    blau = 4

# Vergleich
x = 2
if x == Farbe.gelb:
    print("Das ist gelb")
print()

# Alle Elemente:
for f in Farbe:
    print(f, repr(f))
print()

# Verschiedene Ausgaben und Berechnungen
print(Farbe.gelb)
print(Farbe.gelb * 1)
print(Farbe.gelb * 10)
```
Nach Import des Moduls `enum` wird die Klasse `Farbe` erzeugt, die von der Klasse `IntEnum` erbt. Die Elemente einer Enumeration müssen unmittelbar mit Werten versehen werden. Die Werte müssen nicht in aufsteigender Reihenfolge sein. Ein bestimmter Wert könnte durch mehrere Konstanten repräsentiert werden, dies wäre aber nicht sinnvoll.

Der Vergleich eines Werts mit einem bestimmten anderen Wert wird durch die Elemente der Enumeration erleichert. Dies verbessert dieLesbarkeit des Programmcodes.

Die Enumeration ist iterierbar. Mithilfe einer Schleife können Sie alle Elemente in der definierten Reihenfolge auflisten. Die eingebaute Funktion `repr()` liefert weitere Informationen zu diesem Elementen. Sie können den repräsentierten ganzzahligen Wert auch direkt in Berechnungen einbauen.

### 6.11 Spiel, objektorientierte Version

In diesem Abschnitt stelle ich Ihnen eine objektorientierte Version des Kopfrechenspiels vor. In der Anweisung gibt es ein Objekt der Klasse `Spiel`.

Während der Lebensdauer ieses Objekts werden mehrere Objekte der Klasse `Aufgabe` erzeugt und genutzt. Zunächst die Importanweisung und das kurze Hauptprogramm:

```py
import random

# Hauptprogramm

s = Spiel()
s.spielen()
print(s)
```

Das Modul `random` wird für den Zufallsgenerator benötigt. Im Hauptprogramm wird das Objekt `s` der Klasse `Spiel` erzeugt. Damit wird ein Spiel initialisiert. Für dieses Objekt wird die Methode `spielen()` ausgeführt. Das ist der eigentliche Spielvorgang. Zum Abschluss werden die Spielergebnisse ausgegeben.

Es folgt die Definiton der Klasse `Spiel`:

```py
# Definition der Klasse Spiel
class Spiel:
    def __init__(self):

        # Start des Spiels
        random.seed()

        # Rundenanzahl bestimmen
        self.richtig = 0
        self.anzahl = -1

        while self.anzahl < 0 or self.anzahl>10:
            try:
                print("Wie viele Aufgaben? 1-10")
                self.anzahl = int(input("Wie viele Aufgaben? 1-10"))
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
```

Im Konstruktor der Klasse `Spiel` wird der Zufallsgenerator initialisiert. Der Zähler für die richtig gelösten Aufgaben wird zunächst auf `0` gesetzt. Es wird die Anzahl der zu lösenden Aufgaben ermittelt. Dabei werden zwei Eigenscahften der Klasse `Spiel` gesetzt: `richtig` und `anzahl`.

In der Methode `spielen()` wird die gewünschte Anzahl an Aufgaben erzeugt. Jede Aufgabe ist ein Objekt der Klasse `Aufgabe`. Die Aufgabe wird ausgegeben, also dem Benutzer gestellt. Anschließend wird die Methode `beantworten()` aufgerufen, also die Eingabe des benutzers verarbeitet. Rückgabewert de MEthode `beantworten()` ist `1` oder `0`. Entsprechend wird der Zähler von `richtig` verändert.

In der Ausgabemethode der Klasse Spiel wird das Ergebnis des Spiels-Objekts veröffentlicht.

Zu guter letzt folgt die Defintion der Klasse `Aufgabe`:

```py
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
```

Jedes Objekt der Klasse `Aufgabe` erhält bei der Erzeugung seine eigene Nummer. Zudem wird die Gesamtanzahl der Aufgaben übermittelt. Dabei werden zwei Eigenschaften der KLasse `Aufgabe` gesetzt: `nr` und `gesamt`.

In der Ausgabemethode wird die Aufgabe zusammengesetzt und veröffentlicht. Das richtige Ergebnis der Aufgabe ist eine eigensachft der Klasse `Aufgabe`.

In der Methode `beantworten()` wird die Eingabe des Benutzers gespeicert und mit dem richtigen Ergebnis der Aufgabe verglichen. Eine falsche oder ungültige Eingabe erzeugt eine Ausnahmen, dies führt zur Rückgabe einer 0. Eine richtige Eingabe führt zur Rückgabe einer 1.


## 7 Verschiedene Module

In diesem Kapitel erläutere ich Programmiertechniken zur Aurbeit mit Datums' und Zeitangaben, Collections, die Technik des Multithreadings sowie reguläre Ausdrücke.

### 7.1 Datum und Zeit

Das Modul `time` enthält Funktionen zur Verarbeitung und Formattierung von Datums- und Zeitangaben.

dqmitkönnten wir z.B. das Kopfrechenspiel aus dem Programmierkurs um Datums- und Zeitangaben erweitern. Wir könnten eine Zeitmessung einbauen, die feststellt, wie lange ein Benutzer zur Lösung einer oder aller Aufgaben benötzigt hat. Falls die Bestleistung erzielt wird, z. B. eine hohe Anzahl an gelösten Aufgaben im ersten Versuch oder die Lösung der Aufgaben innerhalb besonders kurzer Zeit, könnten wir das mit Datum und Uhrzeit festhalten.

Auf vielen Betriebssystemen gilt der 1. januar 1970 00:00 Uhr als Nullpunkt für die Verarbeitung von Datums und Zeitangaben. Die Zeit wird in Sekunden ab diesem Zeitpunkt gerechnet.

#### 7.1.1 Ausgabe der Zeit mit `localtime()`

Das nachfolgende Beispielprogramm verdeutlicht die Ermittelung und die formatierte Ausgabe der aktuellen Zeit. Es nutzt die Funktione `time()`, `time_ns()` und `localtime()`aus dem Modul `time`:

```py
# Modul time
import time


# Zeit in Sekunden
print("Zeit in Sekunden:", time.time())

# Zeit in Nanosekunden
print("Zeit in Nanosekunden:", time.time_ns())

# Aktuelle, lokale Zeit als Tupel

lt = time.localtime()
print("Lokale Zeit als Tupel:", lt)


# Entpacken des Tupels, Datum und Uhrzeit

jahr, monat, tag = lt[:3]
stunde, minute, sekunde = lt[3:6]
print(f"  Datum: {tag:02d}.{monat:02d}.{jahr:4d}")
print(f"Uhrzeit: {stunde:02d}:{minute:02d}:{sekunde:02d}")

# Wochentag

wtage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
wtagnr = lt[6]
print(wtage[wtagnr])

# Tag des Jahres

tag_des_jahres = lt[7]
print(f"Tag {tag_des_jahres:d} des Jahres")

# sommerzeit
dst = lt[8]
if dst == 1:
    print("Die Sommerzeit sit aktiv")
elif dst == 0:
    print("Die Sommerzeit ist nicht aktiv")
else:
    print("Keine Sommerzeitinformation vorhanden")
```
```
Zeit in Sekunden: 1602451689.223836
Zeit in Nanosekunden: 1602451689223906000
Lokale Zeit als Tupel: time.struct_time(tm_year=2020, tm_mon=10, tm_mday=11, tm_hour=23, tm_min=28, tm_sec=9, tm_wday=6, tm_yday=285, tm_isdst=1)
  Datum: 11.10.2020
Uhrzeit: 23:28:09
Sonntag
Tag 285 des Jahres
Die Sommerzeit sit aktiv
```
Die Funktion `time()` liefert die katuelle Zeit in Sekunden seit dem 1. Januar 1970.

Seit Python 3.7 gibt es einige Funktionen, die Zeitwerte mit einer Genauigkeit in Nanosekunden (1 Nanosekunde = 10^-9 Sekunden) liefern, darunter die Funktion `time_ns()`

Die Funktion `localtime()` ohne Parameter liefert die katuelle Zeit als ein Tupel, das aus einer Reihe von Einzelinformationen besteht. Diese können anschließend ausgewertet werden:
* Die ersten drei Elemente (0 bis 2) liefern Jahr, Monat und Tag. Monat und Tag sind im Beispiel jeweils mit zwei Ziffern und führender Null formatiert.
* Die nächsten drei Elemente (3,4,5) liefern Stunde, Minute und Sekunde. Alle drei Angaben sind im Beispiel jeweils mit zwei Ziffern und führender Null formatiert.
* Das nächste Element (6) stellt den Wochentag von 0 bis 6 bereit. Montag entspricht dabei der 0, Sonntag der 6.
* Die laufende Nummer des Tages innerhalb eines Jahres wird von Element 7 geliefert.
* Informationen über en status der Sommerzeit liefert das letzt Element (8).

#### 7.1.2 Ausgabe der Zeit mit `strftime()`

Die Funktion `strftime()` dient ebenfalls der Formatierung. Sie lieert allerdings genauere Informationen als die Funktion `localtime()`.

Sie benötigt zwei Parameter:
1. einen Formatierungsstring für die gewünschte Ausgabe
2. 2. Ein Zeittupel, wie es z.B. die Funktion `localtime()` liefert

Im Beispiel werden die folgenden Inormationen geliefert:
* Jahresangabe nur mit zwei Ziffern
* Tag des Jahres
* Nummer es Wochentags, nach verschiedenen Systemen
* Nummer der Kalenderwoche, nach verschiedenen Systemen
* Angabe der Zeitzone
  
Die Nummer des Wochentags und der Kalenderwoche kann seit Python 3.6 auch gemäßg ISO 8601 angegeben werden. Dabei handelt es sich um einen aktuellen internationalen Standard für Datums- und Zeitwerte.

Ein Beispielprogramm:

```py
import time
lt = time.localtime()

print(time.strftime("Tag.Monat.Jahr: %d.%m.%Y", lt))
print(time.strftime("Stunde:Minute:Sekunde: %H:%M:%S", lt))
print(time.strftime("Tag des jahres: %j", lt))
print()

print("Wochentag:")
print(time.strftime("Nr. (Sonntag = 0): %w", lt))
print(time.strftime("Nach ISO 8601: %u", lt))
print()

print("Kalenderwoche:")
print(time.strftime("Beginn Sonntag: %U", lt))
print(time.strftime("Beginn Montag: %W", lt))
print(time.strftime("Nach ISO 8601: %V", lt))

print(time.strftime("Zeitzone: %Z", lt))
```
```
Tag.Monat.Jahr: 12.10.2020
Stunde:Minute:Sekunde: 00:11:55
Tag des jahres: 286

Wochentag:
Nr. (Sonntag = 0): 1
Nach ISO 8601: 1

Kalenderwoche:
Beginn Sonntag: 41
Beginn Montag: 41
Nach ISO 8601: 42
Zeitzone: CEST
```

**Unterschiede in Ubuntu Linux und macOS**
Für die Zeitzone wird CEST Central European Summer Time ausgegeben.
Bei Windows: Mitteleuropäische Sommerzeit


#### 7.1.3 Zeitangabe erzeugen

Zur Erzeugung einer beliebigen Zeitangabe wird die Funktion `mktime()` genutzt. Sie benötigt als Parameter ein Tupel mit allen neun Angaben, wie sie auch von der Funktion `localtime()` geliefert werden.

Die Angaben für Wochentag, Tag des Jahres und SOmmerzeit kennen Sie natürlich nur in den wenigsten Fällen. Falls hier einfach jeweils eine `0` gesetzt wird, werden die richtigen Werte automatisch ermittelt, wie das folgende Beispiel zeigt:

```py
# Modul time
import time

# Zeitangaben erzeugen

dztupel = 2019, 12, 15, 13, 29,59,0,0,0

print(time.strftime("%d.%m.%y %H:%M:%S", dztupel))
damals = time.mktime(dztupel)

# Ausgabe
lt = time.localtime(damals)

# Wochentag
wtage = ["Montag", "Dienstag", "Mittwoch", "Donenrstag", "Freitag", "Samstag", "Sonntag"]
wtagnr = lt[6]
print("Das ist ein", wtage[wtagnr])


# Tag des Jahres
tag_des_jahres = lt[7]
print(f"Der {tag_des_jahres:d}. Tag des Jahres")
```

```
15.12.19 13:29:59
Das ist ein Sonntag
Der 349. Tag des Jahres
```
Die Zeitangabe 15. Dezember 2019 wird gespeichert. Dazu werden die ersten sechs Elemente des Tupels mit den gegebenen Werten besetzt. Die drei restlichen Angaben weren jeweils mi `0` besetzt.

Wird die Funktion `localtime()` mit einer Zeitangabe als Parameter aufgerufen, liefert sie ein Tupel mit den einzelnen Informationen zu dieser Zeitangabe.

#### 7.1.4 Mit Zeitangaben rechnen

Zur Berechnung eines Zeitraums, also der Differenz zwischen zwei Zeitangaben, müssen beide Zeitangaben einzeln erzeugt werden. Anschließend können Sie die Differenz aus den beiden Zeitangaben in Sekunden berechnen. Aus dieser Differenz lässt sich auch die Differenz in Minuten, Stunden und Tagen ermitteln.

Im nun folgenden Programm wird die Differenz zwischen dem 15. Dezember 2019 23:55:00 und dem 16. Dezember 2019 00:05:15 Uhr berechnet.

```py
# Modul time
import time
# Zwei Zeitangaben erstellen
dztupel1 = 2019, 12, 15, 23, 55, 00 ,0,0,0
damals1 = time.mktime(dztupel1)
print("Zeit 1:", time.strftime("%d,%m,%Y %H:%M:%S", dztupel1))

dztupel2 = 2019, 12, 16, 00, 5, 15 ,0,0,0
damals2 = time.mktime(dztupel2)
print("Zeit 2:", time.strftime("%d,%m,%Y %H:%M:%S", dztupel2))

# Diferenz berechnen
print("Differenz:")

diff_sek = damals2 - damals1
print(diff_sek, "Sekunden")
diff_min =diff_sek/60
print(diff_min, "Minuten")
diff_std = diff_min/60
print(diff_std, "Stunden")
diff_tag=diff_std/24
print(diff_tag, "Tage")
```
```
Zeit 1: 15,12,2019 23:55:00
Zeit 2: 16,12,2019 00:05:15
Differenz:
615.0 Sekunden
10.25 Minuten
0.17083333333333334 Stunden
0.007118055555555555 Tage
```

In den Variablen `diff_sek` wird die Differenz zwischen den beiden Zeitangaben `damals1` und `damals2` in Sekunden berechnet. Zur Ermittlung der Minuten wird der Wert für die Sekunden durch 60 geteilt. Zur Ermittlung der Stunden wird der Wert für die Sekunden durch 60 geteilt. Zur Ermittlung der Stunden wird der Wert für die Minuten wiederum durch 60 geteilt. Zur ermittlung der Tage wird zuletzt der Wert für die Stunden durch 24 geteilt.

**Alter Berechnen**
Zur Berechnung des Alters einer Person wird eine anderer weg beschritten.
Dies wird im folgenden Programm gezeigt.

```py
# Modul time
import time

# Geburtstag
dztupel = 1979, 5, 7, 0, 0, 0, 0, 0, 0
print("Geburt:", time.strftime("%d.%m.%Y", dztupel))
geburt = time.mktime(dztupel)
ltgeburt = time.localtime(geburt)

# Aktuell
ltheute = time.localtime()
print("Heute:", time.strftime("%d.%m.%Y"))

# Alter berechnen
alter = ltheute[0] - ltgeburt[0]
if ltheute[1] < ltgeburt[1] or ltheute[1] == ltgeburt[2] and ltheute[2] < ltgeburt[2]:
    alter -= 1
print("Alter:", alter)
```
```
Geburt: 07.05.1979
Heute: 12.10.2020
Alter: 41
```
Die Zeitangabe für den Geburtstag, z. B. für den 7. Mai 1979, wird mithilfe der Funktion mktime() erzeugt. Die aktuelle Zeitangabe wird mit der Funktion `localtime()` ohne Parameter erzeugt.

Das Alter wird zunächst aus der Differenz der Jahresangaben errechnet. Falls die Person in diesem Jahr noch nicht Geburtstag hatte, weil der Geburtsmonat noch nicht erreicht ist *oder*  innerhalb des Geburtsmonats der Geburtstag noch nicht erreicht ist, wird das Alter um 1 reduziert.

#### 7.1.5 Programm anhalten
Die Funktion `sleep()` aus dem Modul `time` ermöglicht das Anhalten eines Programms für einen bestimmten Zeitraum.

Im folgenden Beispielprogramm wird innerhalb einer Schleife mehrmals die aktuelle Zeit ausgegeben. Nach jeder Ausgabe wird das Programm für zwei Sekundenmithilfe der Funktion `sleep()` angehalten. Am Ende wird die Zeitdiffferenz zwischen Start und Ende berechnet.

```py
# Modul time
import time

# Start
startzeit = time.time()
print("Start:", startzeit)

# Zeitangaben, jeweils mit Pause
for i in range(5):
    time.sleep(2)
    print(time.time())

# Ende
endzeit = time.time()
print("Ende:", endzeit)

# Abstand
differenz = endzeit - startzeit
print("Differenz:", differenz)
```

```
Start: 1602503299.944386
1602503301.9462929
1602503303.9493608
1602503305.9507918
1602503307.951159
1602503309.951241
Ende: 1602503309.9512918
Differenz: 10.006905794143677
```

Wie die Ausgabe der Differenz zeigt, lässt sich die Funktion `sleep()` nur für eine zeitliche Steuerung von begrenzter Genauigkeit einsetzen, und zwar aus den folgenden Gründen:
* zum einen benötigen die einzelnen Programmschritte eine eigene, wenn auch kurze Laufzeit, abhängig von der Geschwindigkeit und der Auslastung des Rechners
* zum anderen unterscheiden sich die Zeitabstände geringfügig

Dennoch können Sie die Funktion `sleep()` für viele Anwendungen sinnvoll einsetzen, u.a. im Bereich von grafischen Animationen, Simulationen oder der Spieleprogrammierung.

#### 7.1.6 Spiel, version mit Zeitmessung

In dieser Version des Kopfrechenspiels werden fünf Additionsaufgaben mit Zahlen aus dem bereich von 10 bis 30 gestellt. Der Spieler hat pro aufgabe nur einen Versuch. Ungültige Eingaben oder falsche Ergebnisse werden einfach mit dem Text `Falsch` kommentiert und bewertet. Am ende wird die Gesamtzeit angegeben, die der Spieler benötigt hat.

```py
# Module
import random, time

# Initialisierung

random.seed()
richtig = 0
startzeit = time.time()


# 5 Aufgaben

for aufgabe in range(5):
    # aufgabe mit Ergebnis
    a = random.randint(10,30)
    b = random.randint(10,30)
    c = a + b
    print("Aufgabe", aufgabe+1, "von 5:", a, "+", b, "= ?")

    #Eingabe
    try:
        zahl = int(input("Bitte eine Zahl eingeben: "))
        if zahl == c:
            print("Richtig!")
            richtig += 1
        else:
            raise
    except:
        print("Falsch")

# Auswertung
endzeit = time.time()
differenz = endzeit - startzeit
print(f"Richtig: {richtig:d} von 5 in {differenz:.2f} Sekunden")
print("Ergebnis erzielt:", time.strftime("%d.%m.%Y %H:%M:%S"))
```
```
Aufgabe 1 von 5: 30 + 17 = ?
Bitte eine Zahl eingeben: 47
Richtig!
Aufgabe 2 von 5: 12 + 16 = ?
Bitte eine Zahl eingeben: 28
Richtig!
Aufgabe 3 von 5: 11 + 22 = ?
Bitte eine Zahl eingeben: 33
Richtig!
Aufgabe 4 von 5: 25 + 13 = ?
Bitte eine Zahl eingeben: 38
Richtig!
Aufgabe 5 von 5: 28 + 21 = ?
Bitte eine Zahl eingeben: 49
Richtig!
Richtig: 5 von 5 in 27.35 Sekunden
Ergebnis erzielt: 12.10.2020 17:31:27
```

Am Anfang und am Ende wird die Zeit genommen und anschließend die Differenz berechnet. Die richtigen Ergebnisse werden mitgezählt. Im Fall einer ungültigen Eingabe oder eines falschen Ergebnisses wird eine Ausnahme erzeugt.

#### 7.1.7 Spiel, objektorientierte Version mit Zeitmessung

Die objektorientierteVersion des Kopfrechenspiels mit Zeitmessung basiert auf der objektorientierten Version ohne Zeitmessung, siehe Datei spiel_oop.py in Abschnitt 6.11. Hier stelle ich nur die Erweiterung vor. Zunächst die Importanweisung und das kurze Hauptprogramm:

```py
import random, time ## Add import time module

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

    def __str__(self): ## modified Method
        # Ergebnis
        datum = time.strftime("%d.%m.%Y")
        uhrzeit = time.strftime("%H:%M:%S")
        ausgabe = f"Richtig: {self.richtig:d} von {self.anzahl:d} Aufgaben in {self.zeit:.2f} Sekunden \nam {datum} um {uhrzeit}"
        return ausgabe


    def messen(self, start): ## Adding Method
        # Zeitmessen
        if start:
            self.startzeit = time.time()
        else:
            endzeit = time.time()
            self.zeit = endzeit - self.startzeit


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
s.messen(True)      # added
s.spielen()
s.messen(False)     # added
print(s)
```

In der Methode `messen()` wird die Startzeit ermittelt, falls der Parameterwert `True` übermittelt wird. Andernfalls wird die Endzeit und die Spieldauer ermittelt. Die Spieldauer (`zeit`) ist eine Eigenscahft der Klasse  `Spiel`. in der Ausgabemethode wird das Ergebnis des Spies zusammen mit Spieldauer, Datum und Uhrzeit veröffentlicht.

### 7.2 Warteschlangen

Eine Warteschlange (queue) im allgemeinen Sinne entsteht immer dann, wenn ein System innerhalb eines Zeitraums mehr Anforderungen erhält, als es verarbeiten kann. Dabei kann es sich um eine Warteschlange von Personen an einer Kinokasse oder um eine Warteschlange von gesendeten Daten in einem Netzwerk handeln.

Ziel ist es, eine Warteschlange möglichst schnell zu leeren. Abhängig von der Problemstellung kann dies auf unterschiedliche Weise geschehen:

* In einer *FIFO-Queue* wird diejenige Anforerung, die als Erste eingetroffen ist, auch als Erste behandelt. FIFO steht als Abkürzung für *First In First Out* Anforderungen können nur am Ende der Warteschlange eintreffen und nur am Anfang der Warteschlange behandelt werden.
* In einer *LIFO-Queue* wird diejenige Anforderung, die als Letzte eingetroffen ist, als Erste bheandelt. LIFO steht für *Last In First Out*. Anforderungen können nur am Ende der Warteschlange eintreffen und auch nur dort behandelt werden.
* Eine *Double-Ended Queue* besitzt keinen Anfang, aber dafür zwei Enden. Anforderungen können an beiden Enden der Warteschlagne eintreffen und auch an beiden Enden behandelt werden.

Die Module `queue` und `collections` bieten einige spezialisierte Datentypen zur Bearbeitung von Warteschlangen Sie ähneln den eingebauten Datentype (wie Dictionary, Liste, Set oder Tupel), haben aber zusätzliche Fähigkeiten und bieten einen sehr schnellen Zugriff.

#### 7.2.1 Klasse SimpleQueue

Seit Python 3.7 gibt es im Modul `queue` die Klasse `SimpleQueue` zur Bearbeitung einer FIFO-Queue.

```py
import queue

x = queue.SimpleQueue()
print("Anzahl Elemente:", x.qsize())

x.put(5)
x.put(19)
x.put(-2)
x.put(12)
print("Anzahl Elemente:", x.qsize())

while not x.empty():
    print(x.get())
print("Anzahl Elemente:", x.qsize())
```
Es wird das Objekt `x` der Klasse `SimpleQueue()` erzeugt. Die Methode `qsize()` liefert die Anzahl der Elemente. Die Methode `put()` fügt einzelne Elemente am Ende der Warteschleife hinzu. Die Methode `empty()` liefert die Information, ob die Warteschlange leer ist. Die Methode `get()` entfernt ein Element vom Anfang er Warteschleife und liefert gleichzeitig seinen Wert.

```
Anzahl Elemente: 0
Anzahl Elemente: 4
5
19
-2
12
Anzahl Elemente: 0
```

Der Wert 5 wurde der Warteschlange als erstes hinzugeführt. Er wird auch als erster Wert wieder entnommen (FIFO).

#### 7.2.2 Klasse LifoQueue
Zur Bearbeitung einer LIFO-Queue bietet das Modul `queue` die Klasse `Lifo-Queue`.

```py
import queue
x = queue.LifoQueue()
for y in 5, 19, -2, 12:
    x.put(y)
while not x.empty():
    print(x.get())
```
Der Name de Klasse ist geändert. Zudem entfallen hier die Aufrufe der Methode `qsize()`. Die Methode `get()` entfoert diesmal jeweils ein element vom Ende der Warteschlange. Daher erfolgt die Ausgabe der Elemente in umgekehrter Reihenfolge
```
12
-2
19
5
```

#### 7.2.3 Klasse PriorityQueue

Die Klasse `PriorityQueue` aus dem Modul `queue` bietet eine Besonderheit: Die Elemente werden in einer sortierten Reihenfolge geliefert. Nachfolgend ein Beispiel:

```py
import queue
x = queue.PriorityQueue()
for y in 5, 19, -2, 12:
    x.put(y)
while not x.empty():
    print(x.get())
```
Der Name der Klasse ist wiederum geändert. Die Methode `get()` entfernt die Elemente aus der Warteschlange gemäß einer aufsteigenden Sortiertung. Die Ausgabe sieht daher wie folgt aus:
```
-2
5
12
19
```

#### 7.2.4 Klasse deque
Zur Bearbeitung einer Double-Ended Queue gibt es im Modul `collections` die Klasse `deque` (gesprochen: deck). Sie bietet weitaus mehr Möglichkeiten als die zuvor behandelten Queue-Klassen.

Es folgt ein erstes Beispiel, in dem einige Operationen an eine Double-Ended Queue vorgenommen werden:

```py
# Modul
import collections

# Neu erzeugen
d = collections.deque([8, 18, 28])
print("Neu erzeugt:", d)

# Kopie
dk = d.copy()
print("Kopie:", dk)

# Alle Elemente einzeln 
print("Alle elemente einzeln: ", end="")
for x in d:
    print(x, end=" ")
print()



# Einzelne Elemente
try:
    print("Zweites Element von links:",d[1])
except:
    print("Dieser Index existiert nicht")

try:
    print("Erstes Element von rechts:", D[-1])
except:
    print("Dieser Index existiert nicht")

# Multiplizieren

d = d * 2
print("Mit 2 multipliziert:", d)

# Addieren
dzwei = collections.deque([9,19,29])
d = d + dzwei
print("Zweide deque addiert:", d)

# Deque leeren
d.clear()
print("Nach Leerung:", d)
```
```
Neu erzeugt: deque([8, 18, 28])
Kopie: deque([8, 18, 28])
Alle elemente einzeln: 8 18 28 
Zweites Element von links: 18
Erstes Element von rechts: 28
Mit 2 multipliziert: deque([8, 18, 28, 8, 18, 28])
Zweide deque addiert: deque([8, 18, 28, 8, 18, 28, 9, 19, 29])
Nach Leerung: deque([])
```
Die Funktion `deque()` liefert ein neues Objekt desDatentyps `deque`. Als Parameter wird ein iterierbares Objekt benötigt, also z.B. eine Zeichenkette oder eine Liste. Eine Kopie können Sie (seit 3.5) mit der Methode `copy()` erstellen.

Auf die einzlenen Elemente können Sie mithilfe einer `for`-Schleife zugreifen. Auch der Zugriff über einen Index ist möglich. Die Elemente sind von links aus mit 0, 1, 2, ... nummeriert, von rechts aus mit -1, -2, -3, ... Falls Sie einen ungültigen Indes angeben, wird eine Ausnahme erzeugt.

Seit Python 3.5 können Sie mithilfe des OPerators `*` eine `Double-Ended Queue` vervielfachen und mithilfe des Operators `+` andere `Double Ended Queues` addieren. Die Methode `clear()` löscht alle ELemente.

Es folgt ein weiteres Beispiel, in dem eine Double-Ended Queue auf verschiedene Arten verädert wird:

```py
import collections

d = collections.deque([8,18,28])
print("Neu erzeugt:", d)

# Einzelne Elemente angefügt
d.appendleft(5)
d.append(25)
print("Einzelne Elemente angefügt:", d)

# Einzelnes Element eingefügt
d.insert(2,11)
print("Einzelnes Element eingefügt:", d)

# Um mehrere Elemente erweitert
d.extendleft([7,9])
d.extend([17,19])
print("Um mehrere Elemente erweitert:", d) 

# Element suchen
try:
    print("Position des Werts 5", d.index(5))
except:
    print("Wert 5 ist nicht vorhanden")

# Einzelne Elemente entfernen
for i in range(5):
    li = d.popleft()
    print("Entferntes Element, links:", li)
re = d.pop()
print("Entferntes Element, rechts:", re)
print("Nach Entfernung:", d)

# Deque intern rotieren lassen
d.rotate()
print("Nach Rotation um +1:", d)
d.rotate(-1)
print("Nach Rotation um -1:", d)
```

```
Neu erzeugt: deque([8, 18, 28])
Einzelne Elemente angefügt: deque([5, 8, 18, 28, 25])
Einzelnes Element eingefügt: deque([5, 8, 11, 18, 28, 25])
Um mehrere Elemente erweitert: deque([9, 7, 5, 8, 11, 18, 28, 25, 17, 19])
Position des Werts 5 2
Entferntes Element, links: 9
Entferntes Element, links: 7
Entferntes Element, links: 5
Entferntes Element, links: 8
Entferntes Element, links: 11
Entferntes Element, rechts: 19
Nach Entfernung: deque([18, 28, 25, 17])
Nach Rotation um +1: deque([17, 18, 28, 25])
Nach Rotation um -1: deque([18, 28, 25, 17])
```

Mithilfe der methoden `appendleft()` und `append()` fügen Sie einzelne Elemente am linken oder rechten Ende hinzu.

Die Methode `insert()` kann seit Python 3.5 zum Einfügen eines Elements an der genannten Position genutzt werden. Falls es die Position nicht gibt, wird das Element am rechten Ende angefügt.

Die Methoden `extendleft()` und `extend()` dienen zum Erweitern um mehrere Elemente am linken bzw. rechten Ende. Die Elemente werden nacheinander in der gegebenen Reihenfolge angefügt. Daher ändert sich die Reihenfolge für die angefügten Elemente bei der Methode `extendleft()`.

Die Methoden `popleft()` und `pop()` entfernen ein Element am linken Ende oder am rechten Ende. Das entfernte Element wird jeweils als Rückgabewert  geliefert.

Mithilfe der Methode `rotate()` lassen Sie die Elemente zirkular rotieren. Geben Sie keinen Parameter an, wird um ein Element nach rechts rotiert. Geben Sie negative Werte an, wird nach links rotiert. Ein Element, das bei der Rotation über den Rand geschoben wird, wird am anderen Ende wieder angefügt.

### 7.3 Multithreading

Der Begriff *Multithreading* bezeichnet die Eigenschaft eines Programms, mehrere Teile, die sogenannte *Threads*, parallel bearbeiten zu lassen. Die Programmiersprache Python bietet die entsprechenden Routinen.

#### 7.3.1 Wozu dient Multithreading?

Es gibt eine Reihe von Problemstellungen, bei denen sich Multithreading als nützlich erweist, z.B. bei Simulationen von realen Prozessen, bei denen eine Aktion eine weitere Aktion anstößt, danach aber selbst auch weiterläuft. Die angestoßene Aktion kann wiederum eine dritte Aktion anstoßen usw. Alle Aktionen greifen auf dieselben Daten zu u nd verändern sie gegebenenfalls. Sie enden zu verschiedenen Zeitpunkten und mit unterschiedlichen Ergebnissen.

Es kann sich auch um GUI-Anwendungen handeln, bei denen rechenintensive Programmteile im Hintergrund laufen (*ausgelagert werden*) oder parallel die Ergebnisse von Messwertauswertungen oder anderen Echtzeitprozessen dargestellt werden.

#### 7.3.2 Erzeugung eines Threads

Das Modul *threading* bietet eine einfache Möglichkeit zum Multithreading.

Im nachfolgenden Programm wird ein neuer paralleler Thread aus dem Hauptprogramm gestartet. Anschließend muss es 10 Sekunden warten und wird danach beendet. Beginn und Ende werden angezeigt. Im parallelen Thread läuft während der Wartezeit die Funktion `show()`, in der insgesamt fünfmal die aktuelle Zeit angezeigt wird. Nach jeder Anzeige wird der Thread for 1,5 Sekunden angehalten. Beginn und Ende des Threads werden ebenfalls angezeigt.

```py
# Module
import time, threading
# Thread-Funktion
def show():
    print("Start Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("Ende Thread")

# Hauptprogramm

print("Start Hauptprogramm")
t = threading.Thread(target=show)
t.start()
time.sleep(10)
print("Ende Hauptprogramm")
```
```
Start Hauptprogramm
Start Thread
0 1602627353.4196773
1 1602627354.9304807
2 1602627356.4334946
3 1602627357.9469378
4 1602627359.449835
Ende Thread
Ende Hauptprogramm
```

Zur Erzeugung eines parallelen Threads wird ein Objekt der Klasse `Thread` erstellt. der Konstruktor erwartet mindestens den benannten Parameter `target`, der den Namen einer Callback-Funktion übermittelt, die zu Beginn des Threads durchlaufen wird. Ein Thread wird durch den Aufruf der Methode `start()` für das Thread-Objekt gestartet. Bei den hier genutzten Zeiteinstellungen endet das Hauptprogramm erst, nachdem der parallel laufende Thread bereits beendet ist.

#### 7.3.3 Identifizierung eines Threads

Zur Unterscheidung der Auswirkung unterschiedlicher Threads hat jeder Thread eine eindeutige Identifikationsnummer (ID), die Sie mithilfe der Methode `get_ident()` ermitteln können. Das Hauptprogramm sit ebenfalls ein Thread - auch dieser *Haupt-Thread* verfügt über eine ID.

Das vorherige Programm wird erweitert. Aus dem Haupt-Thread werden, zeitlich versetzt, insgesamt zwei Threads mit der Funktion `show()` gestartet. Für jeden Thread, auch für den Haupt-Thread, wird die ID ermittelt und bei jeder Ausgabe zusätzlich angezeigt.

```py
# Module

import time, threading

# Thread-Funktion

def show():
    id = threading.get_ident()
    print("Start Thread", id)
    for i in range(5):
        print(i, "Thread", id)
        time.sleep(1.5)
    print("Ende Thread", id)
    return

# Hauptprogramm 
id = threading.get_ident()
print("Start Hauptprogramm", id)

t1 = threading.Thread(target=show)
t1.start()
time.sleep(0.5)

t2 = threading.Thread(target=show)
t2.start()

time.sleep(10)
print("Ende Hauptprogramm", id)
```
```
Start Hauptprogramm 13932
Start Thread 2836
0 Thread 2836
Start Thread 13304
0 Thread 13304
1 Thread 2836
1 Thread 13304
2 Thread 2836
2 Thread 13304
3 Thread 2836
3 Thread 13304
4 Thread 2836
4 Thread 13304
Ende Thread 2836
Ende Thread 13304
Ende Hauptprogramm 13932
```

Der Haupt-Thread hat hier die ID 13932, der erste Unter-Thread die ID 2836, und der zweite Unter-Thread die ID 13304. Den parallelen Ablauf der Threads können sie anhand der IDs beobachten.

#### 7.3.4 Gemeinsame Daten und Objekte

Alle Threads haben Zugriff auf alle globalen Daten und Objekte des übergeordneten Threads. Im folgenden Beispiel wird gezeigt, wie eine Variable vom Haupt-Thread und zwei weiteren Threads gemeinsam genutzt und verändert wird.

```py
# Module
import time, threading

# Thread-Funktion
def show():
    global counter
    id = threading.get_ident()
    for i in range(5):
        counter += 1
        print(i, id, counter)
        time.sleep(1.5)
    return

# Hauptprogramm
id = threading.get_ident()
counter = 0
print(id, counter)

t1 = threading.Thread(target=show)
t1.start()
time.sleep(0.5)

t2 = threading.Thread(target=show)
t2.start()

time.sleep(10)

counter += 1
print(id, counter)
```
```
2592 0
0 4036 1
0 6596 2
1 4036 3
1 6596 4
2 4036 5
2 6596 6
3 4036 7
3 6596 8
4 4036 9
4 6596 10
2592 11
```

Die Variable `counter` ist global im Haupt-Thread und wird dort mit `0` vorbesetzt. Sie wird mithilfe des Schlüsselworts `global` (siehe 5.7.6) in der Thread-Funktion bekannt gemacht, um 1 erhöht und angezeigt. In beiden Unter-Threads ist die Variable bekannt und kann verändert werden. Am Ende wird sie auch im Haupt-Thread um 1 erhöht und angezeigt.

#### 7.3.5 Threads und Exceptions

Tritt eine unbehandelte Ausnahme auf, betrifft das nur den Thread, in dem sie auftritt. Weder der aufrufende Thaupt-Thread noch die anderen Threads werden dadurch gestört.

Das vorherige PRogramm wird erweitert. Falls die Variable `counter` den Wert 5 hat, wird die unbehandelte Ausnahme `ZeroDivisionError` künstlich hervorgerufen. Der Thread, in dem das geschieht, wird unmittelbar beendet. Die anderen Threads - auch der Haupt-Thread - laufen unbeeinflusst zu Ende. Es folgt das geänderte Programm:
```py
# Module
import time, threading

# Thread-Funktion
def show():
    global counter
    id = threading.get_ident()
    for i in range(5):
        counter += 1
        print(i, id, counter)
        
        # Div/0 Error
        if counter == 5:
            erg = counter/0
    
        time.sleep(1.5)

    return

# Hauptprogramm
id = threading.get_ident()
counter = 0
print(id, counter)

t1 = threading.Thread(target=show)
t1.start()
time.sleep(0.5)

t2 = threading.Thread(target=show)
t2.start()

time.sleep(10)

counter += 1
print(id, counter)
```
```
15600 0
0 300 1
0 17400 2
1 300 3
1 17400 4
2 300 5
Exception in thread Thread-1:
Traceback (most recent call last):
  File "C:\Python39\lib\threading.py", line 950, in _bootstrap_inner
    self.run()
  File "C:\Python39\lib\threading.py", line 888, in run
    self._target(*self._args, **self._kwargs)
  File "c:\Users\Dennis Zorn\Documents\GitHub\Learn_Python\Einstieg in Python\Beispiele\thread_ausnahme.py", line 14, in show
    erg = counter/0
ZeroDivisionError: division by zero
2 17400 6
3 17400 7
4 17400 8
15600 9
```
Der Thread mit der ID 300 endet aufgrund der unbehandelten Ausnahme. Der Thread mit der ID 17400 läuft regulär zu Ende, ebenso der Haupt-Thread mit der ID 156000.

### 7.4 Reguläre Ausdrücke

Reguläre Ausdrücke erleichtern das Suchen und Ersetzen von bestimmten Texten oder Teiltexten oder von einzelnen Zeichen. Sie kommen z.B. bei der Kontrolle und Auswertung von Benutzereingaben oder bei der Suche nach Dateien zum Einsatz.

Wenn festgestellt wird, dass ein Benutzer eine falsche oder unvollständige Eingabe gemacht hat, kann dies zu einer HIlfestellung und einer erneuten Eingabeaufforderung führen. In Python wird das Modul `re` zum Arbeiten mit regulären Ausdrücken benötigt. Zei Programmbeispiele zeigen einen Teil der umfangreichen Möglichkeiten.

#### 7.4.1 Suchen von Teiltexten

Zum Suchen von Teiltexten wird im folgenden Programm die Methode `findall()` eingesetzt. Sie finden alle Teiltexte, die zum regulären Ausdruck passen, und liefert eine Liste dieser Teiltexte zur weiteren Auswertung zurück. Zur besseren übersicht ist das Programm unterteilt. Außerdem sind die einzelnen Blöcke des Programms und die zugehörigen Ausgaben nummeriert.

```py
# Modul
import re


tx = "Haus und Maus und Laus"
print(tx)

# 1: Exater Text
erg = re.findall("Maus", tx)
print("1:", erg)

# 2: Wahl zwischen bestimmten Zeichen
erg = re.findall("[HM]aus", tx)
print("2:", erg)

# 3: Alle Buchstaben aus Bereich
erg = re.findall("[L-M]aus", tx)
print("3:", erg)

# 4: Alle Buchstaben nicht aus Bereich
erg = re.findall("[^L-M]aus", tx)
print("4:", erg)

# 5: Beliebiges Zeichen
erg = re.findall(".aus", tx)
print("5:", erg)

# 6: Suchbegriff nur am Anfang des Texts
erg = re.findall("^.aus", tx)
print("6:", erg)

# 7: Suchbegriff nur am Ende des Texts
erg = re.findall(".aus$", tx)
print("7:", erg)
```
```
Haus und Maus und Laus
1: ['Maus']        
2: ['Haus', 'Maus']
3: ['Maus', 'Laus']
4: ['Haus']
5: ['Haus', 'Maus', 'Laus']
6: ['Haus']
7: ['Laus']
```

Die ersten sieben regulären Ausdrücke beziehen sich auf den Text `Haus und Maus und Laus`.
1. `"Maus"`      - Im ersten Beispiel wird genau die Zeichenfolge `Maus` gesucht. Alle Vorkommen dieser Zeichenfolge werden geliefert.
2. `"[HM]aus"`   - Es werden die Teiltexte gesucht, die mit einem `H` oder einem `M` beginnen und mit `aus` enden.
3. `"[L-M]aus"`  - Es werden die Teiltexte gesucht, die mit einem der Zeichen von `L` bis `M` beginnen und mit `aus` enden. Die eckigen Klammern geben einen Bereich an. Gefunden werden `Maus` und `Laus`, aber nicht `Haus`.
4. `"[^L-M]aus"` - Es werden die Teiltexte gesucht, die * nicht*  mit einem der Zeichen von `L` bis `M` beginnen, aber mit `aus` enden. Das Zeichen `^` bedeutet im Zusammenhang mit einem Bereich eine logische Verneinung. Gefunden wird `Haus` aber nicht `Maus` und `Laus`.
5.  `".aus"`     - Es werden die Teiltexte gesucht, die mit einem beliebigen Zeichen beginnen und mit `aus` enden. Das Zeichen `.` Punkt beduetet: Beliebiges Zeichen, Gefunden werden `Haus`, `Maus` und `Laus`.
6.  `"^.aus"`    - Es werden die Teiltexte gesucht, die mt einem beliebigen Zeichen beginnen und mit `aus` enden. Dies gilt allerdings nur für Teiltexte, die *zu Beginn* des untersuchten Textes stehen. Das Zeichen `^` bedeutet in diesem Zusammenhang: Zu beginn. Gefunden wird nur `Haus`.
7.  `".aus$"`    - Es werden die Teiltexte gesucht, die mit einem beliebigen Zeichen beginnen und mit `aus` enden. Dies gilt allerdings nur für Teiltexte, die *am Ende* des untersuchten TExtes stehen. Das Zeichen `$` beduetet in diesem Zusammenhang: Am Ende. Gefunden wird nur `Laus`.

Es folgt Teil 2 des Programms:

```py
tx = "0172-445633"
print(tx)

# 8: Alle Ziffern aus Bereich
erg = re.findall("[0-2]", tx)
print("8:", erg)

# 9: Alle Zeichen nicht aus Ziffernbereich
erg = re.findall("[^0-2]", tx)
print("9:", erg)

# 10: Alle Zeichen oder Ziffern, die angegeben sind
erg = re.findall("[047-]", tx)
print("10:", erg)
```
```
0172-445633
8: ['0', '1', '2']
9: ['7', '-', '4', '4', '5', '6', '3', '3']
10: ['0', '7', '-', '4', '4']
```
Die nächsten drei Ausdrücke beziehen sich auf den Text `0172-445633`.
1. Es wird als Teiltext eine der Ziffern von 0 bis 2 gesucht. Zusammenhängende Bereiche können sich also auch auf Ziffern beziehen. Gefunden werden die Ziffern 0, 1 und 2.
2. Es wird als Teiltext ein Zeichen gesucht, das `nicht` im Ziffernbereich von 0-2 liegt. Gefunden werden alle Ziffern außerhalb von 0-2 sowie alle Nicht Ziffern.
3. Es wird als Teiltext eines der Zeichen aus der angegebenen Menge von Zeichen gesucht. Gefunden werden alle Zeichen, sowie Ziffern aus dem Bereich 0, 4, 7 und -.

Es folgt der letzt Teil des Programms:

```py
tx = "aa und aba und abbaa und abbba und aca"
print(tx)

# 11: Wiederholung, beliebig oft
erg = re.findall("ab*a", tx)
print("11:", erg)

# 12: Wiederholung, 1 oder mehr
erg = re.findall("ab+a",tx)
print("12:", erg)

# 13: Wiederholung, 0 oder 1
erg = re.findall("ab?a",tx)
print("13:", erg)

# 14: Wiederholung, m bis n
erg = re.findall("ab{2,3}",tx)
print("14:", erg)

tx = "aa und aba und abba und aca und addda"
print(tx)
# 15: Wiederholung der max. Menge von Zeichen
erg = re.findall("a.*a",tx)
print("15:", erg)

# 16: Wiederholung der min. Menge von Zeichen
erg = re.findall("a.*?a",tx)
print("16:", erg)
```
```
aa und aba und abbaa und abbba und aca
11: ['aa', 'aba', 'abba', 'abbba']
12: ['aba', 'abba', 'abbba']
13: ['aa', 'aba', 'aa']
14: ['abb', 'abbb']
aa und aba und abba und aca und addda
15: ['aa und aba und abba und aca und addda']
16: ['aa', 'aba', 'abba', 'aca', 'addda']
```

Die letzten sechs regulären Ausdrücke beziehen sich auf den Text `aa und aba und abba und abbba und aca`.
 An diesemText wird das Verhalten bei der Wiederholung von Zeichen verduetlicht.

 1. `*`   Gefunden werden alle Teiltexte, die wie folgt aussehen: ein `a`, eine beliebige Zahl (auch 0) des Zeichens `b`, wiederum ein `a`. `*` bedeutet beliebige Wiederholungszahl.
 2. `+`   Gefunden werden alle Teiltexte, die wie folgt aussehen: ein `a`, mindestens ein `b`, wiederum ein `a`. `+` beliebige wiederholungsanzahl, min. 1.
 3. `?`   Gefunden werden alle Teiltexte, die wie folgt aussehen: ein `a`, kein oder ein `b`, wiederum ein `a`. `?` 1 oder 0 Wiederholungsanzahl.
 4. `{}`  Gefunden werden alle Teiltexte, die wie folgt aussehen: ein `a`, 2 oder 3mal das zeichen `b`, wiederum ein `a`. `{2,3}` - gewünschte Wiederholungsanzahl.
 5. `.*`  Gefunden werden alle Teiltexte, die wie folgt aussehen: ein `a`, anschließend so viele beliebe Zeichen wie möglich, wiederum ein `a`. `.` beliebiger Zeichen + `*` maximale Anzahl.
 6. `.*?` Gefunden werden alle Teiltexte, die wie folgt aussehen: ein `a`, anschließend so wenig beliebige Zeichen wie möglich, wiederum ein `a`. Es wird eine ganze Reihe von Zeichenfolgen gefunden, die dazu passen.

#### 7.4.2 Ersetzen von Teiltexten

Die Methode `sub()` ersetzt alle Teiltexte, die zum regulären Ausdruck passen, durch einen anderen Text. Zum leichteren Verständnis werden in diesem Programm die gleichen regulären Ausdrücke eingsetzt wie im vorherigen Programm. Alle Teiltexte, die gemäß dem Ausdruck gefunden werden, werden durch `x` ersetzt.

```py
# Modul
import re


tx = "Haus und Maus und Laus"
print(tx)

# 1: Exater Text
txneu = re.sub("Maus", "x", tx)
print("1:", txneu)

# 2: Wahl zwischen bestimmten Zeichen
txneu = re.sub("[HM]aus", "x", tx)
print("2:", txneu)

# 3: Alle Buchstaben aus Bereich
txneu = re.sub("[L-M]aus", "x", tx)
print("3:", txneu)

# 4: Alle Buchstaben nicht aus Bereich
txneu = re.sub("[^L-M]aus", "x", tx)
print("4:", txneu)

# 5: Beliebiges Zeichen
txneu = re.sub(".aus", "x", tx)
print("5:", txneu)

# 6: Suchbegriff nur am Anfang des Texts
txneu = re.sub("^.aus", "x", tx)
print("6:", txneu)

# 7: Suchbegriff nur am Ende des Texts
txneu = re.sub(".aus$", "x", tx)
print("7:", txneu)

tx = "0172-445633"
print(tx)

# 8: Alle Ziffern aus Bereich
txneu = re.sub("[0-2]", "x", tx)
print("8:", txneu)

# 9: Alle Zeichen nicht aus Ziffernbereich
txneu = re.sub("[^0-2]", "x", tx)
print("9:", txneu)

# 10: Alle Zeichen oder Ziffern, die angegeben sind
txneu = re.sub("[047-]", "x", tx)
print("10:", txneu)

tx = "aa und aba und abbaa und abbba und aca"
print(tx)

# 11: Wiederholung, beliebig oft
txneu = re.sub("ab*a", "x", tx)
print("11:", txneu)

# 12: Wiederholung, 1 oder mehr
txneu = re.sub("ab+a", "x", tx)
print("12:", txneu)

# 13: Wiederholung, 0 oder 1
txneu = re.sub("ab?a", "x", tx)
print("13:", txneu)

# 14: Wiederholung, m bis n
txneu = re.sub("ab{2,3}", "x", tx)
print("14:", txneu)

tx = "aa und aba und abba und aca und addda"
print(tx)
# 15: Wiederholung der max. Menge von Zeichen
txneu = re.sub("a.*a", "x", tx)
print("15:", txneu)

# 16: Wiederholung der min. Menge von Zeichen
txneu = re.sub("a.*?a", "x", tx)
print("16:", txneu)
```
```
Haus und Maus und Laus
1: Haus und x und Laus
2: x und x und Laus
3: Haus und x und x
4: x und Maus und Laus
5: x und x und x
6: x und Maus und Laus
7: Haus und Maus und x
0172-445633
8: xx7x-445633
9: 01x2xxxxxxx
10: x1x2xxx5633
aa und aba und abbaa und abbba und aca
11: x und x und xa und x und aca
12: aa und x und xa und x und aca
13: x und x und abbx und abbba und aca
14: aa und aba und xaa und xa und aca
aa und aba und abba und aca und addda
15: x
16: x und x und x und x und x
```

### 7.5 Audioausgabe

Das Modul `winsound` bietet unter Windows die Möglichkeit zur Ausgabe von Systemtönen und `WAV`-Dateien. Ein kleines Beispiel:

```py
import winsound, time

# Folge von Tönen mit unterschiedlicher Frequenz
for i in range (600, 1500, 200):
    print(i)
    winsound.Beep(i, 500)
    time.sleep(0.2)

# Beispiel für Systemton
print("SystemQuestion")
winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

# Beispiel für WAV-Datei
print("GAkkord.wav")
winsound.PlaySound("GAkkord.wav", winsound.SND_FILENAME)
```

Die Funktio `Beep()` sendet ein Tonsignal. Der erste Parameter steht für die Frequenz, der zweite Parameter für die Dauer des Tonsignals.

Mithilfe der Funktion `PlaySound()` können Windows-Systemtöne oder WAV-Dateien abgespielt werden. Dabei steht der erste Parameter für den Namen des Systemtons oder den Namen der WAV-Datei. Beim zweiten Parameter handelt es sich um eine Konstante. Im Fall eines Systemtons muss `SND_ALIAS` angegeben werden. Bei einer WAV-Datei ist es `SND_FILENAME`.

In Abschnitt 8.9 * Beispielprojekt Morsezeichen, sehen Sie ein weiteres Beispiel für die Nutzung des Moduls `winsound`. Dabei wird ein Text in Morsecode umgesetzt, der wiederum als Tonsignal per Lautsprecher ausgegeben wird.

**Unterschiede in Ubuntu Linux und macOS**
Das Modul `winsound` steht nicht zur Verfügung.


## Kapitel 8 Dateien

Die dauerhafte Speicherung von Daten kann in einfachen Dateien oder in Datenbanken erfolgen. In diesem Abschnitt lernen Sie verschiedene Methoden zur Speicherung von Daten in Dateien kennen.

Abschließend stele ich Ihnen das bereits bekannte Kopfrechenspiel in einer Version vor, die das dauerhafte Abspeichern des Namens und der benötigen Zeit in einer Datei ermöglicht.


### 8.1 Dateitypen

Bei der Ein- und Ausgabe von Daten in Dateien sollten Sie wissen, welcher Dateityp vorliegt und welche Zugriffsart Sie verwenden können. Wir untesrcheiden zwischen folgenden Zugriffsarten:

* Sequenzieller Zugriff: Diese Möglichkeit wird bei einer Datei bevorzugt, deren einzelne Zeilen unteschiedlich lang sind und jeweils mit einem Zeilenumbruch beendet werden. Der Inhalt der Datei kann mit einem einfachen Editor bearbeitet werden. Die Zeilen werden rein sequenziell gelesen und geschrieben. Der direkte Zugriff auf eine bestimmte Zeile ist nicht möglich, da die Länge der Vorgängerzeilen nicht bekannt ist.
* Wahlfreier Zugriff: Diese Möglichkeit haben Sie bei einer Datei, die Datensätze mit bekannter Länge enthält. Zeilenumbrüche können, müssen aber nicht existieren. Neben der Länge sollte die Struktur eines Datensatzes bekannt sein oder innerhalb der Datei an einer vereinbarten Stelle stehen. Die Zeilen können direkt gelesen und verändert werden, da man den Ort jedes Datensatzen berechnen kann.
* Binärer Zugriff: Diese Zugriffsmöglichkeit steht für alle Dateitypen zur Verfügung. Sie arbeiten mit den reinen Bytefolgen; diese können Sie mithilfe eines darauf angepassten Python-Programms lesen oder verändern. Allerdings kann das zur Folge haben, dass die Dateien nicht mehr mit den zugehörigen Anwendungsprogrammen gelesen werden können. Überschreiben Sie bspw. in einer Oracle-Datenbank die Stelle, an der die Anzahl der Datensätze einer bestimmten Tabelle steht, kann das dazu führen, dass diese Tabelle oder auch alle Tabellen zerstört werden.

Ohne Kenntnis der Struktur einer Datei ist es nicht möglich, sie richtig zu bearbeiten. Neben den genannten Typen gibt es auch Mischformen.


### 8.2 Öffnen und Schließen einer Datei

Eine Datei, die bearbeitet werden soll, muss vorher geöffnet werden. Dies geschieht mithilfe der eingebauten Funktion `open()`. Dabei werden der Name der Datei (eventuell mit Pfadangabe) und der Öffnungsmodus angegeben.

Es wird davon ausgegangen, dass sich die zu öffnende Datei im gleichen Verzeichnis wie das Python-Programm befindet. Andernfalls müssen Sie den absoluten oder relativen Pfad zur Datei angeben. Der Pfad kann gemäßg Tabelle 8.1 angegeben werden.

|Beschreibung |Pfad |
|--|--|
|zur Datei *ein.txt* im Unterverzeichnis *unt*|unt/ein.txt |
|zur Datei *ein.txt* im übergeordneten Verzeichnis |../ein.txt |
|zur Datei *ein.txt* im parallelen Verzeichnis *neb* |../neb/ein.txt |
|zur Datei *ein.txt* im Verzeichnis *C:\Temp* |C:/Temp/ein.txt |
*Tabelle 8.1 Relative und absolute Pfadangaben*

**Hinweis:**
Bei Python unte Windows sind sowohl der Forward-Slash(`/`) als auch der Back-Slash (`\`) zum Verzeichniswechsel erlaubt. Häufig wird ein Dateizugriff im Zusammenhang mit Internetserver-Programmierung genutzt. Im Internet herrschen Unix-Server vor, daher nutze ich hier die Unix-freundliche Variante mit `/` (Forward-Slash).

Die Datei kann zum Beispiel in den Modi geöffnet werden, die Sie in Tabelle 8.2 sehen.

Rückgabewert der Funktion `open()` ist ein Dateiobjekt, das für den weiteren Zugrif auf die Datei verwendet wird.

|Modus|Erläuterung |
|-|-|
|r | zum Lesen (kann auch weggelassen werden, Standard) |
|w | zum Schreiben|
|a | zum Anhängen am Ende der Datei|
|r+| zum Lesen und schreiben, aktuelle Position am Anfang|
|w+| zum Lesen und Schreiben, Datei wird geleert|
|a+| zum Lesen und Schreiben, aktuelle Position am Ende|
|b | zum Öffnen einer Datei im Binärmodus, die gelesen oder geschrieben werden soll. Es handelt sich um eine zusätzliche Angabe, siehe auch Abschnitt 8.5, Serialisierung.|
*Tabelle 8.2 Öffnungsmodi* 

In jedem Dateiobjekt ist die aktuelle Zugriffsposition gespeichert. Dies ist die Position, an der aktuell gelesen oder geschrieben wird. Sie verändert sich mit jedem Lese- oder Schreibvorgang. Außerdem kann sie mit der Funktion `seek()` verändert werden, ohne lesen und schreiben zu müssen.

Nach er Bearbeitung muss eine Datei mit de rFunktion `close()` geschlossen werden. Wird sie nicht geschlossen, ist sie eventuell für weitere Zugriffe gesperrt.

### 8.3 Sequenzielle Dateien
Dateien können sequenziell beschrieben oder gelesen werden.

#### 8.3.1 Sequenzielles Schreiben

Zum Schreiben in eine Datei muss diese zunächst mit der Funktion `open()` und dem Öffnungsmodus `w` geöffnet werden. Wenn die Datei noch nicht existiert, wird sie in diesem Moment erzeugt. Achtung: Wenn sie bereits existiert, wird sie ohne Vorwarnung überschrieben!

Beim Öffnen einer Datei im Schreibmodus kann ein Laufzeitfehler auftreten (z. B. beim Schreiben auf ein schreibgeschütztes Medium oder ein nicht vorhandenes Laufwerk). In diesem Fall sollten Sie eine Ausnahmebehandlung mit einem Programmabbruch durchführen. Dazu können Sie die Methode `exit()` aus dem Modul `sys` nutzen.

Falls es keinen Abbruch gibt, können Sie mithilfe der Funktion `write()` einzelne Strings und mit der Funktion `writelines()` eine Liste von Strings in die Datei schreiben. Zahlen können Sie zuvor mitilfe der Funktion `str()` in einen String umwandeln. Das Zeichen `\n` (new line) für das Zeilenende müssen Sie jeweils hinzufügen.

```py
import sys

# Zugriffsversuch
try:
    d = open("schreiben.txt","w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Schreiben von einzelnen Strings, mit Zeilenende
d.write("Die erste Teile \n")
for i in range(2, 11, 2):
    d.write(str(i) + " ")
d.write("\n")

# Schreiben einer Liste
x = ["abc\n", str(12/7.5)+"\n", "xyz\n"]
d.writelines(x)

# Schliessen der Datei
d.close()
```
Die Datei *schreiben.txt* ha anschließend den folgenden Inhalt:
```
Die erste Teile 
2 4 6 8 10 
abc
1.6
xyz
```
Zunächst wird eine einzelne Textzeile mit der Funktion `write()` in die Datei geschrieben. Anschließend werden die Zahlen der Zahlenfolge `2, 4, 6, 8, 10` jeweils in einen String umgewandelt und in die Datei geschrieben. Nach jdeder Zeile wird zusätzlich ein Zeilenende ausgegeben.

Es wird die Liste `x` erzeugt. Die Elemente dieser Liste sind Strings, die mit dem Zeilenende-Zeichen enden. Die Liste wird mithilfe der Funktion `writelines()` in die Datei geschrieben.

**Hinweis:** Verwenden Sie beim Öffnen der Datei den Öffnungsmodus `a` statt `w` (`d = open("schreiben.txt", "a")`), werden die Ausgaben an den bisherigen Dateiinhalt angehängt. Die Datei wird also immer größer.

**Unterschiede unter Ubuntu Linux und macOS:** Das Erzeugen von dateien mithilfe eines Python-Programms kann misslingen, alls nicht Sie der Besitzer der Datei mit dem Python-Programm sind, sondern gegebenenfalls der Benutzer "root".


### 8.3.2 Sequenzielles Lesen

Die Zeilen einer sequenziellen Datei können Sie mithilfe verschiedener Funktionen lesen.
Die Funktion `readlines()` liest alle Zeilen der Datei auf einmal in eine Liste von Strings. Die Funktion `readline()`liest jeweils eine einzelne Zeile einer Datei in einem String. Die Funktion `read()` liest alle Zeilen der Datei auf einmal in einen String.

#### Beispiel 1
Zunächst werden alle Zeilen einer Datei mithifle der Funktion `readlines()` auf einmal in eine Liste gelesen:

```py
import sys
# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen aller Zeilen in eine Liste
allezeilen = d.readlines()

# Schliessen der Datei
d.close()

# Ausgabe und Summierung der Listenlelemente
summe = 0
for zeile in allezeilen:
    print(zeile, end="")
    summe += float(zeile)

# Ausgabe der Summe
print("Summe:", summe)
```
Die Datei lesen.txt hat folgenden Inhalt
```
6.
2.5
4
```
Die Ausgabe des Programms lautet:
```
6
2.5
4
Summe: 12.5
```
Zunächst öffnen Sie die Datei mithilfeder FUnktion `open()` zum Lesen. Den Öffnungsmodus können Sie in diesem Fall weglassen. Gelingt das Öffnen der Datei nicht, tritt eine Ausnahme auf. Dies geschieht z. B., wenn Folgendes der Fall ist:
* Die Datei existiert nicht.
* Der Name der Datei ist falsch geschrieben
* Die Datei beindet sich in einem anderen Verzeichnis.
  
Die Funktion `readlines()` wird auf das Dateiobjekt angewendet. Sie liefert eine Liste von Strings. jede String enthält eine Zeile inklusive Zeilenende. Die Strings können unterschiedlich lang sein.

Alle Elemente der Liste werden auf dem Bildschirm ausgegeben. Sie beinhalten bereits das Zeichen für das Zeilenende. Daher wird kein zusätzliches Zeichenende ausgegeben. Ansonsten würden unnötige Leerzeilen entstehen.

Die Elemente der liste werden mithilfe der Funktion `float()` in Zahlen umgewandelt und anschließend summiert. Die Summe wird ausgegeben

#### Beispiel 2
Im folgenden Programm werden einzelne Zeilen einer Datei mithilfe der Funktion `readline()` gelesen:

```py
import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit()

# Lesen und Ausgabe einzelner Zeilen
zeile1 = d.readline()
print(zeile1, end="")
zeile2 = d.readline()
print(zeile2, end="")

# Summierung und Ausgabe
summe = float(zeile1) + float(zeile2)
print("Summe:", summe)

# Schliessen der Datei
d.close()
```

Nach dem erfolgreichen Öffnen der Datei sit die aktuelle Leseposition der Anfang der ersten Zeile. Die Funktion `readline()` ergibt einen String, der eine Zeile inklusive Zeilenende enthält. Nach einem Aufruf von `readline()` ist die aktuelle Leseposition der Anfang der nächsten Zeile. Daher wird beim zweiten Aufruf die zweite Zeile gelesen usw.

#### Beispiel 3
Auch mit der Funktion `readline()` können Sie alle Zeilen einer Datei lesen.

Dazu ist es notwendig, dass Ende der Datei zu erkennen. Zu diesem Zweck prüfen Sie den gelieferten String.

```py
import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen, Ausgabe und Summierung aller Zeilen

summe = 0

zeile = d.readline()
while zeile:
    summe += float(zeile)
    print(zeile, end="")
    zeile = d.readline()

# Ausgabe der Summe
print("Summe:", summe)

# Schließen der Datei
d.close()
```
Das Lesen der Zeilen wird mithilfe einer `while`-Schleife gesteuert:

* Falls das Dateiende noch nciht erreicht ist, ist der String `zeile` nicht leer. Die Bedingung `while zeile` ist wahr, und die Schleife wird weiter ausgeführt.
* Falls das Dateiende erreicht ist, ist der String `zeile` leer. Die Bedingung `while zeile` ist falsch, und die Schleife wird beendet.

#### Beispiel 4

Die Funktion `read()` liest den gesmaten Inhalt einer Datei in einen einzigen String. Dieser muss anhand des Zeilenende-Zeichens in einzelne Zeilen zerlegt werden. 

```py
import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit()

# Lesen des gesamten Texts
gesamtertext = d.read()

# Schliessen der Datei
d.close()

# Umwandeln in eine Liste
zeilenliste = gesamtertext.split(chr(10))

# Summieren und Ausgeben
summe = 0
for zeile in zeilenliste:
    if zeile:
        summe += float(zeile)
    print(zeile)

# Summe ausgeben
print("Summe:", summe)
```
All Zeilen werden mithilfe der Funktion `read()` in einen String gelesen. Der String wird anhand des Zeilenende-Zeichens (Unicode-Zahl 10) mithilfe der Funktion `split()` in einzelne Zeilen zerlegt.

Über eine `while`-Schleife wird das Bearbeiten der einzelnen Zeilen gesteuert. Die Inhalte der Zeilen werden umgewandelt, summiert und ausgegeben. Anschließend wird die Summe ausgegeben.

#### 8.3.3 CSV-Datei schreiben
CSV-Dateien (Comma-separated Values) sind Textdateien, in denen ein Datzensatz pro Zeile steht. Die Daten des Datensatzes sind durch festgelegte Zeichen (wie Semikola) voneinander getrennt. solche Dateien haben meist die Dateiendung *.csv*. Sie können von bestimmten Programmen (z.B. MS Excel oder Libreoffice Calc) erkannt und richtig genutzt werden.

Neben den Beispielen in diesem Abschnitt finden Sie in Abschnitt 8.10 >Spiel, Version mit Highscore-Datei<, eine weitere Version des bereits bekannten Kopfrechenspiels. Darin werden die Daten des Spielers (Name und benötigte Zeit) in einer CSV-Datei gespeichert, sodass Sie eine Highscore-Liste führen können.

Ein beispiel, in dem eine einfache Liste und eine zweidimensionale Liste als CSV-Datensätze in eine Datei geschrieben werden:

```py
import sys
# Zugriffsversuch
try:
    d = open("daten.csv","w")
except:
    print("Dateizugriff nicht erfolgreich")

# Schreiben einer Liste als CSV-Datensatz
li = [42, "Maier", 3524.52]
d.write(str(li[0]) + ";" + li[1] + ";" + str(li[2]).replace(".",",") +"\n")

# Schreiben einer zweidim. Liste als Datensatztabelle
dli = [[55, "Göçlü", 3185.00], [57, "Wäßmann", 2855.20]]
for element in dli:
    d.write(str(element[0]) + ";" + element[1] + ";" + str(element[2]).replace(".",",") +"\n")

# schliessen der Datei
d.close()

```
Die Ausgabedatei *daten.csv* hat anschließend den folgenden Inhalt:
```
42;Maier;3524,52
55;Göclü;3185,0
57;Wäßmann;2855,2
```

Nach dem erfolgreichen öffnen werden die einzelnen Elemente der einfachen Liste mithilfe der Funktion `write()` in die Datei geschrieben. Zwischen den Elementen wird jeweils ein Semikolon eingefügt.

Handelt es sich bei einem Element um eine Zahl, so wird sie in eine Zeichenkette umgewandelt. Bei Zahlen mit Nachkommastellen wird anschließend der Dezimalpunkt mithilfe der Funktionen `replace()` in ein Komma verwandelt. Damit können diese Zahlen problemlos von einer deutschen Version von MS Excel eingelesen werden.

Zur Gewährleistung eines erfolgreichen Exports muss also die Struktur der Daten bekannt sein. Die Daten der verschiedenen Datentypen müssen individuell verarbeitet werden. Falls MS Excel unter Windows installiert ist, genügt ein Doppelklick auf die Ausgabedatei *daten.csv*, um den Inhalt als Tabelle in MS Excel darzustellen. Dank der UTF-8-Kodierung sind auch Umlaute, Eszetts oder Zeichen aus anderen Zeichensätzen kein Problem, siehe Abildung 8.1.

**Unterschiede unter Ubuntu Linux und macOS** Unter Ubuntu Linux und macOS können sie die Datei mithilfe eines doppelklicks auf den Datennamen in der Verzeichnisanzeige mit LibreOffice Calc öffnen. Es wird das Dialogfeld Textimport geöffnet.

Achten Sie darauf, dass im Bereich Trennoption nur die Option Getrennt und Semicolon makiert sind. Falls Sie zusätzlich die Option Komma markierne, würden die Zahlen mit Nachkommastellen auf zwei Spalten aufgeteilt. Anschließend werden die Daten korrekt dargestellt wie in MS Excel unter Windows.

Gegebenenfalls müssen Sie in der Liste Zeichensatz den Eintrag System auswählen.

#### 8.3.4 CSV-Datei lesen

Zum erfolgreichen Import einer CSV-Datei müssen die Strktur und die datentypen der Daten bekannt sein. Für das nachfolgende beispiel wird die CSV-Datei uas dem vorherigen beispiel in MS Excel ergänzt und abgespeichert, siehe Abbildung 8.2.

Die Datei wird mit dem folgenden Programm gelesen. Die Datensätze werden in einer zweidimensionalen Liste abgelegt.

```py
import sys
# Zugriffsversuch

try:
    d = open("daten.csv")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen des gesamten Texts
gesamtertext = d.read()

# Schliessen der Datei

d.close()

# Umwandeln in eine Liste von Zeilen

zeilenliste = gesamtertext.split(chr(10))

# Jede Zeile umwandeln in Liste von int, string, float
li = []
for zeile in zeilenliste:
    zwliste = zeile.split(";")
    li.append([ int(zwliste[0]), zwliste[1], float( zwliste[2].replace(",",".") ) ])

# Ausgabe
for p in li:
    print(f"{p[0]:d} {p[1]} {p[2]:.2f}")
```
```
42 Maier 3524.52
55 Göclü 3185.00
57 Wäßmann 2855.20
98 Esser 3120.66
```

Zunächst wird der gesamte Text der Datei mit der Funktion `read()` in einen String eingelesen. Dieser String wird mithilfe der Funktion `split()` anhand des Zeilenende-Zeichens (Unicode-Zahl 10) in eine Liste von Zeilen zerelgt. Die Elemente der Liste enthalten nicht mehr das Zeilenende-Zeichen.

Jedes Element der lsite, also jede Zeile, wird wiederum mithilfe der Funktion `split()` anhand des Semikolons in eine Zwischenliste (zwliste) mit den einzelnen Daten zerlegt. Diese Zerlegung wird nur durch geführt, wenn die Zeile nicht leer ist.

Handelt es sich bei einem Element der Zwischenliste um eine Zahl, so wird sie mithilfe der Funktion `int()` oder mit der FUnktion `float()` umgewandelt. Bei Zahlen mit Nachkommastellen wird vorher das KOmma mithilfe der Funktion `replace()` in einen Dezimalpunkt verwandelt. Damit kann diese Zahl, die aus einer deutschen Version von MS Excel kommt, problemlos weiterverarbeitet werden.

Zuletzt werden die Elemente der zweidimensionalen liste zeilenweise formatiert ausgegeben.

### 8.4 Dateien mit festgelegter Struktur

Falls eine Datei *formatiert* beschrieben wird, ist ihre Struktur festgelegt. Es ist genau bekannt, an welcher Stelle welche information steht. Somit können die gewünschten Informationen direkt aus der Datei gelesen werden, ohne die gesamte Datei Zeile für Zeile einlesen zu müssen.

Außerdem ist es möglich, bestimmte Informationen *punktuell* zu verändern, ohne den restlichen Inhalt der Datei zu beeinflussen. Beide Möglichkeiten werden in den foolgenden Abschnitten vorgeführt.

#### 8.4.1 Formatiertes Schreiben

Das formatierte Schreiben in eine Datei ähnelt einer formatierten Ausgabe auf dem Bildschirm. Es werden Datensätze mit gleicher Länge und gleichem Aufbau gebildet.

Optional können Sie nach jedem Datensatz ein Zeilenende-Zeichen einfügen, um die Datei in einem Editor leichter lesbar zu machen. sie können die Datei auch mithilfe des Editors verändern, solange Sie sich an die festgelegte Struktur halten.

Ein Beispiel:

```py
import sys
# Zugriffsversuch
try:
    d = open("obst.txt", "w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Tabelle mit vesrchiendenen Objekten
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:2, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}


d.write(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'EP':>13}{'GP':>13}\n")

for x in 23, 8, 42:
    d.write(f"{x:04d}{artname[x]:>12}{anzahl[x]:>4d}{epreis[x]:>8.2f} Euro{anzahl[x]*epreis[x]:>8.2f} Euro\n")

# Schliessen der Datei
d.close()
```
```
  Nr        Name Anz           EP           GP
0023       Apfel   1    2.95 Euro    2.95 Euro
0008      Banane   2    1.45 Euro    2.90 Euro
0042    Pfirsich   5    3.05 Euro   15.25 Euro
```

Die Datei wird zum Schreiben geöffet. Die einzelnen Datensätze werden mithifle von formatierten String-LIteralen erzeugt, wie in Abschnitt 5.2.2, 'Formatierung mit String-Literalen', beschrieben. Zusätzlich wird jeweils eine `\n` ans Zeilenende angefügt.

#### 8.4.2 Lesen anbeliebiger Stelle

Die Funktion `seek()` ermöglicht die Änderung der katuellen Lese- oder Schreibposition innerhalb der Datei. Sie kann mit einem oder zwei Parametern aufgerufen werden. Wird sie mit einem Parameter aufgerufen, handelt es sich dabei um den Abstand Byte, gemessen vom Dateianfang. Der Dateianfang entspricht dem Wert 0, der Aufruf würde in diesem Fall lauten: `d.seek(0)`

Die gewünschte Position wird direkt erreicht, ohne LEsen der Informationen, die von der Position stehn. Ausgehend von der erreichten Position kann gelesen oder geschrieben werden.

Die Funktion `seek()` wird hier zusammen mit einer Variante der Funktion `read()` eingeführt. Diese Funktion gestattet neben dem Einlesen einer ganzen Datei (wie am Anfang dieses Kapitels gezeigt) auch das Einlesen einer bestimmten Anzahl von Bytes, falls die Funktion mit der entsprechenden Zahl als Parameter angegeben wird. Ein Beispiel:

```py
import sys

# Zugriffsversuch

try:
    d = open("obst.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Gezieltes Lesen
for i in range (1,4):
    # Nr Lesen
    d.seek(48*i)
    nr = int(d.read(4))

    # EP lesen
    d.seek(20 + 48*i)
    ep = float(d.read(8))

    # Ausgabe
    print("Arikel Nr:", nr, "EP:", ep)

# Schließen der Datei
```
```
Arikel Nr: 23 EP: 2.95
Arikel Nr: 8 EP: 1.45
Arikel Nr: 42 EP: 3.05
```

Jeder Datensatz(also jede Zeile) hat eine Gesamtlänge von 48 Byte inklusive der zwei Zeichen, die durch das `\n` erzeugt werden. Die erste Zeile beginnt an Position 0 und enthält die Überschrift. Die zweite Zeile beginnt an Position 48 und enthält den ersten Datzensatz. DIe dritte Zeile beginnt an Position 96 und enthält den zweiten Datensatz uswl.

Im Programm wird die Datei zunächst zum Lesen geöffnet. Anschließend werden mithifle der Funktion `seek()` nacheinander POsitionenen im ersten, zweiten und dritten Datensatz erreicht. Dies sind:
* die Positionen 48, 96 und 144 zum Lesen der Artikelnummer am Anfang jedes Datensatzes
* die Positionen (48 + 20 =)68, 116 und 164 zum Lesen des Einzelpreises jedes Artikels

An diesen Positionenen werden die nächsten 4 Byte (die Artikelnummer) bzw. die nächsten 8 Byte (der Einzelpreis) mithilfe der Funktion `read()` gelesen. Sie liefert jeweils eine Zeichenkette, die mithilfe von `int()` bzw. `float()` in eine Zahl umgewandelt wird. Die Zahlen werden anschließend ausgegeben.

**Unterschiede unter Ubuntu Linux und macOS:** Das Zeichen `\n` für das Zeilenende erzeugt beim Schreiben der Datensätze nur ein Zeichen, nicht zwei Zeichen wie unter Windows. Daher ist ein Datensatz 47 statt 48 Zeichen lang.

#### 8.4.3 Schreiben an beliebiger Stelle

Sie können eine Datei im Modus `r+` öffnen. Anschließend können Sie sie sowohl lesen als auch schreibend ändern. Im nachfolgenden Programm werden der aktuelle Einzelpreis under zugehörige Gesamtpreis eines bestimmten Artikels gelesen, verändert und neu in die Datei geschrieben.

```py
import sys

# Zugriffsversuch
try:
    d = open("obst.txt", "r+")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)


# Lesen des Einzelpreises
d.seek(68)
ep_str = d.read(8)
ep = float(ep_str)

# Schreiben des Einzelpreises
d.seek(68)
ep = ep + 0.2
d.write(f"{ep:8.2f}")

# Lesen des Gesamtpreises
d.seek(81)
gp_str = d.read(8)
gp = float(gp_str)

# Schreiben des Gesamtpreises
d.seek(81)
gp = gp + 0.2
d.write(f"{gp:8.2f}")

# Schließen der Datei
d.close()
```
```
  Nr        Name Anz           EP           GP
0023       Apfel   1    3.15 Euro    3.15 Euro
0008      Banane   2    1.45 Euro    2.90 Euro
0042    Pfirsich   5    3.05 Euro   15.25 Euro
```

Der Einzelpreis des Artikel 23 im ersten Datensatz wird von 2,95 Euro auf 3,15 Euro erhöht. Dazu wird die Datei zunächst im Modus `r+` geöffnet. Der Einzelpreis steht als Zeichenkette in der 8 Byte ab der Position 68. Diese Zeichenkette wird gelesen und in eine Zahl umgewandelt.

Diese Zahl wird gändert, in eine Zeichenkette umgewandelt, mit einer Breite von 8 Byte formatiert und ab der Position 68 in die Datei geschrieben. Das gleiche geschieht mit dem Gesamtpreis ab Position 81.

**Unterschiede Ubuntu Linux und macOS**: Weil `\n` auch hier nur 1 Byte einnimmt anstelle von 2 wie bei Windows verschieben sich hier die Positionen um eins nach links.

### 8.5 Serialisierung

Das Modul `pickle` dient zur Serialisierung und Deserialisierung von Objekten. Das können Objekte der eingebauten Objekttypen oder Objekte eingener Klassen sein.

Bei der Serialisierung werden die Objekte als Bytefolge in einer Datei gespeichert. Bei der Deserialisierung werden die Objekte wieder aus einer Datei geladen. Beim Speichern wird der Typ des Objekts hinzugefügt, sodass er beim Laden bekannt ist.

Neben den Beispielen in diesem Abschnitt finden Sie in Abschnitt 8.10 eine weitere Version des bereits bekannten Kopfrechenspiels. Die Daten des Spielers (Name und Zeit) werden mithilfe der Serialisierung dauerhaft gespeichert, sodass eine Highscore-Liste geführt werden kann.


#### 8.5.1 Objekte in Datei schreiben
Zum Serialisieren von Objekten dient die Methode `dump()`. Im folgenden Beispiel werden ein Objekt eines eingebauten Objekttyps und ein Objekt einer eigenen Klasse nacheinander in einer Datei gespeichert.

```py
import pickle, sys

# Definition der Klasse Fahrzeug

class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"

# Zugriffsversuch
try:
    d = open("objekt.bin", "wb")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Eingebautes Objekt
x = ([4, "abc", 8], "xyz")
print(x)
pickle.dump(x, d)

# Objekt der eigenen Klasse
opel = Fahrzeug("Opel Admiral", 40)
print(opel)
pickle.dump(opel, d)

# Variable Anzahl an Objekten
pickle.dump(3, d)
pickle.dump("Berlin", d)
pickle.dump("Hamburg", d)
pickle.dump("Dortmund", d)

# Datei schliessen
d.close()
```

DAs Programm beginnt mit der Definition der Klasse `Fahrzeug`, die Sie bereits aus Kapitel 6 zur objektorientierten Programmierung kennen.

Die Datei wird im Modus `wb` geöffnet, also zum Schreiben im Binärmodus. Als zusätzlicher Hineis auf den Binärmodus habe ich die Dateiendung *.bin* gewählt.

Es wird eine zweidimensionale Liste erzeugt und zur Kontrolle auf dem Bildschirm ausgegeben. Mithilfe der Funktion `dump()` aus dem Modul `pickle` wird die Liste binär in der geöffneten Datei gespeichert. Der erste Parameter der Funktion ist der Name des Objekts, der zweite Parameter ist das Dateiobjekt.

Außerdem wird ein Objekt der Klasse `Fahrzeug` erzeugt. Dieses Objekt wird zur Kontorlle auf dem Bildschirm ausgegeben. Anschließend wird es binär in der geöffneten Datei gespeichert.

Falls Sie eine bestimmte Anzahl von Objekten speichern möchten, hier z.B. drei Zeichenketten, speicher Sie zunächst diese Anzahl. Anschließend speicher sie die Objekte selbst. Auf diese Weiße kann später die richtige Anzahl von Objekten wieder geladen werden (siehe auch nachfolgend den Abschnitt 8.5.2).

**Hinweise:** Ein potenzieller Inhalt der Datei wird überschrieben. Es könnten auch Objekte an vorhandene Objekte angehängt werden. Zz diesem Zweck hätten Sie die Datei im Öffnungsmodus `ab` öffnen müssen.

 Mithilfe eines Editors können sie ledigleich die Zeichenketten innerhalb der Binärdatei erkennen. Die Datei kann nur mithilfe der genannten Methoden geschrieben oder gelesen werden.

 #### 8.5.2 Objekte aus Datei lesen

 Objekte, die mit der Funktion `dump()` in einer Datei gespeichert wurden, können Sie mit `load()` wieder in der gleichen Reihenfolge aus der Datei in ein Programm übernehmen. Handelt es sich um ein Objekt einer eigenen Klasse, muss die Definition dieser Klasse bekannt sein.

 Es folgt ein Beispiel, in dem die Objekte, die mithilfe des Programms aus dem vorhiergen Abschnitt serialisiert wurden, wieder deserialisiert und in ein Programm übernommen werden.

 ```py
import pickle, sys

# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"


# Zugriffsversuch
try:
    d = open("objekt.bin", "rb")
except:
    print("Dateizugriff nicht erfolgreich!")
    sys.exit(0)

# Eingebautes Objekt
x = pickle.load(d)
print(x)

# Objekt der eigenen Klasse
opel = pickle.load(d)
print(opel)

# Variable Anzahl an Objekten
anzahl = pickle.load(d)
for i in range(anzahl):
    print(pickle.load(d))

# Datei schliessen
d.close()
```
```
([4, 'abc', 8], 'xyz')
Opel Admiral 40km/h
Berlin
Hamburg
Dortmund
```
An der Ausgabe erkennen Sie, dass die Objekte wieder *originalgetreu* geladen werden. Das Programm beginnt mit der Definition der eigenen Klasse `Fahrzeug`. Die Datei wird im Modus `rb` geöffnet, also zum Lesen im Binärmodus.

Mithilfe der Funktion `load()` aus dem Modul `pickle` werden nacheinander die Liste und das Objekt der Klasse `Fahrzeug` geladen. Anschließend wird die Anzahl der nachfolgdnen Objekte als Zahl geladen (hier: 3). Damit ist die Anzahl der zu landenden Objekte für die Schleife bekannt. Alle Objekte werden zur Kontorlle auf dem Bildschirm ausgegeben.

### 8.6 Bearbeitung mehrer Datien

Bisher wurde immer nur eine einzelne Datei bearbeitet, deren Name bekannt war. Falls Sie vor der Aufgabe stehen, mehrere Dateien aus einem Verziehcnis zu bearbeiten, deren Anzahl und Namen unbekannt sind, können Sie sich der Funktion `glob()` aus dem Modul `glob` und der Funktion `scandir()` aus dem Modul `os` beidneen. Sie liefern jeweils eine Liste, die einen Zugriff auf die einzlenen Dateien ermöglicht.

##### 8.6.1 Funktion `glob.glob()`

Im folgenden Beispiel werden zunächst die Namen bestimmter Dateien aus dem aktuellen Verzeichnis mithilfe der Funktionen `glob()` in eine Liste gespeichert. Diese Dateien werden der Reihe nach geöffnet und durchsucht.Wir in einer der Dateien ein bestimmter Suchtext gefunden, so wird ihr Name jweils ausgegeben.

```py
import glob

# Liste der Dateien
dateiliste = glob.glob("schr*.py")
print(dateiliste)

# Jedes Element der Liste durchsuchen
for datei in dateiliste:
    # Zugriffsversuch
    try:
        d = open(datei)
    except:
        print("Dateizugriff nicht erfolgreich")
        continue

    gesamtertext = d.read()

    # Zugriff beenden
    d.close()

    # Suchtext suchen
    if gesamtertext.find("obst") != -1:
        print(datei)
```
```
schreiben_beliebig.py
schreiben_formatiert.py
```

Der Parameter der Funktion `glob()` ist eine Zeichenkette, die als Filter für die Dateisuche dient. Die Zeichenkette kann auch einen der Platzhalter `*` (für mehrere beliebige Zeichen) oder `?` (für ein einzelnes beliebiges Zeichen) enthalten. Hier wird nur nach Dateien gesucht, deren Name mit `schr` beginnt und mit `.py` endet.

Jedes Element der erzeugten Liste entsrpicht einem Dateinamen. Jede dieser Dateien wird geöffnet. Falls das Öffnen nicht erfolgreich war, wird mit der nächsten Datei fortgefahren.

Der vollständige Inhalt der jeweiligen Datei wird mithilfe der Funktion `read()` in eine Zeichenkette eingelesen. Anschließend wird die Datei wieder geschlossen.

Die Zeichenkette wird mithilfe der Funktion `find()` durchsucht. Dird der Suchtext gefunden, so wird der Dateiname ausgegeben.

Seit Python 3.5 können Sie mit der Funktion `glob.glob()` und der Zeichenfolge `**` auch rekursiv einen gesamten Verzeichnisbaum druchsuchen. In den folgenden Vergelichsbeispielen wird eine Liste aller Dateien mit der Endung `.py` geliefert, deren Name mit `c` beginnt:
* `glob.glob("c*.py")` durchläuft nur das aktuelle Verzeichnis.
* `glob.glob("**/c*.py")` durchläuft nur direkte Unterverzeichnisse.
* `glob.glob("**/c*.py", recursive=True)` durchläuft das aktuelle Verzeichnis, direkte Unterverzeichnisse, deren Unterverzeichnisse usw., also den gesamten Verziehcnisbaum.

#### 8.6.2 Funktion `os.scandir()`

Seit Python 3.5 gibt es mit der FUnktion `scandir()` aus dem Modul `os` eine schnellere Alternative zum Durchlaufen eines Verzeichnisses. Das nachfolgende Programm liefert dasselbe Ergebnis wie oben:

```py
import os
eintrag_iterator = os.scandir(".")

# Alle Dateien eines Verzeichnisses
for x in eintrag_iterator:
    # Nur falls gemäß schr*.py
    if x.name.startswith('schr') and x.name.endswith('.py'):
        # Zugriffsversuch
        try:
            d = open(x)
        except:
            print("Dateizugriff nicht erfolgreich")
            continue

        # Text einelsen
        gesamtertext = d.read()

        # Zugriff auf Datei beenden
        d.close()

        # Suchtext suchen

        if gesamtertext.find("obst") != -1:
            print(x.name)
        
# Schließt den Iterator
eintrag_iterator.close()
```
Die FUnktion `scandir()` erwartet den Namen eines Prads als Parameter. Hier wird das aktuelle Verzeichnis angegeben. Die Funktion liefert ein Iterator-Objekt vom Type `os.DirEntry`, mit dessen hilfe alle Einträge des Verzeichnisses durchlaufen werden.

Die Eigenschaft `name` des `DirEntry`-Objekts beinhaltet den Namen des Verzeichniseintrags. Falls dieser mit `schr` beginnt und mit `.py` endet, wird die betreffende ZDatei wie oben weiterbearbeitet.

Seit Python 3.6 haben sie die Möglichkeit, den Iterator mithifle von `close()` zu schließen und die genutzten Ressourcen wieder freizugeben.

### 8.7 Informationen über Dateien

Die funktion `stat()` aus dem Modul `os` liefert eine Reihe von Informationen über Dateien in Form eines Tupels.

Ein Beispiel:

```py
import os, time

# Informationstupel
tu = os.stat("obst.txt")
print(tu)

# Elemente des Tupels
groesse = tu[6]
print("Byte:", groesse)

zugr = time.localtime(tu[7])
print("Letzter Zugriff:", time.strftime("%d.%m.%Y %H:%M:%S", zugr))

mod = time.localtime(tu[8])
print("Letzte Modifikation:", time.strftime("%d.%m.%Y %H:%M:%S", mod))
```
```
Byte: 192
Letzter Zugriff: 15.10.2020 18:58:01
Letzte Modifikation: 15.10.2020 16:27:04
```
As dem gelieferten Tupel werden die folgenden Informationen geholt:
* aus Element 6 die Größe der Datei in Byte
* aus Element 7 der Zeitpunkt des letzten Zugriffs auf die Datei
* aus Element 8 der Zeitpunkt der letzten Änderung der Datei
  Beide Zeitangaben werden mithilfe der Funktion `localtime()` umgewandelt, mithilfe der Funktion `strftime()` formatiert und anschließend ausgegeben.

**Unterschiede unter Ubuntu Linux und macOS**
Die Datensätze haben nur eine Länge von 47 statt 48 Zeichen. Damit ergibt sich eine Dateigröße von 188 Byte.

### 8.8 Dateien und Verzeichnisse verwalten
Die Module `os` und `shutil` bieten weitere Funktionen zur Verwaltung von Dateien und Verzeichnissen. Im folgenden Beispiel werden Dateien kopiert, umbenannt und gelöscht.

```py
import sys, shutil, os, glob

def check():
    print(glob.glob("le*.txt"))

check()

# Existenz feststellen
if not os.path.exists("lesen.txt"):
    print("Datei nicht vorhanden")
    sys.exit(0)

# Datei kopieren
shutil.copy("lesen.txt", "lesen_kopie.txt")
check()

# Datei umbennen
try:
    shutil.move("lesen_kopie.txt","lesen_neu.txt")
except:
    print("Fehler beim umbenennen")
check()
```
```
['lesen.txt']
['lesen.txt', 'lesen_kopie.txt']
['lesen.txt', 'lesen_neu.txt']
['lesen.txt']
```

Die erste Zeile er Ausgabe liefert die ursprüngliche Liste derjenigen Dateien, die mit `le` beginnen und mit `.txt` enden.

Mithilfe der FUnktion `exists()` aus dem Modul `os.path` wird geprüft, ob eine bestimmte Datei existiert, die kopiert werden soll. Falls sie nicht existiert, wird das Programm vorzeitig beendet.

Anschließen wird die Datei *lesen.txt* mithilfe der Funktion `copy()` aus dem Modul `shutil` kopipert. Die Kopie heißt *lesen_kopie.txt*. Die zweite Zeile der Ausgabe liefert die geänderte Liste der Dateien.

Nun wird die Datei * lesen_kopie.txt* mithilfe der Funktion `move()` aus dem Modul `shutil` in *lesen_neu.txt* umbenannt. Die nächste Zeile der Ausgabe liefert die geänderte Liste der Dateien. Die Methode `move()` kann auch zum Verschieben einer Datei in ein anderes Verzeichnis genutzt werden.

Als Letztes wird die Datei *lesen_kopie.txt* mithilfe der Funktion *remove()* aus dem Modul `os` wieder gelöscht. Die letzte Zeile der Ausgabe liefert wiederum die geänderet Liste der Dateien.

### 8.9 Beispielprojekt Morsezeichen

In diesem Abschnitt sehen Sie ein Beispielprojekt, in dem auf Dateien, externe Module, Zeichenketten, Dictionarys, einige Funktionen und das Modul `winsound` zur Ausgabe von Tönen (siehe 7.5) zugegriffen wird.

Ein Beispieltext wird in Morsecode umgesetzt. Es besteht aus einzelnen Morsezeichen und Pausen. Ein Morsezeichen steht für ein einzelnes Zeichen eines Texts und setzt sich aus einer Folge von kurzen und lnagen Signalen zusammen. Damit werden bereits seit langer Zeit Texte als eine Folge von Ton-, Funk- oder LIchtsignalen übermittelt.

#### 8.9.1 Morsezeichen aus Datei lesen

Zunächst werden die verschiedenen Zeichen und das jeweils zugehörige Morsezeichen aus der Datei *morsen.txt*  in ein Dictionary gelesen. In der Datei wird ein kurzes Signal durch einen Punkt dargestellt, ein langes Signal durch einen Strich. Die einzelnen Zeichen und das dazugehörige Morsezeichen sind jeweils durch ein Leerzeichen getrennt:

```
A .-
B -...
C -.-.
D -..
E .
...
```
Zum Lesen dient eine Funktion im nachfolgenden Modul `morsen`, die anderen Python-Programmen zur Verfügung gestellt werden kann:

```py
import sys
# Erstellt Dictionary mit Morsezeichen aus Datei

def leseCode():
    # Lesen der Datei mit Zeichen und Morsezeichen
    try:
        d = open("morsen.txt")
    except:
        print("Dateifehler")
        sys.exit(0)
    
    allezeilen = d.readlines()
    print(allezeilen)
    d.close

    # Erste Zeichenketet in dder Zeile ist das Zeichen
    # Es dient als Schlüssel für das Dictionary
    code = {}
    for zeile in allezeilen:
        worte = zeile.split()
        code[worte[0]] = worte[1]

    # Morsezeichen gleich, ob kleine oder große Buchstaben
    for i in range(97,123):
        code[chr(i)] = code[chr(i-32)]
    
    # Liste zurückliefern
    return code
```
In der Funktion `leseCode()` werden zuerst alle Zeilen der Datei *morsen.txt* gelesen. Anschließend wird ein leeres Dictionary erzeugt.

Jede Zeile wird anhand des Leerzeichens in zwei Zeichenketten zerlegt. Die erste Zeichenkette beinhaltet ein Unicode-Zeichen, die zweite Zeichenkette das zugehörige Morsezeichen. Das Unicode-Zeichen wird als Schlüssel üfr den Eintrag des Morsezeichens im Dictionary genutzt.

Beim Orsen wird nicht zwischen Groß- und Kleinschreibung unterschieden. Daher wird den Dictionary-Elementen für die KLeinbuchstaben das gleiche Morsezeichen zugewiesen wie den entsprechenden Elementen für die Großbuchstaben.

Als Ergebnis der Funktion wird das Dictionary zurückgeliefert.

#### 8.9.2 Ausgabe auf dem Bildschirm

In diesem Abschnitt werden die Morsezeichen eines Beispieltexts auf dem Bildschirm ausgegeben. Die einzelnen Morsezeichen werden jeweils durch ein Leerzeichen getrennt. Es folgt das Programm:

```py
import sys, morsen

# Beispieltext codieren
def schreibeCode(text, code):
    for zeichen in text:
        try:
            print(code[zeichen], end=" ")

        except KeyError:
            print(" ", end=" ")
    print()

# Lesefunktion aufrufen

code = morsen.leseCode()

# Schreibfunktion aufrufen
schreibeCode("Hallo Welt", code)
```
```
.... .- .-.. .-.. ---   .-- . .-.. - 
```

Im Hauptprogramm wird die Funktion `leseCode()` aus dem oben beschriebenen Modul `morsen` aufgerufen. Sie liefert ein Dictionary zurück. Anschließend wird die Funktion `schreibeCode()` mit einem Beispieltext aufgerufen.

In der Funktion `schreibeCode()` wird ein übergebener Beispieltext in Morsezeichen codiert und ausgegeben. Falls es zu einem Zeichen keine Entsprechung im Dictionary gibt, tritt ein `KeyError` auf. In diesem Fall wird ein Leerzeichen ausgegeben.

#### 8.9.3 Ausgabe mit Tonsignalen

In diesem Abschnitt werden die Morsezeichen eines Beispieltexts als Tonsignale ausgegeben. Bevor Sie das nachfolgende Programm starten, sollten Sie den Lautsprecher Ihres Windows-PCs einschalten:

```py
import sys, morsen, time, winsound

# Beispieltext codieren
def tonCode(text):

    code = morsen.leseCode()
    
    # Zeitschema, Dauer eines Signals in Millisekunden
    signalDauer = {".":100, "-":300}

    # Zeitschema, Dauer einer Pause in Sekunden
    signalPause = 0.1
    zeichenPause = 0.3
    wortPause = 0.7

    # Text in Wörter zerlegen
    alleWorte = text.split()
    

    # Jedes Wort im Text
    for w in range(len(alleWorte)):
        wort = alleWorte[w]
        print()
        print(wort)
        
        
        # Jedes Zeichen im Wort
        for z in range(len(wort)):
            # Übernahme des Zeichens
            zeichen = wort[z]
            
            # Kontrollausabe des Zeichens
            print(str(zeichen) + ":", end=" ")

            # Versuch, ein Zeichen auszugeben
            try:
                # Übernahme des Morsezeichens für das Zeichen
                # Falls kein Eintrag im Dictionary: KeyError
                alleSignale = code[zeichen]
                
                # Jedes Signal des Morsezeichens
                for s in range(len(alleSignale)):
                    # Übernahme eines Symbols
                    signal = alleSignale[s]
                    print(signal, end="")
                    # Ausgabe des Symbols, kurz oder lang
                    winsound.Beep(800, signalDauer[signal])
                    # Nach jedem Singal eine Signalpause,
                    # außer nach dem letzten Signal
                    if s < len(alleSignale)-1:
                        time.sleep(signalPause)
                print()
                # Nach jedem Zeichen eine Zeichenpause,
                # außer nach dem letzten Zeichen
                if z < len(wort)-1:
                    time.sleep(zeichenPause)
            # Falls kein Eintrag im Dictionary: ignorieren 
            except KeyError:
                print("keyerror")
                pass

            # Nach jedem Wort eine Wortpause,
            # außer nach dem letzten Wort
            if w <len(alleWorte)-1:
                print("", end="")
                time.sleep(wortPause)
# Lesefunktion aufrufen

code = morsen.leseCode()

# Schreibfunktion aufrufen

tonCode("Der braune schnelle Fuchs springt ueber den faulen alten Hund und wiederholt das Spielchen hundert mal am Tag")
```

In der Funktion `tonCode()` wird ein übergebener Beispieltext in Morsezeichen codiert und als Folge von Tonsignalen ausgegeben. Dazu wird zunächst ein weiteres Dictionary angelegt. Darin wird die Signaldauer für ein kurzes Signal mit 100ms festgelegt. Ein langes Signal muss dreimal so lang sein. Daher bekommt es eine Länge von 300ms.

Nach jedem Signal folgt eine Signalpause in der Dauer eines kurzen Signals, nach jedem Zeichen in der Dauer eines langen Signals und nach jedem Wort in einer Dauer von sieben kurzen Signalen.

Der gesamte Text wird anhand der Leerzeichen in einzelne Wörter zerlegt. Jedes Wort wird in einzelne Zeichen zerlegt. Zu jedem Zeichen wird der zugehörige Eintrag im Dictionary der MOrsezeichen gesucht. Jedes gefundene Morsezeichen wird in einzelne Signale zerlegt. Jedes Signal wird mithilfe der Funktion `Beep()` aus dem Modul `winsound` als Ton ausgegeben.

Falls es zu einem Zeichen keine Entsprechung im Dictionary gibt, tritt ein `KeyError` auf. In diesem Fallwird das Zeichen ignoriert.

Die Funktion `sleep()` aus dem Modul `time` sorgt für die Pausen zwischen den Signalen, Zeichen und Wörtern.

Im Hauptprogramm wird zunächst die Funktion `leseCode()` aus dem Modul morsen aufgerufen. Sie liefert ein Dictionary zzurück. Dann wird die Funktion `tonCode()` mit einem Beispieltext aufgerufen.

**Unterschiee in Ubuntu Linux und macOS:** Das Modul `winsound` steht nicht zur Verfügung.


### 8.10 Spiel, Version mit Highscore-Datei

Es folgt eine weiter Version des bereist bekannten Kopfrechenspiels. Die Daten des Spielers (Name und Zeit) werden mithilfe der Serialisierung dauerhaft gespeichert, sodass eine Highscore-Liste geführt werden kann.

Es wird zunächst nach dem Namen des Spielers gefragt. Anschließend bekommt de Spieler fünf Additionsaufgaben mit Zahlen aus dem Bereich von 10 bis 30 gestellt. Pro Aufgabe hat er nur einen Versuch. Ungültige Eingaben oder falsche Ergebnisse werden mit dem Text `Falsch` kommentiert. Zuletzt wird die Gesamtzeit angegeben, die de rSpieler für die LÖsungsversuche benötigt hat.

Fals der Spieler alle fünf Aufgaben richtig löst, werden sein Name und die benötigte Zeit in eine Highscore-Liste aufgenommen, die in einer Datei abgespeichert wird.

#### 8.10.1
```
Bitte eingeben (0: Ende, 1: Highscores, 2: Spielen): 1
P. Name         Zeit
1. Ole          8.3s
[...]
Bitte eingeben (0: Ende, 1: Highscores, 2: Spielen): 2
Bitte geben Sie ihren Namen ein (max. 10 Zeichen): Paul
Aufgabe 1 von 5: 20 + 30 : 50
* * * Richtig * * *
[...]
Ergebnis: 5 von 5 in 9.48 Sekunden, Highscore
P. Name         Zeit
1. Ole          8.3s
[...]
Bitte eingeben (0: Ende, 1: Highscores, 2: Spielen): 0
```
Der Benutzer schaut sich zuerst die Highscores an. Dort gibt es bereits einige Einträge. Anschließend spielt er eine Runde, löst alle fünf Aufgaben richtig, in sein Name erscheint ebenfalls im Highscore. Als Letztes verlässt er das Programm.

#### 8.10.2 Aufbau des PRogramms

Das Programm enthält ein Hauptprogramm und vier Funktionen.
Im Hauptprogramm wird innerhalb einer Endlosschelife ein Hauptmenü aufgerufen. Darin kann sich der Spieler entwerde die Highscores anzeigen lassen, spielen oder das Programm beenden.

Es folgen die 4 Funktionen des Programms.
* `hs_lesen()`: Lesen der Highscores aus der Datei in eine Liste
* `hs_anzeigen()`: Anzeigen der Highscore_liste auf dem Bildschirm
* `hs_schreiben()`: Schreiben der Highscore-Liste in die Datei
* `spiel()`: Stellen der Aufgaben, Lösen der Aufgaben, Einfügen der ermittelten Zeit in die Highscore-Liste
  
#### 8.10.3 Code des Programms

Im nachfolgenden Listing sehen Sie den Beginn des Programms mit der Funktion zum Lesen der Highscore-Daten aus der Datei:

```py
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
```
Es werden die Module `random`, zur Erzeugund der Zufallszahlen, `time` zur Zeitmessung und `glob` zur Prüfung der Datei benötigt.

Nach dem Einlesen aus der Datei stehen in der Liste `hs_liste` die Namen und Ergebniszeiten der Spieler. Da die Liste in dieser Funktion erstmalig benutzt, aber im gesamten Programm benötigt wird, wird sie hier mit `global` im globalen Namensraum bekannt gemacht.

Falls die Datei nicht vorhanden ist, wird eine leere Liste erzeugt. Ist die Datei vorhandne, wird der gesamte Inhalt mithilfe der Funktion `load()` aus dem Modul `pickle` in die Liste `hs_liste` gelesen.

Es folgt die FUnktion zum Anzeigen des Highscores:

```py
# Funktion Highscore anzeigen
def hs_anzeigen():
    # Highscore nicht vorhanden
    if not hs_liste:
        print("Keine Highscores vorhanden")
        return

    # Ausgabe Highscore
    print(f"{'P':>2}. {'Name':10}{'Zeit':>5}")
    for i in range(len(hs_liste)):
        print(f"{(i+1):>2d}. {hs_liste[i][1]:10}{hs_liste[i][1]:5.2f}")
        if i >= 9:
            break
```

Falls die Highscore-Liste leer ist, wird eine entsprechende Meldung angezeigt. Ist die Liste nicht leer, werden nach einer Überschrift maximal zehn Highscores formatiert ausgegeben, und zwar mit den Informationen *Platzierung*, *Name*, *Ergebniszeit*.

Es folgt die FUnktion zum Schreiben der Highscore-LIste in die Datei:

```py
# Funktion Highscore schreiben
def hs_schreiben():
    # Zugriff
    d = open("highscore.bin", "wb")
    pickle.dump(hs_liste,d)
    d.close()
```

Die gesamte Liste wird mithilfe der Funktion `dump()` aus dem Modul `pickle` in die Datei geschrieben.

Es folgt die FUnktion zum Spielen:
```py
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
            zahl = int(input("Aufgabe " + str(aufgabe+1) + "von 5: " + str(a) + " + " + str(b) " = "))
            if zahl == c:
                print("*** Richtig ***")
                richitg += 1
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
```

Nach der Eingabe des Namens wird er zur einheitlichen Ausgabe auf maximal zehn Zeichen verkürzt. Es folgen einige Programmteile, die bereits aus früheren Versionen des Spiels bekannt sind: Stellen der fünf Aufgaben, Eingabe der Lösung, Bewertung der Lösung, Messung der Zeit. Beachten Sie, dass die Zahlenvariablen `aufgabe`, `a` und `b` für die Funktion `input()` in Zeichneketten umgewandelt werden müssen.

Falls nicht alle fünf Aufgaben richtig gelöst werden, kann kein Eintrag in die Highscore-Liste erfolgen.

Die Highscore-Liste wird Element für Element durchsucht. Wird ein Element gefunden, in dem eine größere als die neue Ergebniszeit eingetragen sit, so wird die neue Ergebniszeit mithilfe der Funktion `insert()` an dieser Stelle in die Highscore-Liste eingefügt.

Falls kein Eintrag durch Einfügen erfolgte, wird die neue ERgebniszeit mit hilfe der Funktion `append()` ans Ende der Liste angehängt. Auf diese Weise ist dafür gesorgt, dass die Highscore-Liste immer aufsteigend nach Ergebniszeit sortiert ist. Sie wird nach jeder Änderung angezeigt.

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
        menu = int(input("0: Ende \n1: Highscores \n2: Spielen\nBitte Wählen: "))
    except:
        print("Falsche Eingabe")
        continue

    # Aufruf einer FUnktion oder Ende
    if menu == 0:
        break
    if menu == 1:
        hs_anzeigen()
    if menu == 2:
        spiel()
    else:
        print("Falsche Eingabe")
    # Highscore aus Lsite in Datei schreibne
    hs_schreiben()
```

* Nach der Initialisierung des Zufallsgenerators wird die Highscore-Datei eingelesen. Es beginnt die Endlosschleife mit dem Hauptmenü. 
* Nach der Eingabe von `2` beginnt das Spiel, anschließend erscheint wieder das Hauptmenü.
* Nach der Eingabe von `0` wird die Endlosschleife verlassen. Die Highscore-Liste wird in die Datei geschrieben. Das Programm endet.

### 8.11 Spiel, objektorientierte Version mit Highscore-Datei

Es folgt eine weitere objektorientiere Version des Kopfrechenspiels. Diesmal werden die Daten des Spielers (Name und Zeit) in einer CSV-Datei gespeichert. Diese CSV-Datei können Sie sich mithilfe von MS Excel unter Windows oder mit LibreOffice Calc unter Linux und macOS ansehen.

Neben den beiden Klassen `Spiel` und `Aufgabe` benötigen Sie die KLasse `Highscore`. Die Klasse `Aufgabe` hat sich gegenüber der Version in der Datei *spiel_oop.py*  nicht verändert.

Zunächst die Importanweisung und das Hauptprogramm

```py
import random, time, glob

# Hauptprogramm
while True:
    # Hauptmenü, Auswahl
    try:
        menu = int(input("0: Ende \n1: Highscores \n2: Spielen\nBitte Wählen: "))
    except:
        print("Falsche Eingabe")
        continue

    # Anlegen eines Objekts oder Ende
    
    if menue == 0:
        break
    elif menue == 1:
        hs = Highscore()
        print(hs)
    elif menue == 2:
        s = Spiel()
        s.messen(True)
        s.spielen()
        s.messen(False)
        print(s)
    else:
        print("Falsche Eingabe")
```
Es werden die Module `random` (zur Erzeugung der Zufallszahlen), `time` (zur Zeitmessung) und  `glob` (zur Prüfung der Datei) benötigt.

Falls der Benutzer die Highscore-Liste sehen möchte, wird ein Objekt der Klasse `Highscore` erzeugt und ausgegeben. Falls er speilen möchte, wird ein Objekt der Klasse `Spiel` erzeugt. Nach der messung der Zeit und dem eigentlichen Spielvorgang werden die Ergebnisse ausgegeben.

Es folgt die KLasse `Spiel`:

```py
# Klasse "Spiel"

class Spiel:
    def __int__(self):
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie ihren Namen ein (max. 10 Zeichen):")
        self.spieler = [0:10]

    def spielen(self):
        # Spielablauf
        for i in range(1, self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()
    
    def messen(self, start):
        if start:
            self.startzeit = time.time()
        else:
            endzeit = time.time()
            self.zeit = endzeit - self.startzeit
    
    def __str__(self):
        # Ergebnis
        ausgabe = f"Richtig: {self.richtig:d} von {self.anzahl:d} in {self.zeit:.2f} Sekunden"
        if self.richtig == self.anzahl:
            ausgabe += ", Highscore"
            hs = Highscore()
            hs.speichern(self.spieler, self.zeit)
            print(hs)
        else:
            ausgabe += ", leider kein Highscore")
        return ausgabe
```

Im Konstrutkor der Klasse wird er Zufallsgenerator initialisiert. Der Zähler für die richtig gelösten Aufgaben wird auf 0, die Anzahl der Aufgaben auf 5 gesetzt. Es wird der Name des Spielers ermittelt. Dabei werden drei Eigenschaften der Klasse `Spiel` gesetzt. `richtig`, `anzahl` und `spieler`.

In der Methode `spielen()` werden insgesamt fünf Aufgaben gestellt und beantwortet. Die Methode `messen()` dient zur Zeitmessung. Es wird die Eigenscaht `zeit` der Klasse `Spiel` gesetzt.

Falls der Spieler alle Aufgaben richtig löst, wird in der Ausgabenmethode ein Objekt der Klasse `Highscore` erzeugt und gespeichert. Anschließend wird die Liste ausgegeben.

Die neue Klasse `Highscore` sieht wie folgt aus:

```py
# Klasse "Highscore"

class Highscore:
    # Liste aus Datei lesen
    def __init__(self):
        self.liste = []
        if not glob.glob("highscore.csv"):
            return
        d = open("highscore.csv")
        zeile = d.readline()
        while zeile:
            teil = zeile .split(";")
            name = teil[0]
            zeit = teil[1][0:len(teil[1])-1]
            zeit = zeit.replace(",", ".")
            self.liste.append([name, float(zeit)])
            zeile = d.readline()
        d.close()

    # Liste ändern
    def aendern(self, name, zeit):
        # Mitten in Liste schreiben
        gefunden = False
        for i in range(len(self.liste)):
            # Einsetzen in Liste
            if zeit < self.liste[i][1]:
                self.liste.insert(i, [name, zeit])
                gefunden = True
                break
        
        # Ans Ende der Liste schreiben:
        if not gefunden:
            self.liste.append([name, zeit])

    # Liste ändern, in Datei speichern
    def speichern(self, name, zeit):
        self.aendern(name, zeit)
        d = open("highscore.csv", "w")
        for element in self.liste:
            name = element[0]
            zeit = str(element[1]).replace(".", ",")
            d.write(name + ";" + zeit + "\n")
        d.close()

    # Liste Anzeigen

    def __str__(self):
        # Highscore nicht vorhanden
        if not self.liste:
            return "Keine Highscores vorhanden"1

        # Ausgabe Highscore
        ausgabe = "P. Name      Zeit\n"
        for i in range(len(self.liste)):
            ausgabe += f"{i+1:2d}. {self.liste[i][0]:10} {self.liste[i][1]:5.2f} sec\n"

            if i >= 9:
                break
        return ausgabe
```

Im Konstruktor der Klasse wird die wichtigste Eigenschaft gesetzt: die Highscore-Liste mit dem Namen `liste`. Sie ist zunächst leer. Falls keine CSV-Datei existiert, bleibt sie leer. Falls es keine SV-Datei exisiert, blebit sie leer. Falls es eine CSV-Datei gibt, werden alle Zeilen daraus gelesen. Anschließend werden die Zeilen zerlegt. Aus dem Dezimalkomma (für MS Excel oder LibreOffice Calc) wird ein Dezimalpunkt. Die beiden Bestandteile werden der Highscore-Liste als Unterliste angehängt.

Die Methode `aendern()` wird klassenintern von der Methode `speichern()` benötigt. Ein neu ermittelter Highscore wird entweder in die Liste eingefügt oder der Liste angehängt.

In der Methode `speichern()` wird zunächst die Highscore-Liste geändert. Anschließend wird aus dem Dezimalpunkt ein Dezimalkomma für MS Excel oder LibreOffice calc. Die gesamte Liste wird in der CSV-Datei gespeichert. Zudem wird sie in der Ausgabemethode veröffentlicht, falls sie nicht leer ist.


## 9 Internet

Dieses Kapitel beschäftigt sich mit dem Empfangen und Senden von Internetdaten und mit der Erstellung von Programmen, die auf einem Webserver laufen. Sie können mithilfe von Python auf Daten im Internet zugreifen, Daten ins Internet senden und Daten anderen Benutzern im Internet zur Verfügung stellen.

Zum Testen der Programme dieses Kapitels wird ein lokaler Webserver benötigt. XAMPP ist ein vorkonfiguriertes und einfach zu installierenedes Paket, das neben einem *Apache-Webserver* weitere Software umfasst, z. B. die Webserver-Sprache *PHP* und das Datenbanksystem *MySQL* bzw. seine Abspaltung *MariaDB*. Bezüglich der Beispiele in diesem Buch stellt es keinen Unterschied dar, ob die jeweilige XAMPP-Version mit MySQL oder mit MariaDB arbeitet.

Sie erreichen die Website zum Herunterladen von XAMPP über die Adresse *www.apachefriends.org*, sowohl für Windows als auch für Ubuntu Linux und für macOS. Die Installation von XAMPP wird in Abschnitt A.2 beschrieben.

Am Ende dieses Kapitels wird das bereits bekannt Kopfrechenspiel in einer Version vorgestellt, die das Spielen im Internet ermöglicht. Die Aufgaben werden aus dem Internet abgerufen, die Benutzereingaben ins Internet gesendet und die Spielerergebnisse mithifle der Serialisierung dauerhaft auf einem Webserver im Internet gespeichert.

### 9.1 Laden und Senden von Internetdaten

Das Modul `urllib` mit den Untermodulen `urllib.request` und `urllib.parse` kann zum Laden von Daten aus dem Internet und zum Senden von Daten in das Internet verwendet werden.

Bei existierender Verbindung zu einem Webserver, ob lokal oder im Internet, haben Sie folgende Möglichkeiten:
* Sie können mithilfe der Funktion `urlopen()` eine Verbindung zu einer URL öffnen und anschließend die Ihalte in eine Variable eines Python-Programms einlesen.
* Sie können mithilfe der Funktion `urlretrieve()` Daten direkt von einer URL in eine Datei auf der Festplatte kopieren.

Mitder Funktion `urlopen()` können Sie auch Daten ur weiteren Verarbeitung auf dem Webserver an eine URL senden.

#### 9.1.1 Daten Lesen

Im folgenden Programm wird der Inhalt der Internetseite *http://local-host/Python38/url_lesen.thm* mithilfe der Funktion `urlopen()` aus dem Modul `urllib.request` in eine Liste gelesen. Diese Liste wird anschließend ausgegeben.

Es folgt zunächst der INhalt der einfachen HTML-Datei `url_lesen.htm`:

```html
<!DOCTYPE html><html>
<head>
    <meta charset="utf-8">
    <title>Titelzeile</title>
</head>
<body>
    <b>Hallo Python</b>
</body>
</html>
```

Standardmäßg wird XAMPP im Verzeichnis *C:\xampp\htdocs* installiert. Die Datei *url_lesen.htm* wird im Verzeichnis *C:\xampp\htdocs\Python38* gespeichert. Alle HTML_Dateiein dieses Kapitels sollten die Kodierung UTF-8 besitzen. Falls Sie zu ihrer Erstellung den Editor Notepad++ nutzen, können Sie die Datei bei Darf über den Menüpunkt *Kodierung* konvertieren.

Es handelt sich nur um einfache HTML-Codebeispiele, da eine weitereEinführung in HTML nicht Gegenstand dieses Buchs ist.

Geben sie die Adresse *http://localhost/Python38/url_lesen.htm* in einem Webbrowser ein.

Das Python-Programm zum Lesen des HTML-Codes dieses internetseite sieht wie folgt aus:

```py
import sys, urllib.request

# Verbindung zu einer URL
try:
    u = urllib.request.urlopen("http://localhost/Python38/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

# Liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung
u.close()

# Ausgabe der Liste
for element in li:
    print(element)
```

```
b'\xef\xbb\xbf<!DOCTYPE html><html>\r\n'
b'<head>\r\n'
b'meta charset="uft-8">\r\n'
b'<title>Titelzeile</title>\r\n'
b'</head>\r\n'
b'<body>\r\n'
b'<b>Hallo Python</b>\r\n'
b'</body>\r\n'
b'</html>\r\n'
```

Erscheint eine Fehlermeldung, dann haben Sie eventuell vergessen, den lokalen Webserver zu starten (siehe im Anhang unter Abschnitt A.2, "Installation von XAMPP").

Die Verbindung zur URL wird mithilfe der FUnktion `urlopen()` geöffnet. Ihr Rückgabewert ähnelt einem Dateiobjekt. Auf die geöffnete Datei können sie lesend zugreifen, wie im Abschnitt 8.3.2, "Sequenzielles Lesen", beschrieben.

Die Funktion `readlines()` liefert eine LIste. Jedes Listenelement umfasst eine Zeile des HTML-Codes der Internetseite.

Nach dem Abspeichern der Zeilen in der Liste können Sie die Datei mit der Funktion `close()` wieder schließen.

Jedes Element der Liste ist eine Zeichenkette, die als Byte-Literal ausgegeben wird. Byte-Literale sind Zeichenketten des Datentyps `bytes`(siehe 4.2.7). Zu Beginn der ersten Zeile sehen sie einige Steuerzeichen bezüglich der UTF-8-Kodierung.

 