import urllib.request

# Eingabedaten

pnn = input("Bitte den Nachnamen eingeben: ")
pvn = input("Bitte den Vornamen eingeben: ")

# sendet Daten
u = urllib.request.urlopen("http://192.168.64.2/Python38/senden_get.php?nn=" + pnn + "&vn=" + pvn)

# Empfang de Antwort und Ausgabe

li = u.readlines()
u.close()
for element in li:
    print(element)