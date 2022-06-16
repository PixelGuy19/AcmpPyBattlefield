n = [int(i) for i in input().split(" ")]
N = n[0]
M = n[1]
K = n[2]
if K <= 2:
    print(0)
    exit()

bus = 0
while N + M >= K:
    M -= 2
    N -= K - 2
    bus += 1
if N > 0 and M < 2:
    print(0)
    exit()

print(bus)
