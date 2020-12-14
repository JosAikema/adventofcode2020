filecontent = open("day14/instructions.txt",'r').read().split('\n')

mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def v1(codes):
    memory = {}
    for i in range(0,len(codes)):
        
        line = codes[i]
        if line[0:4] == 'mask':
            part1, mask = line.split(' = ')
        else:
            part1, value = line.split(' = ')
            part1, address = part1.split("[")
            address = int(address[:-1])
            valueStr = str(bin(int(value)))[2:]
            valueStr = valueStr.zfill(36)
            newValueStr = ''
            for i, ch in enumerate(valueStr):
                if mask[i] == 'X':
                    newValueStr += ch
                else:
                    newValueStr += mask[i]
            newValue = int(newValueStr,2)
            memory[address] = newValue
    return memory

import itertools

def v2(codes):
    memory = {}
    for i in range(0,len(codes)):
        
        line = codes[i]
        if line[0:4] == 'mask':
            part1, mask = line.split(' = ')
        else:
            part1, value = line.split(' = ')
            part1, address = part1.split("[")
            address = int(address[:-1])  
            addressStr = str(bin(int(address)))[2:]
            addressStr = addressStr.zfill(36) 
            newAddressStr = ''
            for i, ch in enumerate(addressStr):
                if mask[i] == '0':
                    newAddressStr += ch
                elif mask[i] == '1':
                    newAddressStr += '1'
                else:
                    newAddressStr += 'X'
            
            turns = []
            for x in map(''.join, itertools.product('01', repeat=newAddressStr.count('X'))):
                turns.append(x)
            
            for turn in turns:
                newStr = ''
                xCtr = 0
                for i, ch in enumerate(newAddressStr):
                    if ch == "X":
                        newStr += turn[xCtr]
                        xCtr += 1
                    else:
                        newStr += ch
                newAddress = int(newStr,2)
                memory[newAddress] = int(value)
    return memory 



memory = v1(filecontent)
print("The answer for part1 is " + str(sum(memory.values())))

memory = v2(filecontent)
print("The answer for part2 is " + str(sum(memory.values())))
        



    

