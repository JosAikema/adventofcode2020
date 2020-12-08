


def runProgram(code):
    idx = 0
    stop = False
    acc = 0
    error = 0
    executedLines = []
    while idx < len(code) and not stop:
        if idx in executedLines:
            stop = True
            error = 1
        else:
            executedLines.append(idx)
            instr, param = code[idx].split(' ')
            sign = param[0]
            value = param[1:]
            if instr == 'acc':
                if sign == "+":
                    acc += int(value)
                else:
                    acc -= int(value)
                idx += 1
            elif instr == 'jmp':
                if sign == "+":
                    idx += int(value)
                else:
                    idx -= int(value)
            else:
                idx += 1
    return acc, error, idx

def checkError(error, acc, line):
    if error > 0:
        print("Program has quit with an error " + str(error) + " on line " + str(line) +" and the accumulator is " + str(acc))
    else:
        print("Program ended with succes and the accumulator is " + str(acc))

instructions = open("day8/instructions.txt",'r').read().split('\n')
print("First run")
acc, error, line = runProgram(instructions)
checkError(error, acc, line)


print("=========")
print("Try to fix the bug")
idx = 0

for test in instructions:
    instr, param = instructions[idx].split(' ')
    testInstructions = instructions.copy()
    if instr == 'jmp':
        testInstructions[idx] = 'nop ' + param
        acc, error, line = runProgram(testInstructions)
        checkError(error, acc, line)
    elif instr == 'nop':
        testInstructions[idx] = 'jmp ' + param
        acc, error, line = runProgram(testInstructions)
        checkError(error, acc, line)
    if error == 0:
        break
    else:
        idx += 1
        
        





