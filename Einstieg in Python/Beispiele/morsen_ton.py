import sys, morsen, time, winsound

# Beispieltext codieren
def tonCode(text):

    code = morsen.leseCode()
    
    # Zeitschema, Dauer eines Signals in Millisekunden
    signalDauer = {".":100, "-":300}

    # Zeitschema, Dauer einer Pause in Sekunden
    signalPause = 0.1
    zeichenPause = 0.3
    wortPause = 0.7

    # Text in Wörter zerlegen
    alleWorte = text.split()
    

    # Jedes Wort im Text
    for w in range(len(alleWorte)):
        wort = alleWorte[w]
        print()
        print(wort)
        
        
        # Jedes Zeichen im Wort
        for z in range(len(wort)):
            # Übernahme des Zeichens
            zeichen = wort[z]
            
            # Kontrollausabe des Zeichens
            print(str(zeichen) + ":", end=" ")

            # Versuch, ein Zeichen auszugeben
            try:
                # Übernahme des Morsezeichens für das Zeichen
                # Falls kein Eintrag im Dictionary: KeyError
                alleSignale = code[zeichen]
                
                # Jedes Signal des Morsezeichens
                for s in range(len(alleSignale)):
                    # Übernahme eines Symbols
                    signal = alleSignale[s]
                    print(signal, end="")
                    # Ausgabe des Symbols, kurz oder lang
                    winsound.Beep(800, signalDauer[signal])
                    # Nach jedem Singal eine Signalpause,
                    # außer nach dem letzten Signal
                    if s < len(alleSignale)-1:
                        time.sleep(signalPause)
                print()
                # Nach jedem Zeichen eine Zeichenpause,
                # außer nach dem letzten Zeichen
                if z < len(wort)-1:
                    time.sleep(zeichenPause)
            # Falls kein Eintrag im Dictionary: ignorieren 
            except KeyError:
                print("keyerror")
                pass

            # Nach jedem Wort eine Wortpause,
            # außer nach dem letzten Wort
            if w <len(alleWorte)-1:
                print("", end="")
                time.sleep(wortPause)
# Lesefunktion aufrufen

code = morsen.leseCode()

# Schreibfunktion aufrufen

tonCode("Der braune schnelle Fuchs springt ueber den faulen alten Hund und wiederholt das Spielchen hundert mal am Tag")
