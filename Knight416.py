xPositions = {
    "a": 0 ,
    "b": 1 ,
    "c": 2 ,
    "d": 3 ,
    "e": 4 ,
    "f": 5 ,
    "g": 6 ,
    "h": 7 ,
}
xLetters = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h"]


def getPosition(point):
    return [xPositions.get(point[0]) , int(point[1])-1]


def positionOnBoard(point):
    if 8 > point[0] >= 0:
        if 8 > point[1] >= 0:
            return True

    return False


def getPossiblePositions(point):
    possibles = [[point[0] - 1 , point[1] + 2] ,
                 [point[0] - 1 , point[1] - 2] ,
                 [point[0] + 1 , point[1] + 2] ,
                 [point[0] + 2 , point[1] + 1] ,
                 [point[0] + 2 , point[1] - 1] ,
                 [point[0] + 1 , point[1] - 2] ,
                 [point[0] - 2 , point[1] + 1] ,
                 [point[0] - 2 , point[1] - 1]]

    return possibles

pos = getPosition(input())
cells = []
for i in getPossiblePositions(pos):
    if positionOnBoard(i):
        cells.append(xLetters[i[0]] + str(i[1]+1))
cells.sort()
print(str.join("\n", cells))
