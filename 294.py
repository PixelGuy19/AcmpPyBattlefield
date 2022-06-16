n = [int(num) for num in input().split(" ")]
n2 = [int(num) for num in input().split(" ")]
cost = 0

nlost = n[0] * n[1] / 100
n2lost = n2[0] * n2[1] / 100
unuse = abs((n[0] - nlost)-(n2[0] - n2lost))

cost += nlost * n[2]
cost += n2lost * n2[2]

if (n[0] - nlost) > (n2[0] - n2lost):
    cost += unuse * n[2]
if (n[0] - nlost) < (n2[0] - n2lost):
    cost += unuse * n2[2]

print(int(cost))