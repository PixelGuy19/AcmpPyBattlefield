input()
n=[int(i) for i in input().split(" ")]
crashIndex = -1
for i in range(0, len(n)):
    if n[i] <= 437:
        print("Crash " + str(i + 1))
        exit(0)

print("No crash")