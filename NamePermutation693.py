w = input().lower().split(" ")
l1, l2 = list(w[0]), list(w[1])
l1.sort()
l2.sort()
if len(l1) != len(l2):
    print("No")
    exit()

for i in range(0, len(l1)):
    if l1[i] != l2[i]:
        print("No")
        exit()
print("Yes")