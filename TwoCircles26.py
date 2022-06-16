import math

n1 = [int(i) for i in input().split(" ")]
n2 = [int(i) for i in input().split(" ")]

dis = math.sqrt((n2[0]-n1[0])*(n2[0]-n1[0])+(n2[1]-n1[1])*(n2[1]-n1[1]))
if n1[2] + n2[2] >= dis and dis + n2[2] >= n1[2] and dis + n1[2] >= n2[2]:
    print("YES")
else:
    print("NO")