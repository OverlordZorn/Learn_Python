"""
Es soll wiederum die Stuer für verschiedene Gehälter berechnet werden.
Liegt das Gehalt über 2.500 Euro, sind 22% Steuern zu zahlen,
ansonsten 18%. Die Berechnung und die Ausgabe der Steuer
sollen diesmal innerhalb einer Funktion mit dem Namen steuer() stattfinden.
Die Funktion soll dür die folgenden Gehälter aufgerufen werden:
1.800 Euro, 2.200 Euro, 2.500 Euro, 2.900 Euro.
"""


def line():
    print("--------------------------------------------")
def steuer(Gehalt):
    if Gehalt > 2500:
        Steuersatz = 0.22
    else:
        Steuersatz = 0.18
    line()
    print("Bei einem Gehalt von", Gehalt, "Euro liegt der Steuersatz bei:", Steuersatz*100,"%.")
    print("Hierbei wird die Steuer in der Höhe von", Gehalt * Steuersatz, "Euro fällig.")
    print("Es bleiben", Gehalt - Gehalt * Steuersatz, "Euro übrig.")
    line()
    
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
 
