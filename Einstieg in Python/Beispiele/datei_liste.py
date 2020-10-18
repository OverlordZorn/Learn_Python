import glob

# Liste der Dateien
dateiliste = glob.glob("schr*.py")
print(dateiliste)

# Jedes Element der Liste durchsuchen
for datei in dateiliste:
    # Zugriffsversuch
    try:
        d = open(datei)
    except:
        print("Dateizugriff nicht erfolgreich")
        continue

    gesamtertext = d.read()

    # Zugriff beenden
    d.close()

    # Suchtext suchen
    if gesamtertext.find("obst") != -1:
        print(datei)
