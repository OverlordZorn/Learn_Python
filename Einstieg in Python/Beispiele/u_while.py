"""
Schreiben Sie ein Programm, das den Anwender wiederholt dazu auffordert,
einen Wert in Inch einzugeben. Der eingegebene Wert soll anschließend
in Zentimeter umgerechnet wund ausgegeben werden.
Das Programm soll nach der Eingabe des Werts 0 beendet werden.

Bei einer while-Schleife wird immer angegeben,
gemäß welcher Bedingung wiederholt werden soll, und nicht,
gemäß welcher Bedingung beendet werden soll.
Daher müssen Sie in diesem Programm formulieren:
Solange die Eingabe ungleich 0 ist.
"""

inch = 1

while inch != 0:
    print("Zum Umrechnen in CM bitte einen Wert in Inch eingeben:")
    inch = float(input())

    print(inch, "Inch sind", inch * 2.54, "cm.")
print("Die Umrechnung wurde beendet")

