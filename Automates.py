k = int(input())
for i in range(0, k):
    line = input().split(" ")
    n = int(line[0])
    m = int(line[1])
    d = 19 * m + (n + 239)*(n + 366) / 2
    print(int(d))
