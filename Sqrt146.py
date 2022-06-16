from decimal import *
s = input()
n = Decimal(s)
getcontext().prec = (len(s) + 1)
q = int(n.sqrt().quantize(Decimal('1.'), rounding=ROUND_HALF_EVEN))
if q*q>n:
    q-=1
print(q)