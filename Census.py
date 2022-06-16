l = int(input())

maxmanindex = -1
maxmanvalue = 0
for i in range(0, l):
    line = input().split()
    if line[1] == "1":
        val = int(line[0])
        if val > maxmanvalue:
            maxmanindex = i
            maxmanvalue = val

if maxmanindex == -1:
    print(-1)
else:
    print(maxmanindex+1)