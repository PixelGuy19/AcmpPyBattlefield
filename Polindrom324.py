s = input()
sr = s[2:4][::-1]
if s[0:2] == sr:
    print("YES")
else:
    print("NO")