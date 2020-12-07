def parseFile(rulesfile):
    end = ['root']
    rules = {}
    for line in rulesfile:
        line = line.replace(' bags','').replace(' bag','').replace('.','')
        rule = line.split(' contain ')
        if 'no other' in line:
            rules[rule[0]] = {}
            end.append(rule[0])
        else:
            rules[rule[0]] = {}
            for rulePart in rule[1].split(', '):
                rulePartParts = rulePart.split(' ',1)
                rules[rule[0]][rulePartParts[1]] = int(rulePartParts[0])
    return end, rules



def checkRule(rules, searchTerm):
    for rule in rules:
        if rule == searchTerm:
            return True
        else:
            if checkRule(rulesSet[rule], searchTerm) == True:
                return True

def countBags(rules,count):
    for rule in rules:
        thisCounter = rules[rule]
        if rule not in endBags:
            nextRule = {}
            for bag in rulesSet[rule]:
                countNumberBags = rulesSet[rule][bag]
                nextRule[bag] = countNumberBags * thisCounter
            nextRule.update({'root':thisCounter})
            count = countBags(nextRule,count)
        else:
            count += thisCounter
    return count


rulesfile = open("Day7/rules.txt",'r').read().split('\n')

endBags, rulesSet = parseFile(rulesfile)

checkedRules = {rule:checkRule(rulesSet[rule], 'shiny gold') for rule in rulesSet}

totalA = 0
for bag, checked in checkedRules.items():
    if checked:
        totalA += 1

print ("There are " + str(totalA) + " bag colors that can contain at least one shiny gold bag")

numberBags = countBags(rulesSet['shiny gold'],0)
print ("There are " + str(numberBags) + " bags required inside one shiny gold bag")
