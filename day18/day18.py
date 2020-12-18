toCalculate = open("day18/sum.txt",'r').read().split('\n')

def calculate(s, phase = 1):
    fs = parse(s, phase)
    new = ''
    
    if phase == 1:
        result = 0
        for f in fs:
            if f[0] == "+":
                result += int(f[1])
            elif f[0] == "*":
                result *= int(f[1])
            else:
                result = int(f[1])
    else:
        for f in fs:
            new += f[0]
            new += str(f[1])
        result =  1
        for n in new.split("*"):
            result *= eval(n)
        
    return result
     

def parse(s, phase):
    
    factors = []
    op = ''
    parantheses = 0
    for ch in s:
        if ch != ' ':
            if parantheses != 0:
                if ch == ")":
                    parantheses -= 1
                    if parantheses == 0:
                        value = calculate(sub, phase)
                        factors.append([op, value])
                    else:
                        sub += ch
                else:
                    if ch == "(":
                        parantheses += 1
                    sub += ch
            else:
                if ch == "(":
                    parantheses += 1
                    sub = ""
                elif ch == '*' or ch == '+':
                    op = ch
                else:
                    value = ch
                    factors.append([op, value])
    
    return factors



print("Test1 (71): " + str(calculate('1 + 2 * 3 + 4 * 5 + 6')))
print("Test2 (61): " + str(calculate('1 + (2 * 3) + 4 * 5 + 6')))
print("Test2 (51): " + str(calculate('1 + (2 * 3) + (4 * (5 + 6))')))
print("Test3 (26): " + str(calculate('2 * 3 + (4 * 5)')))
print("Test4 (437): " + str(calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)')))
print("Test5 (12240): " + str(calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')))
print("Test6 (13632): " + str(calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')))

answer1 = 0
for i, o in enumerate(toCalculate):
    answer1 += calculate(o)

print("The answer for part1 is " + str(answer1))

print("Test2-1 (231): " + str(calculate('1 + 2 * 3 + 4 * 5 + 6',2)))
print("Test2-3 (51): " + str(calculate('1 + (2 * 3) + (4 * (5 + 6))',2)))
print("Test2-3 (46): " + str(calculate('2 * 3 + (4 * 5)',2)))
print("Test2-4 (1445): " + str(calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)',2)))
print("Test2-5 (669060): " + str(calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',2)))
print("Test2-6 (23340): " + str(calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',2)))

answer2 = 0
for i, o in enumerate(toCalculate):
    answer2 += calculate(o,2)

print("The answer for part1 is " + str(answer2))