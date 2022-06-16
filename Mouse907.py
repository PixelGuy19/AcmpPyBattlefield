import math
n = [int(i) for i in input().split(" ")]

if n[0] >= 2*n[2] and n[1] >= 2*n[2]:
    print("YES")
else:
    print("NO")
