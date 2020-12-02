f = open("Day2/passwords.txt", "r")
passwords = f.readlines()
validPasswordsPart1 = 0
validPasswordsPart2 = 0
for p in passwords:
    firstNumber = int(p.split("-")[0])
    secondNumber = int(p.split("-")[1].split(" ")[0])
    character = p.split("-")[1].split(" ")[1][0]
    password = p.split("-")[1].split(" ")[2]
    validPasswordsPart1 += password.count(character) >= firstNumber and password.count(character) <= secondNumber
    # Python does  not have the xor operator, use != instead
    # Python is zero-based, so we need to do a -1 to access the right character
    validPasswordsPart2 += (password[firstNumber-1] == character) != (password[secondNumber-1] == character)
        
print("There are " + str(validPasswordsPart1) + " valid passwords in the file according to the old policy")
print("There are " + str(validPasswordsPart2) + " valid passwords in the file according to the new policy")