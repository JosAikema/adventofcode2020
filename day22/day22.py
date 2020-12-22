def parse(filecontent):
    cards = {}
    for p in filecontent:
        player = int(p.split('\n')[0].split(' ')[1][:-1])
        cards[player] = p.split('\n')[1:]
    return cards

def playFirstPart(cards):
    play = True
    round = 1
    while play:
        if int(cards[1][0]) > int(cards[2][0]):
            cards[1].append(cards[1][0])
            cards[1].append(cards[2][0])
        else:
            cards[2].append(cards[2][0])
            cards[2].append(cards[1][0])
        cards[1].pop(0)
        cards[2].pop(0)
        if len(cards[1]) == 0 or len(cards[2]) == 0:
            play = False
        else:
            round += 1
    return cards


def playRecursiveCombat(cards):
    previousDecks = set()
    play = True
    winner = 0
    while play:
        if (tuple(cards[1]), tuple(cards[2])) in previousDecks:
            play = False
            return 1, cards[1]
        
        previousDecks.add((tuple(cards[1]), tuple(cards[2])))
        if int(cards[1][0]) < len(cards[1]) and int(cards[2][0]) < len(cards[2]):
            cardsToPlayWith = {}
            cardsToPlayWith[1] = cards[1].copy()
            cardsToPlayWith[2] = cards[2].copy()
            cardsToPlayWith[1] = cardsToPlayWith[1][1:int(cards[1][0])+1]
            cardsToPlayWith[2] = cardsToPlayWith[2][1:int(cards[2][0])+1]
            winner, cardsWinner = playRecursiveCombat(cardsToPlayWith)
        else:
            if int(cards[1][0]) > int(cards[2][0]):
                winner = 1
            else:
                winner = 2
        if winner == 1:
            cards[1].append(cards[1][0])
            cards[1].append(cards[2][0])
        else:
            cards[2].append(cards[2][0])
            cards[2].append(cards[1][0])   
        cards[1].pop(0)
        cards[2].pop(0)
        if len(cards[1]) == 0 or len(cards[2]) == 0:
            play = False
    return winner, cards[winner]


def calculateScorePart1(cards):
    
    results = {}
    for player, deck in cards.items():
        results[player] = calculateScore(deck)
    return results

def calculateScore(deck):
    sum = 0
        
    for idx in range(len(deck)):
        sum += int(deck[idx]) * (len(deck) - idx)
    return sum


print('===========')
print("Part 1:")

fc = open("day22/cards.txt",'r').read().split('\n\n')
cards = parse(fc)
cards = playFirstPart(cards)
scores = calculateScorePart1(cards)

for key,score in scores.items():
    print("Player " + str(key) + " score is " + str(score))

print('===========')

cards = parse(fc)
winner, cardsWinner = playRecursiveCombat(cards)
scores = calculateScore(cardsWinner)

print('Part 2 is won by player ' + str(winner) + ' with a score of ' + str(score))

