# Kopie einer Zahl
print("Zahl:")
x = 12.5
y = x
print("Dasselbe Objekt:", x is y)
y = 15.8
print("Dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Kopie eines Strings
print("String:")
x = "Robinson"
y = x
print("dasselbe Objekt:", x is y)
y = "Freitag"
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Zweite Refernz auf eine Liste
print("Liste:")
x = [23, "hallo", -7.5]
y = x
print("dasselbe Objekt:", x is y)
y[1] = "welt"
print("dasselbe objekt:", x is y)
print("gleicher Inhalt:", x == y)
