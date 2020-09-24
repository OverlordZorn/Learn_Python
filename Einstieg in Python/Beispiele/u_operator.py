"""
Schreiben Sie ein Programm zur vereinfachten Berechnung der Steuer.
Der Anwender wird dazu aufgefordert, sein monatliches Gehalt einzugeben.
Anschließend werden 18% dieses Betrags berechnet und ausgegeben.
"""

"""
Das vereinfachte Programm zu Berechnung der Steuer wird verändert.
Der Anwender solld azu aufgeforder werden, sein monatliches Gehalt einzugeben.
Liegt es über 2.500 Euro, sind 22% Steuern zu zahlen, anosnsten 18%.
Nutzen Sie die Datei u_verzweigung_einfach.py.
"""
"""
Das Programm zu Berechnugn der Steuer soll weiter verändert werden.
Der Anwender soll sein monatliches Gehalt eingeben.
4000 > Gehalt ? => 26%
"""
"""
Das Programm zu Berechnung der Steuer soll wiederum verändert werden.
Der Steuersatz soll sich entsprechend des Familienstandes anpassen.
"""

# Aufforderung
print("Geben Sie Ihr Gehalt in Euro ein:")
x = input()
print("Geben Sie ihren Familienstand ein (ledig oder verheiratet)")
y = input()
# Berechnung
income = float(x)

if income > 4000 and y == "ledig":
    tax = 0.26
elif income <= 4000 and y == "verheiratet":
    tax = 0.18
else:
    tax = 0.22

taxes = income * tax
print("Es ergibt sich eine Steuer von", taxes, "Euro bei einem Steuersatz von", (tax*100),"%")
rest = income - taxes
print("Es bleiben", rest, "Euro übrig")
