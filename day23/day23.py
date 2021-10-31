input = '157623984'
moves = 10

origin = [int(char) for char in input]  

# print(cups)

# def findDestination(oldset,currentCup,low,high):
#     destinationCup = currentCup-1
#     while True:
#         if destinationCup in oldset:
#             return oldset.index(destinationCup)
#         else:
#             destinationCup -= 1
#             if destinationCup < low:
#                 return oldset.index(high)


# def cycleIndex(idx):
#     if idx < len(cups):
#         return idx
#     else:
#         return idx - len(cups)


# currentIndex = 0

# for i in range(1,moves+1):
#     print("Move " + str(i))
#     oldset = cups.copy()
#     currentCup = cups[currentIndex]
#     firstCup = cups[cycleIndex(currentIndex+1)]
#     secondCup = cups[cycleIndex(currentIndex+2)]
#     thirdCup = cups[cycleIndex(currentIndex+3)]
#     pickset = [firstCup, secondCup, thirdCup]
#     cups.pop(cycleIndex(currentIndex+1))
#     cups.pop(cycleIndex(currentIndex+1))
#     cups.pop(cycleIndex(currentIndex+1))
#     lowest = min(cups)
#     highest = max(cups)
#     destinationIndex = findDestination(cups, currentCup, lowest, highest)
    
#     cups.insert(destinationIndex+1,pickset[2])
#     cups.insert(destinationIndex+1,pickset[1])
#     cups.insert(destinationIndex+1,pickset[0])
    
#     if destinationIndex > currentIndex:
#         currentIndex = cycleIndex(currentIndex+1)
#     else:
#         currentIndex = cycleIndex(currentIndex+4)

# print(cups)

class Cup:
    def __init__(self, value):
        self.value = value # actual value
        self.prev  = None  # pointer to previous Cup (left)
        self.next  = None  # pointer to next Cup (right)

def play(cur, cups, moves):
    maxcup = len(cups) - 1

    for _ in range(moves):
        # Picu up 3 cups
        first  = cur.next
        mid    = first.next
        last   = mid.next
        picked = (first.value, mid.value, last.value)

        # Remove them from the list
        cur.next = last.next
        cur.next.prev = cur

        # Select the destination cup value, after which we'll insert the 3 picked cups
        dst = maxcup if cur.value == 1 else cur.value - 1
        while dst in picked:
            dst = maxcup if dst == 1 else dst - 1

        # Get the corresponding cup from its value
        dst = cups[dst]
        # Insert the picked cups right after it
        first.prev = dst
        last.next  = dst.next
        dst.next.prev = last
        dst.next      = first

        # Advance the current cup
        cur = cur.next


from itertools import chain

def build_list(values, n=None):
    n = (n if n else len(values)) + 1
    cups = [None] * n
    values = chain(values, range(len(values) + 1, n))

    # Instantiate the first Cup right away to connect it to the next one
    first  = next(values)
    cups[first] = Cup(first)
    first = cups[first]
    prev = first

    # Create all Cup instances while also connecting each instance to the previous
    for value in values:
        cur = cups[value] = Cup(value)
        cur.prev = prev
        prev.next = cur
        prev = cur

    # Finally connect the last to the first
    cur.next = first

    return first, cups
    

first, cups = build_list(origin)
play(first, cups, 100)

ans = ''
c = cups[1].next
while c != cups[1]:
    ans += str(c.value)
    c = c.next

print('Part 1:', ans)


first, cups = build_list(origin)
play(first, cups, 10000000)
ans = cups[1].next.value * cups[1].next.next.value
print('Part 2:', ans)



import array

def crabcups(labels, moves=100, cups=0, pick=3):
    cups = max(cups, len(labels))
    a = array.array('I', range(1, cups + 2))
    b = array.array('I', map(int, labels))

    a[0] = a[-1] = b[0]
    for i in range(len(b) - 1):
        a[b[i]] = b[i + 1]
    a[b[len(b) - 1]] = b[0] if cups == len(b) else len(b) + 1

    cur = 0
    for _ in range(moves):
        cur = a[cur]
        nxt = cur - 1 if cur != 1 else cups

        while True:
            i = cur
            found = False
            for _ in range(pick):
                if (i := a[i]) == nxt:
                    found = True
                    nxt = nxt - 1 if nxt != 1 else cups
                    break
            if not found:
                break

        a[i], a[nxt], a[cur] = a[nxt], a[cur], a[i]

    if cups < 10:
        s = ''
        i = a[1]
        while i != 1:
            s += str(i)
            i = a[i]
        print(s)

    return a[1] * a[a[1]]

# Part 1
crabcups(input)

# Part 2
print(crabcups(input, moves=10000000, cups=1000000))