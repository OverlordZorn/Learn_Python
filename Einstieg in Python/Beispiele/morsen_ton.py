import sys, morsen, time, winsound

# Beispieltext codieren
def tonCode(text, code):
    # Zeitschema, Dauer eines Signals in Millisekunden
    signalDauer = {".":200, "-":600}

    # Zeitschema, Dauer einer Pause in Sekunden
    singalPause = 0.2
    zeichenPause = 0.6
    wortPause = 1.4

    # Text in Wörter zerlegen
    alleWorte = text.split()

    # Jedes Wort im Text
    for w in range(len(alleWorte)):
        wort =alleWorte[w]

    
    # Jedes Zeichen im Wort
    for z in range(len(wort)):
        
        # Übernahme des Zeichens
        zeichen = wort[z]

        # Kontrollausabe des Zeichens
        print(zeichen, end="")

        # Versuch, ein Zeichen auszugeben
        try:
            # Übernahme des Morsezeichens für das Zeichen
            # Falls kein Eintrag im Dictionary: KeyError
            alleSignale = code[zeichen]
            # Jedes Signal des Morsezeichens
            for s in range(len(alleSignale)):
                # Übernahme eines Symbols
                signal = alleSignale[s]
                # Ausgabe des Symbols, kurz oder lang
                winsound.Beep(800, singalDauer[signal])
                

        except KeyError:
            pass