input = open('input', 'r').read().split(',')

HighestCrab = 0
for crab in input:
    if HighestCrab < int(crab):
        HighestCrab = int(crab)

MostEfficientHeight=MostEfficentFuelUsage=0
for i in range(HighestCrab):
    FuelRequired = 0
    for crab in input:
        CrabFuelNeed = abs(i-int(crab))
        FuelRequired = FuelRequired + CrabFuelNeed

    if FuelRequired < MostEfficentFuelUsage or MostEfficentFuelUsage == 0:
        MostEfficentFuelUsage = FuelRequired
        MostEfficientHeight = i

print("Most efficient Height: " + str(MostEfficientHeight))
print("With a Fuel Usage of: " + str(MostEfficentFuelUsage))

