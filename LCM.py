def lcm(a , b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

line = input().split(" ")
a = int(line[0])
b = int(line[1])
print(lcm(a,b))