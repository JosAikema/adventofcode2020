import re

def convertToPassports(c):
    passports = []
    passport = ''
    for line in c:
        if line != '\n':
            passport += line.replace("\n", " ")
        else:
            passports.append(passport)
            passport = ''
    #Last one has no newline after
    passports.append(passport)
    return passports

def checkDataIsValid(field):
    fieldname, value = field.split(":")
    if fieldname == 'byr':
        return len(value) == 4 and (int(value) >= 1920) and (int(value) <= 2002)
    elif fieldname == 'iyr':
        return len(value) == 4 and (int(value) >= 2010) and (int(value) <= 2020)
    elif fieldname == 'eyr':
        return len(value) == 4 and (int(value) >= 2020) and (int(value) <= 2030)
    elif fieldname == 'hgt':
        if value[-2:] == 'cm':
            return int(value[0:len(value)-2]) >= 150 and int(value[0:len(value)-2]) <= 193
        elif value[-2:] == 'in':
            return int(value[0:len(value)-2]) >= 59 and int(value[0:len(value)-2]) <= 76
    elif fieldname == 'hcl':
        return bool(re.match(r"^#([a-f0-9]{6})$", value))
    elif fieldname == 'ecl':
        return value in ['amb','blu','brn','gry','grn','hzl','oth']
    elif fieldname == 'pid':
        return bool(re.match(r"^\d{9}$", value))
    elif fieldname == 'cid':
        return True
    return False

def countValidPassports(passports):
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    closeYourEyesFields = ["cid"]
    validCount = 0  
    validDataCount = 0
    for passport in passports:
        fields = passport.split(" ")
        fieldsInPassport = []
        for field in fields:
            if field != '':
                fieldname, value = field.split(":")
                fieldsInPassport.append(fieldname)
        valid = True
        validData = False
        for requiredField in requiredFields:
            if requiredField not in fieldsInPassport:
                if requiredField not in closeYourEyesFields:
                    valid = False
        if valid:
            validCount += 1
            validData = True
            for field in fields:
                if validData and field != '':
                    validData = checkDataIsValid(field)
            if validData:
                validDataCount += 1
    return validCount, validDataCount

f = open("Day4/passports.txt", "r")
content = f.readlines()
passports = convertToPassports(content)
valid, validData = countValidPassports(passports)

print("There are " + str(len(passports)) + " passports in the file of which " + str(valid) + " are valid but only " + str(validData) + " has valid data")