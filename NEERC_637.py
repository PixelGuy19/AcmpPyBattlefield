input()
n = [int(i) for i in input().split(" ")]
k = int(input())

t = 0
for i in range(0, k):
    for j in range(0, len(n)):
        if sum(n) == 0:
            break
        if n[j] > 0:
            n[j] -= 1
            t += 1

    if sum(n) == 0:
        break

print(t)