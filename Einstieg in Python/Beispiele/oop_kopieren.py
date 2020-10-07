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

# Objekt der KLasse Fahrzeug erzeugen
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
