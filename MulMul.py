n = int(input()) # 75
start = ["1"]
for i in range(1,n):
    start.append("0")
start = int(str.join('', start))
end = []
for i in range(0,n):
    end.append("9")
end = int(str.join('', end))

sum = 0
for i in range(start, end+1):
    num = str(i)
    mul = 1
    for j in num:
        mul *= int(j)
    sum += mul
print(sum)