input()
n=[int(i) for i in input().split(" ")]
combos = []
combo = []
for i in n:
    if i > 0:
        combo.append(i)
    else:
        combos.append(combo[:])
        combo.clear()

if len(combo) != 0:
    combos.append(combo[:])
    combo.clear()
combos = [len(i) for i in combos]

print(max(combos))