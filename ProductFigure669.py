n = int(input())


def getSimpleDividers(x):
    if x == 1:
        print("1")
        exit()
    if x == 0:
        print("10")
        exit()
    d = [2,3,5,7,-1]
    ds = []
    while x != 1:
        for i in d:
            if i == -1:
                print(f'{-1} {-1}')
                exit()
            if x % i == 0:
                ds.append(i)
                x /= i
                break
    return ds

divs = getSimpleDividers(n)
divs.sort()
line = ''.join([str(x) for x in divs])
lineCopy = line[:]

while line.__contains__('222'):
    line = line.replace("222", "8")
while line.__contains__('33'):
    line = line.replace("33", "9")

def sortLine(s):
    d = [int(i) for i in s]
    d.sort()
    s = ''.join([str(i) for i in d])
    return s

line = sortLine(line)
while line.__contains__('23'):
    line = line.replace("23", "6")
    line = sortLine(line)

while line.__contains__('22'):
    line = line.replace("22", "4")

divs = [int(i) for i in line]
divs.sort()
line = ''.join([str(x) for x in divs])



print(f"{line} {lineCopy[::-1]}")