instructions = open("day12/instructions.txt",'r').read().split('\n')


directions = ["N", "E", "S", "W"]


def getPositionPart1():
    x = y = 0
    dir = "E"
    for i in instructions:
        cmd = i[0]
        value = int(i[1:])
        
        if cmd == "F":
            if dir == "N":
                y += value
            elif dir == "S":
                y -= value
            elif dir == "E":
                x += value
            else:
                x -= value
        elif cmd == "N":
            y += value
        elif cmd == "S":
            y -= value
        elif cmd == "E":
            x += value
        elif cmd == "W":
            x -= value
        elif cmd == "R":
            currentDirIndex = directions.index(dir)
            value = int(value / 90)
            newDirIndex = currentDirIndex+value
            if newDirIndex > 3:
                newDirIndex -= 4
            dir = directions[newDirIndex]
        elif cmd == "L":
            currentDirIndex = directions.index(dir)
            value = int(value / 90)
            newDirIndex = currentDirIndex - value
            if newDirIndex < 0:
                newDirIndex += 4
            dir = directions[newDirIndex]
    return x,y

def getPositionPart2():
    xShip = 0
    yShip = 0
    x = 10 
    y = 1 
    for i in instructions:
        cmd = i[0]
        value = int(i[1:])
        
        if cmd == 'N':
            y += value
        elif cmd == 'S':
            y -= value
        elif cmd == 'E':
            x += value
        elif cmd == 'W':
            x -= value
        elif cmd == 'L':
            turns = int(value / 90)
            for i in range(0,turns):
                x, y = -y, x
        elif cmd == 'R':
            turns = int(value / 90)
            for i in range(0,turns):
                x, y = y, -x
        elif cmd == 'F':
            xShip += value * x
            yShip += value * y
    return xShip, yShip 
        

x, y = getPositionPart1()
print(str(x) + ":" + str(y))
print("The answer for part 1 is " + str(abs(x)+abs(y)))

x, y = getPositionPart2()
print(str(x) + ":" + str(y))
print("The answer for part 2 is " + str(abs(x)+abs(y)))
