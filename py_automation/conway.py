import copy
import random
import time

WIDTH = 60
HEIGHT = 20

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
    
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end = '')
        print()
    
for x in range(WIDTH):
    for y in range(HEIGHT):
        leftCoord = (x - 1) % WIDTH
        rightCoord = (x + 1) % WIDTH
        aboveCoord = (y - 1) % HEIGHT
        belowCoord = (y + 1) % HEIGHT
        