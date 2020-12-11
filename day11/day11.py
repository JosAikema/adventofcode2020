

def getEndSet(seats, lines, seatsPerLine, SeatsInSight, groupSize):

    def countNeighbours(checkseats,x,y, SeatsInSight):
        def getNeightBours(x, y, dx, dy, workingset):
            while True:
                x += dx
                y += dy
                seatInSight = workingset.get((x,y))
                if seatInSight != '.':
                    return seatInSight
        count = 0

        if SeatsInSight:
            neightBours = [
                getNeightBours(x, y, -1, -1, checkseats),
                getNeightBours(x, y, 0, -1, checkseats),
                getNeightBours(x, y, 1, -1, checkseats),
                getNeightBours(x, y, -1, 0, checkseats),
                getNeightBours(x, y, 1, 0, checkseats),
                getNeightBours(x, y, -1, 1, checkseats),
                getNeightBours(x, y, 0, 1, checkseats),
                getNeightBours(x, y, 1, 1, checkseats),
            ]

            count = neightBours.count('#')
        else:
            if checkseats.get((x-1, y-1), '.') == '#':
                count += 1
            if checkseats.get((x, y-1), '.') == '#':
                count += 1
            if checkseats.get((x+1, y-1), '.') == '#':
                count += 1
            if checkseats.get((x-1, y), '.') == '#':
                count += 1
            if checkseats.get((x+1, y), '.') == '#':
                count += 1
            if checkseats.get((x-1, y+1), '.') == '#':
                count += 1
            if checkseats.get((x, y+1), '.') == '#':
                count += 1
            if checkseats.get((x+1, y+1), '.') == '#':
                count += 1

        return count

    changing = True
    workingset = seats.copy()
    prevset = workingset.copy()

    while changing:
        
        for y in range(0,lines):
            for x in range(0,seatsPerLine):
                if workingset[x,y] != '.':
                    neighbours = countNeighbours(prevset,x,y, SeatsInSight)
                    if neighbours == 0:
                        if workingset[x,y] == "L":
                            workingset[x,y] = "#"
                    elif neighbours >= groupSize:
                        if workingset[x,y] == "#":
                            workingset[x,y] = "L"
        
        if workingset == prevset:
            changing = False
        else:
            prevset = workingset.copy()
    return workingset



seatLines = open("day11/seats.txt",'r').read().split('\n')
lines = len(seatLines)
seatsPerLine = len(seatLines[0])
seats = {}
for i1, line in enumerate(seatLines):
    for i2, character in enumerate(line):
        seats[(i2, i1)] = character

#Phase 1
endSet = getEndSet(seats, lines, seatsPerLine, False, 4)
sum = 0
for i in endSet:
    if endSet[i] == "#":
        sum += 1
    
print("The answer for the first phase is " + str(sum))

#Phase 2
endSet = getEndSet(seats, lines, seatsPerLine, True, 5)
sum = 0
for i in endSet:
    if endSet[i] == "#":
        sum += 1

print("The answer for the second phase is " + str(sum))
