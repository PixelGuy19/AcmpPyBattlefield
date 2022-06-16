dist = int(input()) #38
hs = [int(num) for num in input().split(" ")]


def scoreJump(start):
    return abs(hs[start + 1] - hs[start])


def scoreSuperJump(start):
    return 3 * abs(hs[start + 2] - hs[start])


pos = 0
energy = 0
while True:
    if dist - pos == 2:
        energy += scoreJump(pos)
        pos += 1
    if dist - pos == 1:
        break

    small = scoreJump(pos) + scoreJump(pos + 1)
    big = scoreSuperJump(pos)

    if small < big:
        energy += small
    else:
        energy += big
    pos += 2

print(energy)