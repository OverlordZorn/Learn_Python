"""
Schreiben Sie ein Programm zur vereinfachten Berechnung der Steuer.
Der Anwender wird dazu aufgefordert, sein monatliches Gehalt einzugeben.
Anschließend werden 18% dieses Betrags berechnet und ausgegeben.
"""

# Aufforderung
print("Geben Sie Ihr gehalt in Euro ein:")
x = input()

# Berechnung
income = float(x)


taxes = income * 0.18
print("Es ergibt sich eine Steuer von", tax, "Euro")
rest = income - taxes
print("Es bleiben", rest, "Euro übrig")
