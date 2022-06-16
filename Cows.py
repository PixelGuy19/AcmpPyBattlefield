line = input().split(" ")
q = line[0]
a = line[1]

cows = 0
bulls = 0
for i in range(0, len(q)):
    if q[i] == a[i]:
        bulls += 1
    else:
        if q.__contains__(a[i]):
            cows += 1

print(str(bulls) + " " + str(cows))
