import math

def calculateSameAnswers(answer, count):
    s = 0
    for i in range(ord('a'), ord('z') + 1):
       s = s + math.floor(answer.count(chr(i))/count) 
    return s

def convertToGroups(c):
    groups =[]
    countPassengers = 0
    answerString = ''
    answers = []
    for line in c:
        if line == "":
            groups.append([countPassengers, answerString, len(set(answerString)), calculateSameAnswers(answerString, countPassengers), answers])
            countPassengers = 0
            answerString = ''
            answers = []
        else:
            countPassengers += 1 
            answerString = answerString + line
            answers.append(line)
    groups.append([countPassengers, answerString, len(set(answerString)), calculateSameAnswers(answerString, countPassengers), answers])
           
        
        
    return groups

content = open("Day6/answers.txt",'r').read().split('\n')

groups = convertToGroups(content)

totalUnique = 0
totalSame = 0
for group in groups:
    totalUnique = totalUnique + group[2]
    totalSame = totalSame + group[3]
    print("Number of passengers: " + str(group[0]) + ", anwers: " + ''.join(sorted(str(group[1]))) + " (Unique: " + str(group[2]) +" / Answered all yes: " + str(group[3]) +")")

print("Total unique answers: " + str(totalUnique))
print("Total same answers: " + str(totalSame))

