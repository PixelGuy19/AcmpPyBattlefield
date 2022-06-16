n = [int(i) for i in input().split(" ")]
As = n[0:3]
Bs = n[3:6]

As.sort()
Bs.sort()

cost = 0
for i in range(0, len(As)):
    cost += As[i]*Bs[i]
print(cost)