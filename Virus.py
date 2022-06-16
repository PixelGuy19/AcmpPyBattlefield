import numpy as np # 951

size = input().split(" ")
fieldSize = np.ndarray(shape=(int(size[0]) , int(size[1])) , dtype=bool)
fieldSize.fill(False)

def setPoint(x , y):
    try:
        if y < 0 or x < 0:
            return
        fieldSize[x][y] = True
    except:
        return

virus = input().split(" ")
virus = virus[1:]
for i in range(0 , len(virus) , 2):
    setPoint(int(virus[i])-1 , int(virus[i + 1])-1)


def checkField():
    for i in fieldSize:
        for i2 in i:
            if not i2:
                return False
    return True


def timeStep():
    fieldCopy = fieldSize.copy()
    for x in range(0 , fieldCopy.shape[0]):
        for y in range(0 , fieldCopy.shape[1]):
            if (fieldCopy[x][y]):
                setPoint(x + 1 , y)
                setPoint(x - 1 , y)
                setPoint(x , y + 1)
                setPoint(x , y - 1)


time = 0
while not checkField():
    timeStep()
    time += 1
print(time)
