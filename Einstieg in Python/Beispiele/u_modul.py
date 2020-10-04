"""
Schreiben Sie das Programm aus der Übung u_rueckgabewert um:
Die Funktion Steuer() soll in die Datei u_modul_finanz.py ausgelagert werden.
Das Hauptprogramm in Datei u_modul.py soll die Funktion aus dieser Datei
importieren und nutzen.
"""

# Import des u_modul_finanz Moduls
import u_modul_finanz as tax

tax.calc(1800)
tax.calc(2200)
tax.calc(2500)
tax.calc(2900)
