"""
Schreiben Sie das Programm aus der Übung u_range_inch so um,
dass eine Ausgabe wie in Abbild 5.3 erzeugt wird.
Die Beträge für die Spalten Inch und cm sollen jeweils
mit einer Nachkommastelle angezeigt und rechtsbündig ausgerichtet werden.
"""


print(f"{'Inch':>6}{'cm':>8}")
for i in range(15, 45, 5):
    print(f"{i:6.1f}{i*2.54:8.1f}")
