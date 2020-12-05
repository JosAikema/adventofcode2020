import math

def searchSeat(str,highChar,lower,upper):
    for c in str:
        if c == highChar:
            lower = math.floor((lower + upper) / 2)
        else:
            upper = math.floor((lower + upper) / 2)
    return upper

def getSeat(boarding_pass):
    row = searchSeat(boarding_pass[0:-3],"B",0,127)
    column = searchSeat(boarding_pass[-3:],"R",0,7)
    seatId = (row * 8) + column
    return row, column, seatId

def searchMySeat(values):
    row = 0
    counter = 0
    seats = []
    for value in values:
        seats.append(value[1])
        if value[0] != row:
            if counter != 7 and row != 0 and row != 121:
                missingRow = row
                missingSeat = [ele for ele in range(max(seats)+1) if ele not in seats] 
            counter = 0
            row = value[0]
            seats.clear()
        else:
            counter += 1
    return missingRow, missingSeat[0]

boarding_passes = sorted(open("Day5/boarding_passes.txt",'r').read().split('\n'))

highest = 0
values = []

for boarding_pass in boarding_passes:
    row, column, seatId = getSeat(boarding_pass)
    highest = max(seatId,highest)
    value = [row,column]
    values.append(value)

print("Max seatId: " + str(highest))

mySeatRow, mySeat = searchMySeat(values)
print("My seat is on row "+ str(mySeatRow) + " and seat " + str(mySeat) + " (seatId: " + str(mySeatRow*8+mySeat) +")")