import re
line = input()
a = len(re.findall(r'(?=<--<<)', line))
a += len(re.findall(r'(?=>>-->)', line))

print(a)