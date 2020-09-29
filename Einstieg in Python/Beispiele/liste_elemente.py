# Originalliste

fr = ["Paris", "lyon", "Marseille", "Bordeaux"]
print("Original:")
print(fr)

# Ersetzen eines Elements durch ein Element
fr[2] = "Lens"
print("Element ersetzt:")
print(fr)

# Ersetzen eines Teilbereiches durch eine Liste
fr[1:3] = ["Nancy", "Metz", "Gap"]
print("Teil ersetzt:")
print(fr)

# Entnehmen eines Teilbereiches
del fr[3:]
print("Teil entnommen:")
print(fr)

# Ersetzen eines Elements durch eine Liste
fr[0] = ["Paris-Nord", "Paris-Sud"]
print("Element durch Liste ersetzt:")
print(fr)


# Originalliste
fr = ["Paris", "Lyon", "Marseille"]
print("Original:")
print(fr)

# Einsetzen eines Elements
fr.insert(0, "Nantes")
print("Nach Einsetzen:")
print(fr)

# Sortieren der Elemente
fr.sort()
print("Nach Sortierung der Elemente")
print(fr)

# Umdrehen der Liste
fr.reverse()
print("Nach Umdrehen:")
print(fr)

# Entfernen eines Elements
fr.remove("Nantes")
print("Nach Entfernen:")
print(fr)

# Ein Element am Ende hinzufügen
fr.append("Paris")
print("Ein Element hinzu:")
print(fr)

# Anzahl bestimmter Elemente
print("Anzahl Elemente Paris:", fr.count("Paris"))

# Suchen bestimmter Elemente
print("Erste Position Paris:", fr.index("Paris"))
