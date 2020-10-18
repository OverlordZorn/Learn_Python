import sys, shutil, os, glob

def check():
    print(glob.glob("le*.txt"))

check()

# Existenz feststellen
if not os.path.exists("lesen.txt"):
    print("Datei nicht vorhanden")
    sys.exit(0)

# Datei kopieren
shutil.copy("lesen.txt", "lesen_kopie.txt")
check()

# Datei umbennen
try:
    shutil.move("lesen_kopie.txt","lesen_neu.txt")
except:
    print("Fehler beim umbenennen")
check()

# Datei entfernen
try:
    os.remove("lesen_neu.txt")
except:
    print("Fehler beim Entfernen")

check()
