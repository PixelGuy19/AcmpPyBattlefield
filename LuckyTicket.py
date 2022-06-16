t = input()
t1 = t[0:3]
t2 = t[3:6]
s1, s2 = 0, 0
for i in t1:
    s1 += int(i)
for i in t2:
    s2 += int(i)

if s1==s2:
    print("YES")
else:
    print("NO")