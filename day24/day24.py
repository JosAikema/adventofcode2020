def parseTile(t):
    instructions = []
    idx = 0
    while idx <= len(t)-1:
        if t[idx] == 'w' or t[idx] == 'e':
            instructions.append(t[idx])
            idx += 1
        else:
            instructions.append(t[idx] + t[idx+1])
            idx += 2
    return instructions


def part1(fc):
    tilesBlack = []
    for tile in fc:
        print(tile)
        x = 0
        y = 0
        instructions = parseTile(tile)
        print(instructions)
        for i in instructions:
            if i == 'e':
                x += 1
            elif i == 'w':
                x -= 1
            elif i == 'se':
                x += 0.5
                y -= 0.5
            elif i == 'ne':
                x += 0.5
                y += 0.5
            elif i == 'sw':
                x -= 0.5
                y -= 0.5
            elif i == 'nw':
                x -= 0.5
                y += 0.5
            else:
                print('Not possible')
        if [x,y] in tilesBlack:
            tilesBlack.remove([x,y])
        else:
            tilesBlack.append([x,y])
    return tilesBlack


def countBlack(x,y,tiles):
    black = 0
    if [x+1,y] in tiles:
        black += 1
    if [x-1,y] in tiles:
        black += 1
    if [x+0.5,y-0.5] in tiles:
        black += 1
    if [x+0.5,y+0.5] in tiles:
        black += 1
    if [x-0.5,y-0.5] in tiles:
        black += 1
    if [x-0.5,y+0.5] in tiles:
        black += 1
    
    return black;

def turnTiles(tiles):
    
    minX = maxX = tiles[0][0]
    minY = maxY = tiles[0][1]
    for test in tiles:
        if test[0] < minX:
            minX = test[0]
        if test[0] > maxX:
            maxX = test[0]
        if test[1] < minY:
            minY = test[1]
        if test[1] > maxY:
            maxY = test[1]
    

    #linksboven = [minX, maxY]
    #rechtsboven = [maxX, maxY]
    #linksonder = [minX-1, minY]
    #rechtsonder = [maxX, minY]

    tilesToBeFlipped = []
    #for x in range(minX, maxX, 0.5):
        #for y in range(minY, maxY, 0.5):
    for x in [x / 10.0 for x in range(int((minX-1)*10), int((maxX+1) * 10), 5)]:
        for y in [y / 10.0 for y in range(int((minY-1)*10), int((maxY+1) * 10), 5)]:
            black = countBlack(x,y,tiles)
            if [x,y] in tiles:
                if black == 0 or black > 2:
                    tilesToBeFlipped.append([x,y])
            else:
                if black == 2:
                    tilesToBeFlipped.append([x,y])

    for tileToBeFlipped in tilesToBeFlipped:
        if tileToBeFlipped in tiles:
            tiles.remove(tileToBeFlipped)
        else:
            tiles.append(tileToBeFlipped)
    
    return tiles

fc = open("day24/tiles.txt",'r').read().split('\n')
tilesBlack = part1(fc)

print("===== Part 1 ======")
print(tilesBlack)
print('Number of black tiles: ' + str(len(tilesBlack)))

for day in range(100):
    turnTiles(tilesBlack)

print("===== Part 2 ======")
print(tilesBlack)
print('Number of black tiles: ' + str(len(tilesBlack)))


