f = open("Day16/input.txt", "r").read().split('\n')

def parseText(lines):
    rules = []
    stage = 'rules'
    myTicketFields = []
    nearbyTickets = []
    for line in lines:
        if line != '':
            if line == 'your ticket:':
                stage = 'yourticket'
            elif line == 'nearby tickets:':
                stage = 'nearbytickets'
            else:
                if stage == 'rules':
                    field, conditionsTotal = line.split(': ')
                    conditions = conditionsTotal.split(' or ')
                    #for condition in conditions:
                    rules.append([field, conditions])
                elif stage == 'yourticket':
                    myTicketFields = line.split(',')
                else:
                    nearbyTickets.append(line.split(","))
    return rules, myTicketFields, nearbyTickets

def validTicket(t, rules):
    valid = True
    nonvalidFields = t.copy()
    for field in t:
        fieldValid = False
        for rule in rules:
            if not fieldValid:
                ruleValid = False
                for condition in rule[1]:
                    rangeStart, rangeEnd = condition.split('-')
                    if (int(field) >= int(rangeStart) and int(field) <= int(rangeEnd)):
                        ruleValid = True
                fieldValid = ruleValid
            if fieldValid:
                break
                
        if not fieldValid:
            valid = False
        else:
            nonvalidFields.remove(field)
    return valid, nonvalidFields

def checkRule(rule,field):
    
    ruleValid = False
    for condition in rule:
        rangeStart, rangeEnd = condition.split('-')
        if int(field)>= int(rangeStart) and int(field) <= int(rangeEnd):
            ruleValid = True
    return ruleValid


rules, myTicketFields, nearbyTickets = parseText(f)

sum = 0

print("Total tickets: " + str(len(nearbyTickets)))
validNearbyTickets = nearbyTickets.copy()
for ticket in nearbyTickets:
    valid, nonValidFields = validTicket(ticket, rules)
    if valid:
        print (','.join([str(elem) for elem in ticket]))
    if not valid:
        #print('Ticket ' + ticket + ' is valid')
    #else:
        #print (' '.join([str(elem) for elem in ticket]))
        #print('Ticket ' + ticket + ' is not valid')
        #print(nonValidFields)
        for f in nonValidFields:
            sum += int(f)
        validNearbyTickets.remove(ticket)
        
print("Sum is " + str(sum))

print("Total valid tickets: " + str(len(validNearbyTickets)))

    
