import winsound, time

# Folge von Tönen mit unterschiedlicher Frequenz
for i in range (600, 1500, 200):
    print(i)
    ts = round(time.time(),5)
    print(ts)
    winsound.Beep(i, 1000)
    te = round(time.time(),5)
    print(te)
    time.sleep(0.2)

# Beispiel für Systemton
print("SystemQuestion")
winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

# Beispiel für WAV-Datei
print("GAkkord.wav")
winsound.PlaySound("GAkkord.wav", winsound.SND_FILENAME)

