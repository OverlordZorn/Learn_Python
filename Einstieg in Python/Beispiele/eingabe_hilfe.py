# Berechnung einer Summe
summe = 0
for i in range (1,4):
    fehler = True
    while fehler:
        zahl = input(str(i) + ". Zahl eingeben: ")
        try:
            summe += float(zahl)
            fehler= False
        except:
            print("Das war keien Zahl")
            fehler = True
print("Summe:", summe)
print()

# Geografiespiel

hauptstadt = {"Italien":"Rom", "Spanien":"Madrid", "Portugal":"Lissabon"}
hs = hauptstadt.items()

print(hauptstadt)
print(hs)

for land, stadt in hs:
    print(land)
    print(stadt)

for x in hauptstadt:
    print(x)
    print(hauptstadt[x])
    
