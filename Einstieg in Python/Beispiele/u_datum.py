"""
Entwickeln Sie ein Program zu Prüfung einer Datumsangabe.
Der Benutzer soll die drei Bestandteile eines Datums einzeln eingeben.
Anschließend wird ermittelt, ob es sich um ein falsches oder ein richtiges Datum handelt.
Gehen Sie bei der Entwicklung wie nachfolgend beschrieben vor.
Testen Sie ihr Programm nach jedem Schritt.
"""

print("Tag des Datums eingeben:")
day = int(input())

print("Monat des Datums eingeben:")
month = int(input())

print("Jahr des Datums eingeben:")
year = int(input())

"""
Untersuchen Sie den eingegebenen Wert für das Jahr. Geben Sie aus, ob es sich um ein Schaltjahr handelt.
Die vereinfachte Regel für ein Schaltjahr lautet:
Falls sich der Wert ohne Rest durch 4 teilen lässt, handelt es sich um ein Schaltjahr.
"""
schaltjahr = 0
falsch = 0
if year % 4 == 0 and not year % 100:
    schaltjahr = 1

if year % 400 == 0:
    schaltjahr = 1

if schaltjahr == 1:
    print("Das Jahr", year, "ist ein Schaltjahr")


"""
Untersuchen Sie den eingegebenen Wert für den Tag.
Falls er kleiner 1 oder größer als 31, falsches Datum.
"""

if day < 1 or day > 31:
    falsch = 1

"""
Untersuchen Sie den eingegeben Wert für den Monat.
Falls er kleiner als 1 oder größer als 12, falsches Datum.
"""

if month < 1 or month > 12:
    falsch = 1
"""
Geben sie den Wert aus, den der letzte Tag des betreffenden Monats hat.
Denken Sie daran, dass es nur drei mögliche Fälle gibt: 28, 30 oder 31 Tage.
Die Regel für Schaltjahre werden noch nicht beachtet.
"""

if month == 2:
    if schaltjahr == 1:
        daysInMonth = 29
    else:
        daysInMonth = 28

elif month == 4 or month == 6 or month == 9 or month == 11:
    daysInMonth = 30
else:
    daysInMonth = 31

print("Tage im Monat:", daysInMonth)

"""
Untersuchen Sie den eingebenen Wert für den Tag.
Geben Sie aus, ob er kleiner als 1 oder
größer als der letzte Tag des betreffenden Monats ist.
"""

if day < 1 or day > daysInMonth:
    falsch = 1

"""
Kombinieren Sie die bisherigen Schritte miteinander.
Falls der Wert für den Tag kleiner als 1 oder größer als der letzte Tag des betreffendes Monats ist
(mit Berücksichtigung der Regel für ein Schaltjahr),
handelt es sich um ein falsches Datum, ansonsten um ein richtiges Datum.
"""

# Siehe Oben

"""
Erweitern Sie das Programm. Die vollständige Regel für ein Schaltjahr lautet:
Falls sich der Wert ohne Rest durch 4 teilen lässt,
aber nicht ohne Rest durch 100 teilen lässt, handelt es sich um ein Schaltjahr.
Es handelt sich aber auch nur um ein Schaltjahr, falls sich der Wert ohne Rest durch 400 teilen lässt.
"""

# Siehe Oben

if falsch == 1:
    print("Falsches Datum")
else:
    print("Richtiges Datum")
