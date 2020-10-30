import sys, urllib.request

# Verbindung zu einer URL
try:
    u = urllib.request.urlopen("http://localhost/Python38/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

# Liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung