input()
ts = [int(num) for num in input().split(" ")]
ts.sort()
for i in ts:
    print(i, end=" ")