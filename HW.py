l = int(input())
ns = input().split(" ")
ns = [int(num) for num in ns]

s1 = 0
for i in ns:
    n = i
    if n >= 0:
        s1 += n

maxIndex = ns.index(max(ns))
minIndex = ns.index(min(ns))
sub = ns[minIndex+1:maxIndex]
if len(sub) == 0:
    sub = ns[maxIndex+1:minIndex]

s2 = 1
for i in sub:
    s2 *= i

print(str(s1) + " " + str(s2))
