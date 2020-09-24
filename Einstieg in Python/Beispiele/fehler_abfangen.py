# init while
fehler = 1

# while loop bei falscher Eingabe

while fehler == 1:
    print("bitte eine ganze zahl eingeben!")
    z = input()
    try:
        zahl = int(z)
        print("success! Zahl:", zahl)
        fehler = 0
    except:
        print("wrong input")

print("programm ende")
