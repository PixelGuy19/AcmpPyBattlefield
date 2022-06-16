n = int(input())

k = pow(3, n / 3)
if n % 3 == 1:
    k = k * 4 / 3
if n % 3 == 2:
    k = k * 2

print(k)
