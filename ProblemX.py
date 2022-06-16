line = input()

s = []
# 1
if line[0] == "x":
    s.append("x")
else:
    s.append(int(line[0]))
# 2
if line[2] == "x":
    s.append(line[1] + "x")
else:
    s.append(int(line[1:3]))
if line[4] == "x":
    s.append("x")
else:
    s.append(int(line[4]))

x = 0
if s[2] == "x":
    x = s[0] + s[1]
if s[1] == "+x":
    x = s[2] - s[0]
if s[1] == "-x":
    x = -(s[2] - s[0])
if s[0] == "x":
    x = s[2] - s[1]

print(x)