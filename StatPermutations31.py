from itertools import permutations
line = input().split(" ")
arr = range(1, int(line[0])+1)
k = int(line[1])

s = 0
for i in permutations(arr):
    c = 0
    for j in range(0, len(i)):
        if j + 1 == i[j]:
            c += 1
    if c == k:
        s += 1
print(s)