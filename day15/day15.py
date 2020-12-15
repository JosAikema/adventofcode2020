numbers = [0,6,1,7,2,19,20]
max = 30000000
#max = 2020

turns = len(numbers) + 1
finished = False

numbersChosen = {x: i + 1 for i, x in enumerate(numbers)}
prev = numbers[-1]
while not finished:
     if turns == max + 1:
         finished = True
     else:
        if prev in numbersChosen:
            n = turns - 1 - numbersChosen[prev]
        else:
            n = 0    
        numbersChosen[prev] = turns - 1
        prev = n
        turns += 1

print("The number chosen in turn " + str(turns-1) + " is " + str(n))



