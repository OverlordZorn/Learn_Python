"""
Schreiben Sie ein Programm zur Eingabe und Umrechnung von beliebigen Inch_werten in Zentimeter.
Speichern Sie das Programm in der Datei u_eingabe_inch.py.
Rufen Sie das Programm auf, und testen Sie es.
"""

# Aufforderung
print("Bitte geen Sie einen Wert ein, den Sie von Inch in Zentimeter umrechnen wollen!")
x = input()

# Umrechnung
i = float(x)
c = i * 2.54

# Ausgabe
print("Ihre Eingabe von", i, "Inch sind umgerechnet", c, "cm.")

