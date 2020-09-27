a = -1
while a != -10:
    print("Bitte ganze Zahl eingeben!")
    try:
        a = int(input())
    except:
        continue

    print("Dezimal:", a)
    print("Hexadeimal:", hex(a))
    print("Oktal:", oct(a))
    print("Dual:", bin(a))


    
b = 0x1a + 12 + 0b101 + 0o67
print("Summe:", b)
