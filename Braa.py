def checkLine(line): #899
    while True:
        if len(line) == 0:
            return True
        if len(line) % 2 == 1:
            return False
        line = line.strip('()')
        line = line.strip('[]')
        line = line.strip('{}')


out = []

while True:
    line = input()
    if line == "":
        break
    if checkLine(line):
        out.append('0')
    else:
        out.append('1')

print(str.join('' , out))
