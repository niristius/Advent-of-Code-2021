input = open('input', 'r').read().split(',')

HighestCrab = 0
for crab in input:
    if HighestCrab < int(crab):
        HighestCrab = int(crab)

MostEfficientHeight=MostEfficentFuelUsage=0
for i in range(HighestCrab):
    FuelRequired = 0
    for crab in input:
        CrabFuelNeed = 0
        for step in range(abs(i-int(crab))):
            CrabFuelNeed = CrabFuelNeed + step + 1
        FuelRequired = FuelRequired + CrabFuelNeed

    if FuelRequired < MostEfficentFuelUsage or MostEfficentFuelUsage == 0:
        MostEfficentFuelUsage = FuelRequired
        MostEfficientHeight = i + 1
    print(str(i+1) + ", " + str(MostEfficentFuelUsage))

print("Most efficient Height: " + str(MostEfficientHeight))
print("With a Fuel Usage of: " + str(MostEfficentFuelUsage))