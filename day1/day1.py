f = open("Day1/expenses_report.txt", "r")
foundWithTwo = False
foundWithThree = False
content = f.readlines()
for i in content:
    for j in content:
        som = int(i) + int(j)
        if som == 2020 and not foundWithTwo:
            print("For the numbers " + str(int(i)) + "  and " + str(int(j)) + " the sum is 2020 and the product is "+ str(int(i)*int(j)))
            foundWithTwo = True
        for k in content:
            som = int(i)+int(j)+int(k)
            if som == 2020 and not foundWithThree:
                print("For the numbers " + str(int(i)) + ", " + str(int(j)) + "  and " + str(int(k)) + " the sum is 2020 and the product is "+ str(int(i)*int(j)*int(k)))
                foundWithThree = True

