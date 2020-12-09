numbers = open("day9/numbers.txt",'r').read().split('\n')

def createGrid(numbersToCheck):
    grid = []
    for i in numbersToCheck:
        for j in numbersToCheck:
            grid.append(int(i)+int(j))
    return grid

def findNumbers(numbers, weakness):
    sum = 0
    start = 0
    for idx, item in enumerate(numbers):
        sum += int(item)

        while sum > weakness and start < idx-1:
            sum -= int(numbers[start])
            start += 1

        if sum == weakness:
            return numbers[start:idx+1]



preamble = 25
    
for idx, n in enumerate(numbers[preamble:]):
    checkGrid = createGrid(numbers[idx:idx+preamble])
    if int(n) not in checkGrid:
        print("Number " + n + " is not valid for part 1")
        weakness = int(n)

range = findNumbers(numbers, weakness)

print("The numbers are " + str(range[0]) + " and " + str(range[-1:][0]) + ", so the answer is " + str(int(range[0]) + int(range[-1:][0])))


