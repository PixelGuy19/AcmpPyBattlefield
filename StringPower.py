import re
s = input()
p = int(input())

o = ""
if p > 0:
    for i in range(0, p):
        o += s
        if len(o) > 1023:
            break
else:
    item = s[0: int(len(s) / abs(p))]
    if len(re.findall(item, s)) != abs(p) or abs(p) > len(s):
        print("NO SOLUTION")
        exit()
    o = s[0: len(s) - (abs(p)-1) * len(item)]

if len(o) > 1023:
    o = o[:1023]
print(o)