content = open("day19/input.txt",'r').read().split('\n')

# import re

# def expandRule(rule):
#     result = ''
#     if re.match('^\d$', rule):
#         result = rules[int(rule)]
#     else:
#         for d in rule.split(" "):
#             result += expandRule(d)
#     return result


# messages = []
# rules = {}
# getRules = True
# for line in content:
#     if line == '':
#         getRules = False
#     elif getRules:
#         idx, rule = line.split(": ")
#         rules[int(idx)] = rule.strip('"')
#     else:
#         messages.append(line)

# print(rules)
# print(messages)
# print("===============")

# #for key, rule in rules.items():
# r = expandRule(rules[0])
# print(r)

#4 1 5

#4 -> a
#1 -> 2 3 | 3 2 -> 4 4 | 5 5 4 5 | 5 4 -> a a | b b a b | b a 
#5 -> b 

# given string s and list of rules seq is there a way to produce s using seq?
def test(s,seq):
    if s == '' or seq == []:
        return s == '' and seq == [] # if both are empty, True. If only one, False.
    
    r = rules[seq[0]]
    if '"' in r:
        if s[0] in r:
            return test(s[1:], seq[1:]) # strip first character
        else:
            return False # wrong first character
    else:
        return any(test(s, t + seq[1:]) for t in r) # expand first term

def parse_rule(s):
    n,e = s.split(": ")
    if '"' not in e:
        e = [[int(r) for r in t.split()] for t in e.split("|")]
    return (int(n),e)

rule_text, messages = [x.splitlines() for x in open("day19/input.txt").read().split("\n\n")]
rules = dict(parse_rule(s) for s in rule_text)            
print("Part 1:", sum(test(m,[0]) for m in messages))       

rule_text += ["8: 42 | 42 8","11: 42 31 | 42 11 31"]
rules = dict(parse_rule(s) for s in rule_text)
print("Part 2:", sum(test(m,[0]) for m in messages)) 