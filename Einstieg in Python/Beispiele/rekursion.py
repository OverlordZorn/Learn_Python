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
