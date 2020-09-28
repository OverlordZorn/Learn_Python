# Operator + und *
t1 = "Teil 1"
t2 = "Teil 2"
tgesamt = t1 + ", " + t2

t3 = "-ooo-"
t4 = "***"
tline = t4 + 3*t3 + t4

print(tgesamt)
print(tline)

# Operator in
tname = "Robinson Crusoe"
print("text:", tname)

if "b" in tname:
    print("b: ist enthalten")

if "p" not in tname:
    print("p ist nicht enthalten")

