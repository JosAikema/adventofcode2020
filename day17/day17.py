content = open("day17/matrix.txt",'r').read().splitlines()

active = {(x, y, 0, 0) for y, line in enumerate(content) for x, state in enumerate(line) if state == '#'}

def count_active_neighbours(active, x, y, z, w, dw_min, dw_max):
    active_neighbours = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(dw_min, dw_max + 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    active_neighbours += (x + dx, y + dy, z + dz, w + dw) in active
    return active_neighbours

def run_cycles(active, dw_min, dw_max):
    for _ in range(6):
        cycle_active = set()
        minx = miny = minz = minw = float('inf')
        maxx = maxy = maxz = maxw = float('-inf')
        for x, y, z, w in active:
            minx, maxx = min(minx, x), max(maxx, x)
            miny, maxy = min(miny, y), max(maxy, y)
            minz, maxz = min(minz, z), max(maxz, z)
            minw, maxw = min(minw, w), max(maxw, w)
        for x in range(minx - 1, maxx + 2):
            for y in range(miny - 1, maxy + 2):
                for z in range(minz - 1, maxz + 2):
                    for w in range(minw - 1, maxw + 2):
                        active_neighbours = count_active_neighbours(active, x, y, z, w, dw_min, dw_max)
                        if (x, y, z, w) in active and active_neighbours in (2, 3):
                            cycle_active.add((x, y, z, w))
                        if (x, y, z, w) not in active and active_neighbours == 3:
                            cycle_active.add((x, y, z, w))
        active = cycle_active
    return len(active)

part1 = run_cycles(active, 0, 0)
part2 = run_cycles(active, -1, 1)

print(f'Part 1: {part1}, Part 2: {part2}')

def countNeighbours(m, x, y, z):
    alive = 0
    for dx in range(x - 1, x + 2):
        for dy in range(y - 1, y + 2):
            for dz in range(z - 1, z + 2):
                if dx != x or dy != y or dz != z:
                    if (dx, dy, dz) in m:
                        alive += 1
    return alive

def bounds(cube):
    lox = min(map(lambda p: p[0], cube)) - 1
    loy = min(map(lambda p: p[1], cube)) - 1
    loz = min(map(lambda p: p[2], cube)) - 1
    hix = max(map(lambda p: p[0], cube)) + 2
    hiy = max(map(lambda p: p[1], cube)) + 2
    hiz = max(map(lambda p: p[2], cube)) + 2
    return range(lox, hix), range(loy, hiy), range(loz, hiz)

def doCycle(m):
    new = set()
    rangex, rangey, rangez = bounds(m)

    for x in rangex:
        for y in rangey:
            for z in rangez:
                alive = countNeighbours(m, x, y, z)

                if (x, y, z) in m:
                    if alive == 2 or alive == 3:
                        # alive cell stays alive only if exactly 2 or 3 neighbors are alive
                        new.add((x, y, z))
                elif alive == 3:
                    # dead cell becomes alive only if exactly 3 neighbors are alive
                    new.add((x, y, z))

    return new

def doCycleJos(m):
    print(m)
    return m

matrix = set()

for x, row in enumerate(content):
    for y, cell in enumerate(row):
        if cell == '#':
            matrix.add((x, y, 0))

#print(matrix)

for run in (range(1)):
    matrix = doCycleJos(matrix)

#print(matrix)
answer = len(matrix)

print("Answer for part1: " + str(answer))

