import re

def checkPassword(password, phase):
    password = str(password);
    groups = [password.count(ch) for ch in set(password)]
    if phase == 1:
        groupCheck = any((group >= 2) for group in groups)
    else:
        groupCheck = any((group == 2) for group in groups)
    if not groupCheck:
        return False
    elif not bool(re.match(r"^([0-9]{6})$", password)):
        return False
    elif any(password[i] > password[i+1] for i in range(5)):
        return False
    return True

passwords = []

for password in range(245182,790572):
    if checkPassword(password,1):
        passwords.append(password)
print("There are " + str(len(passwords)) + " passwords valid for phase 1")

passwords = []
for password in range(245182,790572):
    if checkPassword(password,2):
        passwords.append(password)
print("There are " + str(len(passwords)) + " passwords valid for phase 2")

