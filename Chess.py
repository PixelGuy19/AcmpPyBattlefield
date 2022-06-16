import re

c = input()

# error check
check = re.match(r'[A-H][1-8]-[A-H][1-8]' , c)
if check is None:
    print("ERROR")
    exit()

xPositions = {
    "A": 1 ,
    "B": 2 ,
    "C": 3 ,
    "D": 4 ,
    "E": 5 ,
    "F": 6 ,
    "G": 7 ,
    "H": 8 ,
}


def getPosition(point):
    return [xPositions.get(point[0]) , int(point[1])]


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


fromPos = getPosition(c.split('-')[0])
toPos = getPosition(c.split('-')[1])
if getPossiblePositions(fromPos).__contains__(toPos):
    print("YES")
else:
    print("NO")
