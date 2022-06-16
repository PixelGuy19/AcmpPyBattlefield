import re
def shift(list, shift):
    return list[-shift:] + list[:-shift]

a = input()
b = input()

s = 0
start = b
for i in range(0, len(b)):
    sh = shift(b, i)
    if sh == start and i > 0:
        break
    s += len(re.findall(f"(?={sh})", a))

print(s)