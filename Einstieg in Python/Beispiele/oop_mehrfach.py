# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez="(leer)", ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    def __str__(self):
        return self.bezeichnung + " " + str(self.geschwindigkeit) + " km/h"

# Definition der Klasse PKW
class PKW(Fahrzeug):
    def __init__(self, bez="(leer)", ge=0, ins=0):
        Fahrzeug.__init__(self,bez,ge)
        self.insassen = ins
    def __str__(self):
        return Fahrzeug.__str__(self) + " " + str(self.insassen) + " Insassen"
    def einsteigen(self, anzahl):
        self.insassen += anzahl
    def aussteigen(self, anzahl):
        self.insassen -= anzahl


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


# Test
print("Test LKW")
mercedes = LKW("Mercedes Actros", 80, 20)
print(mercedes)
mercedes.beladen(10)
print(mercedes)
mercedes.entladen(30)
print(mercedes)
print()

# Definition der Klasse Lieferwagen
class Lieferwagen(PKW, LKW):
    def __init__(self, bez="(leer)", ge=0, la=0, ins=0):
        PKW.__init__(self, bez, ge, ins)
        LKW.__init__(self, bez, ge, la)
    def __str__(self):
        return PKW.__str__(self) + "\n" + LKW.__str__(self)

# test
print("Test Lieferwagen")
sprinter = Lieferwagen("Mercedes Sprinter", 140, 5, 5)
print(sprinter)
sprinter.aussteigen(3)
sprinter.beschleunigen(-80)
print()
sprinter.entladen(2)
print(sprinter)
print()

# Hauptprogramm
# Objekt der abgeleiteten Klasse Leiferwagen erzeugen
toyota = Lieferwagen("Toyota Allround")
toyota.einsteigen(2)
toyota.beladen(3.5)
toyota.beschleunigen(30)
print(toyota)
