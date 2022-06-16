input() #293

n = [int(num) for num in input().split(" ")]
p = [int(num) for num in input().split(" ")]
taxed = []
for i in range(0, len(n)):
    taxed.append(n[i] * p[i] / 100)

print(taxed.index(max(taxed))+1)
