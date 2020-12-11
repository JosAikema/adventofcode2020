def getFullPath(adapters):
    prev = 0
    one = 0
    three = 0
    other = 0
    for adapter in adapters:
        diff = adapter - prev
        if diff == 1:
            one += 1
        elif diff == 3:
            three += 1
        else:
            other += 1
        prev = adapter
    return one*three

from functools import lru_cache
@lru_cache
def searchPath(adapterIndex):
    if adapterIndex >= len(adapters):
        return 1
    
    adapter = adapters[adapterIndex]
    result = searchPath(adapterIndex+1)

    if adapterIndex + 2 < len(adapters) and adapters[adapterIndex+2] - adapter <=3:
        result += searchPath(adapterIndex + 2)
        if adapterIndex + 3 < len(adapters) and adapters[adapterIndex + 3] - adapter <= 3:
            result += searchPath(adapterIndex + 3)

    return result

def getAdapters():
    adapters = open("day10/adapters.txt",'r').read().split('\n')
    
    #Convert all adapter to int
    for i in range(len(adapters)):
        adapters[i] = int(adapters[i])
    #Sort adapters
    adapters.sort()

    #Add start and endpoint
    adapters = [0] + adapters + [adapters[-1] + 3]
    return adapters

adapters = getAdapters()
answer = getFullPath(adapters)
print ("The answer for part 1 is " + str(answer))

path = searchPath(0)
print("The answer for part 2 is " + str(path))




