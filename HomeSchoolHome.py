home = input() == "Home"
x = int(input())
if not home:
    x -= 1
if x % 2 == 1:
    print("YES")
else:
    print("NO")
