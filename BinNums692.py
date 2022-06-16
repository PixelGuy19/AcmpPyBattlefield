import math
line = int(input())
if line <= 0:
    print("NO")
    exit()
log = math.log(line, 2)
if int(log) == log:
    print("YES")
else:
    print("NO")