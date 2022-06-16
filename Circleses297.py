s = 0
for i in input():
    if i == "0":
        s += 1
    if i == "9":
        s += 1
    if i == "8":
        s += 2
    if i == "6":
        s += 1

print(s)
