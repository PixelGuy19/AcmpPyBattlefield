n=[int(i) for i in input().split(" ")]

even, neven = [], []
for i in range(0, len(n)):
    if i % 2 == 0:
        even.append(n[i])
    else:
        neven.append(n[i])

print(max(neven) + min(even))