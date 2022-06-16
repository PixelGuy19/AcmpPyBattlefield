n=0
s=int(input())
for i in range(1, s+1):
    if s % i == 0:
        n += i

print(n)
