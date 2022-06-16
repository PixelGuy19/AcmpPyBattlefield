# 129

line = input().split(" ")
x = int(line[0])
y = int(line[1])

table = [[0 for i in range(y)] for j in range(x)]
onesPoints = []
for ty in range(0 , x):
    lineT = input().split(" ")
    for tx in range(0 , len(lineT)):
        table[ty][tx] = lineT[tx]
        if lineT[tx] == "1":
            onesPoints.append([ty , tx])


def distance(x1 , y1 , x2 , y2):
    return abs(x1 - x2) + abs(y1 - y2)


def nearestOnePoint(x , y):
    if onesPoints.__contains__([x, y]):
        return 0
    dis = 101
    for i in onesPoints:
        tdis = distance(x , y , i[0] , i[1])
        if tdis < dis:
            dis = tdis
    return dis

for xt in range(0 , x):
    for yt in range(0 , y):
        print(nearestOnePoint(xt , yt), end=" ")
    print()
