def walk(mapLines,right, down):
    numberTrees = 0
    placeToCheck = 0
    for lineNumber in range(0,len(mapLines),down):
        if mapLines[lineNumber][placeToCheck] == "#":
            numberTrees += 1
        placeToCheck += right
    return numberTrees

f = open("Day3/map_big.txt", "r")
mapLines = f.readlines()
answer1 = walk(mapLines,1,1)
answer2 = walk(mapLines,3,1)
answer3 = walk(mapLines,5,1)
answer4 = walk(mapLines,7,1)
answer5 = walk(mapLines,1,2)
print("Number of trees for slope 1,1: " + str(answer1))
print("Number of trees for slope 3,1: " + str(answer2))
print("Number of trees for slope 5,1: " + str(answer3))
print("Number of trees for slope 7,1: " + str(answer4))
print("Number of trees for slope 1,2: " + str(answer5))
print("Multiplied : " + str(answer1*answer2*answer3*answer4*answer5))

    