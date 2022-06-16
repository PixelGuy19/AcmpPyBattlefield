import re
gl = int(input())
gods = []
for i in range(0, gl):
    gods.append(input())
wl = int(input())
words = []
for i in range(0, wl):
    words.append(input())

for i in gods:
    c = 0
    for j in range(0, len(i)):
        same = False
        for i2 in words:
            if i == i2:
                same = True
        if same:
            continue

        s = i[:]
        s = s[:j] + "." + s[j + 1:]
        for i2 in words:
            c += len(re.findall(s, i2))
    print(c, end=" ")
