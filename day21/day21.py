from collections import defaultdict

lines = open("day21/food.txt",'r').read().split('\n')

recipes = []
allergenInRecipe = defaultdict(list)
ingredientsWithAllergens = defaultdict(set)

#Parse input to dictionaries
for idx, line in enumerate(lines):
    ingredients, allergens = line[:-1].split(' (contains ')
    ingredients = set(ingredients.split())
    allergens   = set(allergens.split(', '))
    recipes.append(ingredients)

    for a in allergens:
        allergenInRecipe[a].append(idx)

    for ingr in ingredients:
            ingredientsWithAllergens[ingr] |= allergens


#Walk trough the list ans find out which ingredient does not have an allergen
ingredientsWithNoAllergen = []

for ingr, allergens in ingredientsWithAllergens.items():
    notPossible = set()

    for aller in allergens:
        for i in allergenInRecipe[aller]:
            if ingr not in recipes[i]:
                notPossible.add(aller)
                break

    
    notAllergen = []

    for a in allergens:
        if a not in notPossible:
            notAllergen.append(a)


    if not notAllergen:
        ingredientsWithNoAllergen.append(ingr)


total = 0
for ingr in ingredientsWithNoAllergen:
    total += sum(ingr in r for r in recipes)


print('The answer of part 1 is ' + str(total))

#Remove inert ingredients
ingredientsNew = ingredientsWithAllergens.copy()
for ingredient in ingredientsWithAllergens:
    if ingredient in ingredientsWithNoAllergen:
        del ingredientsNew[ingredient]

assigned = {}

while len(ingredientsNew) > 0:
    for ingredient, allergens in ingredientsNew.items():
        if len(allergens) == 1:
            break

    allergen = allergens.pop()
    assigned[allergen] = ingredient
    del ingredientsNew[ingredient]

    for ingredient, allergens in ingredientsNew.items():
        if allergen in allergens:
            allergens.remove(allergen)

print("The answer for part 2 is " + ','.join(map(assigned.get, sorted(assigned))))

print("Klaar")



d = {}
ingredients = []
lines = open("day21/food.txt",'r').read().split('\n')
for line in lines:
    line = line.strip().rstrip(')')
    ingred, aller = line.split('(')
    aller = aller.split()
    ingredients.append(ingred)
    for a in aller[1:]:
        a = a.rstrip(',')
        if a not in d:
            d[a] = set(ingred.split())
        else:
            d[a] = d[a].intersection(set(ingred.split()))

search = True
allergens = []
while search:
    search = False
    for k,v in d.items():
        if len(v) == 1:
            val = v.pop()
            d[k] = set()
            d[k].add(val)
            allergens.append(val)
            for k_ in d.keys():
                if val in d[k_] and k_ != k:
                    search = True
                    d[k_].remove(val)

total = 0
for i in ingredients:
   L = i.split()
   for l in L:
       if l not in allergens:
           total += 1
print(total)

pt2 = sorted(d.items(), key=lambda x: x[0])
s = ''
for t in pt2:
    s += t[1].pop() + ','
print(s.rstrip(','))

