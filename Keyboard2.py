input()
keysTime = [int(num) for num in input().split(" ")]
input()
breaking = [int(num) for num in input().split(" ")]
for i in breaking:
    keysTime[i-1] -= 1
for i in keysTime:
    if i < 0:
        print("yes")
    else:
        print("no")