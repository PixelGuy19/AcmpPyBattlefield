input()
days = input().split(" ")

g1 = 0
g2 = 0
for i in days:
    if int(i) % 2 == 1:
        print(i, end=" ")
        g1 += 1

print()

for i in days:
    if int(i) % 2 == 0:
        print(i, end=" ")
        g2 += 1

print()

if g1 <= g2:
    print("YES")
else:
    print("NO")