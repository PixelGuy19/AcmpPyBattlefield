#very bad solution, I'm sorry
n = [int(i) for i in input().split(" ")]

if n[0] == n[1] == n[2] == 0:
    print("0")
    exit()

f = ""
if n[0] != 0:
    f = str(n[0])

x = ""
if n[1] < 0:
    x += "-"
else:
    x += "+"
y = ""
if n[2] < 0:
    y += "-"
else:
    y += "+"
if abs(n[1]) > 1:
    x += str(abs(n[1]))
if abs(n[2]) > 1:
    y += str(abs(n[2]))

x += "x"
y += "y"

if n[1] == 0:
    x = ""
if n[2] == 0:
    y = ""
f += x + y

print(f.lstrip("+"))
