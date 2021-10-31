


def runProgram(code, noun, verb):
    code[1] = noun
    code[2] = verb
    idx = 0
    while idx < len(code) and code[idx] != '99':
        #print(code[idx])
        if code[idx] == '1':
            value = int(code[int(code[idx+1])]) + int(code[int(code[idx+2])])
            positions[int(positions[idx+3])] = value
        elif code[idx] == '2':
            value = int(code[int(code[idx+1])]) * int(code[int(code[idx+2])])
            code[int(code[idx+3])] = value
        #print('Value : ' + str(value))
        idx += 4
    return code

positions = open("intcode/program.txt",'r').read().split(',')

print(*positions)
print("Output")
output = runProgram(positions, 12, 2)
print(*positions)

#Calculate for output 19690720
for i in range(0,100):
    for j in range (0,100):
        positions = open("intcode/program.txt",'r').read().split(',')
        output = runProgram(positions, i, j)
        if output[0] == 19690720:
            print("Noun " + str(i) + " and verb " + str(j) + " = " + str(output[0]) + " (answer=" + str(i * 100 + j) + ")")



