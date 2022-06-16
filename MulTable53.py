line = [int(i) for i in input().split(" ")]

red = 0
green = 0
blue = 0
black = 0
row = range(1, line[0] + 1)
for column in range(1, line[1] + 1):
    for j in row:
        n = j * column
        if n % 5 == 0:
            blue += 1
            continue
        if n % 3 == 0:
            green += 1
            continue
        if n % 2 == 0:
            red += 1
            continue
        black += 1

print(f'RED : {red}\nGREEN : {green}\nBLUE : {blue}\nBLACK : {black}')