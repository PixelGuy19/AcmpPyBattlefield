line,x = input(),int(input())
line = line.replace("^", "**") #.replace("x", x)
print(eval(line, {'x' : x}))