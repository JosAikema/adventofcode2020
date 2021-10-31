

def convertToInstruction(code):

    # position 0 -> operator
    # position 1 -> parammode for parameter 1
    # position 2 -> parammode for parameter 2
    # position 3 -> parammode for parameter 3
    # position 4 -> parammode for parameter 4
    
    intcode = []

    for c in reversed(str(code).rjust(5, '0')):
        intcode.append(int(c))
    del intcode[1]

    return intcode



def runProgram(code, input):
    def getValue(mode,pos):
        if mode == 0:
            return code[code[pos]]
        else:
            return code[pos]
    
    def setValue(mode,pos, value):
        if mode == 0:
            code[code[pos]] = value
        else:
            code[pos] = value

    idx = 0
    while idx < len(code) and code[idx] != 99:
        #print(code[idx])
        instruction = convertToInstruction(code[idx])
        operator = instruction[0]
        if operator == 1:
            value = getValue(instruction[1], idx+1) + getValue(instruction[2], idx+2)
            code[code[idx+3]] = value
            idx += 4
        elif operator == 2:
            value = getValue(instruction[1], idx+1) * getValue(instruction[2], idx+2)
            code[code[idx+3]] = value
            idx += 4
        elif operator == 3:
            code[code[idx+1]] = input
            idx += 2
        elif operator == 4:  
            print(getValue(instruction[1],idx+1))  
            idx += 2
        elif operator == 5:
            if getValue(instruction[1], idx+1) != 0:
                idx = getValue(instruction[2], idx+2)
            else:
                idx += 3
        elif operator == 6:
            if getValue(instruction[1], idx+1) == 0:
                idx = getValue(instruction[2], idx+2)
            else:
                idx += 3
        elif operator == 7:
            if getValue(instruction[1], idx + 1) < getValue(instruction[2], idx + 2):
                setValue(instruction[3], idx+3, 1)
            else:
                setValue(instruction[3], idx+3, 0)
            idx += 4
        elif operator == 8:
            if getValue(instruction[1], idx + 1) == getValue(instruction[2], idx + 2):
                setValue(instruction[3], idx+3, 1)
            else:
                setValue(instruction[3], idx+3, 0)
            idx += 4 
        #print('Value : ' + str(value))
        
    return code



prg = open("2019/day5/program.txt",'r').read().split(',')
for i in range(len(prg)):
    prg[i] = int(prg[i])


#print("Output part 1")
#output = runProgram(prg, 1)

print("==========")
print("Output part 2")
output = runProgram(prg, 5)





