f = input().split(" ")
a = int(f[0])
b = int(f[1])
c = int(f[2])
d = int(f[3])


for i in range(-100,101):
    if a*pow(i, 3) + b*pow(i,2) + c * i + d == 0:
        print(i)