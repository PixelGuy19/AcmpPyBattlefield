n=[int(i) for i in input().split(" ")]
dis = abs(n[2] - n[1])
if dis > n[0] / 2:
    dis = n[0] - abs(n[2] - n[1])
print(dis-1)