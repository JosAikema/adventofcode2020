import math

modules = open("2019/day1/input.txt",'r').read().split('\n')

def getFuel(mass):
    if mass <= 0:
        return 0
    else:
        fuel = max(math.floor(mass/3) - 2,0)
        extra_fuel = getFuel(fuel)
        fuel = fuel + extra_fuel
        return fuel

def getFuelTotal(modules):
    total = 0
    for module in modules:
        print("Module mass: " + module)
        
        fuel = getFuel(int(module))
        print("Fuel needed: " + str(fuel))
        total += fuel
    return total

total = 0
for module in modules:
    total = total + math.floor(int(module) / 3) - 2

print("Total needed: " + str(total))
print("==========")
totalInclFuel = getFuelTotal(modules)

print("Total (incl fuel) needed: " + str(totalInclFuel))