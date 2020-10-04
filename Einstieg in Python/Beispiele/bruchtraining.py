while 1:
    #Eingabemenü
    fehler = 1
    while fehler == 1:
        print()
        print("Ihre wahl: 1=Leicht, 2=Mittel, 3=Schwer, 0=Ende")
        try:
            wahl = int(input())
            fehler = 0
            if wahl < 0 or wahl > 3:
                fehler = 1
                print("Bitte nur 0, 1, 2 oder 3 eingeben")
        except:
            print("Bitte nur 0,1,2 oder 3 eingeben")

    if wahl == 0:
        break
    elif wahl == 1:
        leicht()
    elif wahl == 2:
        mittel()
    else:
        schwer()
