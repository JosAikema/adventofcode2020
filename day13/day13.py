filecontent = open("day13/bus.txt",'r').read().split('\n')

busStr = filecontent[1]
bs = busStr.split(",")

buses = []
idx = 0
for bus in bs:
    if bus != 'x':
        buses.append([idx,int(bus)])
    idx += 1

ts = int(filecontent[0])
smallest = buses[0][1] - (ts % buses[0][1])

for bus in buses:
    x = bus[1] - (ts % bus[1])
    if x != 0:
        if x < smallest:
            smallest = x
            busBelongToSmallest = bus[1]


print("The answer for part 1 is " + str(smallest*busBelongToSmallest))

multiplier = 1
sum = 0
for bus in buses:
    busNr = bus[1]    
    while True:
        if (bus[0] + sum) % busNr == 0: break
        sum += multiplier
    multiplier *= busNr
print('Answer 2 for part 2 is' + str(sum))



      
