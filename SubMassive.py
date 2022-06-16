input()
n = [int(i) for i in input().split(" ")]
l = int(input())
for i in range(0, l):
    line = [(int(i)) for i in input().split(" ")]
    print(str.join(" ", [str(i) for i in n[line[0]-1:line[1]]]))