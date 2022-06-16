from decimal import *
a = Decimal(input())
b = Decimal(input())

if a < b:
    print("<")
elif a > b:
    print(">")
else:
    print("=")