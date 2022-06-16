c = input()
f = []
e = 101
f.append(e)
for i in c:
    if i == "1":
        e += 1
    else:
        e -= 1
    f.append(e)
print(max(f)-min(f)+1)
