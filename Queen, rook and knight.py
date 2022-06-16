#19
xPositions = {
    "A": 0 ,
    "B": 1 ,
    "C": 2 ,
    "D": 3 ,
    "E": 4 ,
    "F": 5 ,
    "G": 6 ,
    "H": 7 ,
}


def positionOnBoard(point):
    if 8 > point[0] >= 0:
        if 8 > point[1] >= 0:
            return point

    return


def getPosition(point):
    return [xPositions.get(point[0]) , int(point[1])]


def getKnightPositions(point):
    possibles = [[point[0] - 1 , point[1] + 2] ,
                 [point[0] - 1 , point[1] - 2] ,
                 [point[0] + 1 , point[1] + 2] ,
                 [point[0] + 2 , point[1] + 1] ,
                 [point[0] + 2 , point[1] - 1] ,
                 [point[0] + 1 , point[1] - 2] ,
                 [point[0] - 2 , point[1] + 1] ,
                 [point[0] - 2 , point[1] - 1]]
    return possibles


def getRookPositions(point):
    possibles = []
    for x in range(0 , 8):
        possibles.append([x , point[1]])
    for y in range(0 , 8):
        possibles.append([point[0] , y])
    return possibles

#?
def getQueenPositions(point):
    possibles = getRookPositions(point)
    for x in range(0, 8):
        for y in range(0, 8):
            if x != y:
                continue
            possibles.append([x,y])
            possibles.append([8-x, y])
    return possibles

line = input().split(" ")

positions = []
#for i in getQueenPositions(getPosition(line[0])):
#    positions.append(i)
#for i in getRookPositions(getPosition(line[1])):
#    positions.append(i)
for i in getKnightPositions(getPosition(line[2])):
    positions.append(i)

for i in range(0,3):
    break
    if(positions.__contains__(getPosition(line[i]))):
        positions.remove(getPosition(line[i]))

positions = [i for n, i in enumerate(positions) if i not in positions[:n]]
positions.sort()

print(len(positions))
print(positions)
