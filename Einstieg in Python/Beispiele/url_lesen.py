import sys, urllib.request

try:
    u = urllib.request.urlopen("http://192.168.64.2/Python38/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

# liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung

u.close()

# Ausgabe der Liste
for element in li:
    print(element)

