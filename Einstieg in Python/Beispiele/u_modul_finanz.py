def calc(Gehalt):
    Ausgabe(Gehalt, steuersatz(Gehalt))

def line():
    print("--------------------------------------------")
    
def steuersatz(Gehalt):
    if Gehalt > 2500:
        Steuersatz = 0.22
    else:
        Steuersatz = 0.18

    return Steuersatz

def Ausgabe(Gehalt, Steuersatz):
    print("Bei einem Gehalt von", Gehalt, "Euro liegt der Steuersatz bei:", Steuersatz*100,"%.")
    print("Hierbei wird die Steuer in der Höhe von", Gehalt * Steuersatz, "Euro fällig.")
    print("Es bleiben", Gehalt - Gehalt * Steuersatz, "Euro übrig.")
    line()
