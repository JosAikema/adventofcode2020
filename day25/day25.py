def encode(subjectNumber, loopSize, start = 1, startLoopSize = 0):
    result = start
    for loop in range(startLoopSize,loopSize):
        
        result *= subjectNumber
        result = result % 20201227
    return result

def decode(subjectNumber,key):
    loopSize = 1
    result = 1
    while True:
        result = encode(subjectNumber,loopSize, result, loopSize-1)
        if result == key:
            return loopSize
        else:
            loopSize += 1


cardPublicKey = 14082811
doorPublicKey = 5249543

#print("Public key card: " + str(cardPublicKey))
#print("Public key door: " + str(cardPublicKey))

loopSizeCard = decode(7,cardPublicKey)
loopSizeDoor = decode(7,doorPublicKey)

print("Loopsize card: " + str(loopSizeCard))
print("Loopsize door: " + str(loopSizeDoor))

encryptionKeyCard = encode(doorPublicKey, loopSizeCard)
encryptionDoor = encode(cardPublicKey, loopSizeDoor)

print("Encryption key card: " + str(encryptionKeyCard))
print("Encryption key door: " + str(encryptionDoor))