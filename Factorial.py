#51
field = input().split(" ")
n = int(field[0])
f = len(field[1]) # factorial count
if f > n:
        print(n)
        exit(0)

d = n % f == 0 # is dividable

def dTrue(n,f):
        mod = n % f
        out = 1
        if n < f:
                return n
        for i in range(n, mod, -f):
                out *= i
        return out


def dFalse(n,f):
        out = 1
        for i in range(n, f-2, -f):
                out *= i
        return out


if d:
        print(dTrue(n, f))
else:
        print(dFalse(n, f))