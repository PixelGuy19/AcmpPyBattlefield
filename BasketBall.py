n1 = 0
n2 = 0
for i in range(1, 5):
    text = input().split(" ")
    n1 += int(text[0])
    n2 += int(text[1])
if n1 > n2:
    print(1)
if n1 < n2:
    print(2)
if n1 == n2:
    print("DRAW")