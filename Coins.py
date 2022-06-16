count = int(input())
coins = []
for i in range(0, count):
    coins.append(int(input()))

r = 0
for i in coins:
    if i == 1:
        r += 1
half = len(coins) / 2
if r > half:
    print(len(coins)-r)
else:
    print(r)
