input = open('input','r').read().split('\n')
charCount = len(input[0])

oxygenGeneratorRating=input
for i in range(charCount):
    intDistribution=0
    for line in oxygenGeneratorRating:
        if int(line[i]) == 1:
            intDistribution += 1
        elif int(line[i]) == 0:
            intDistribution -= 1
    if intDistribution >= 0:
        oxygenGeneratorRating = [ x for x in oxygenGeneratorRating if x[i] == "1"]
    else:
        oxygenGeneratorRating = [ x for x in oxygenGeneratorRating if x[i] == "0"]
    if len(oxygenGeneratorRating) == 1:
        break

co2ScrubberRating=input
for i in range(charCount):
    intDistribution=0
    for line in co2ScrubberRating:
        if int(line[i]) == 1:
            intDistribution += 1
        elif int(line[i]) == 0:
            intDistribution -= 1
    if intDistribution >= 0:
        co2ScrubberRating = [x for x in co2ScrubberRating if x[i] == "0"]
    else:
        co2ScrubberRating = [x for x in co2ScrubberRating if x[i] == "1"]
    if len(co2ScrubberRating) == 1:
        break

liveSupportRating = int(oxygenGeneratorRating[0], 2) * int(co2ScrubberRating[0], 2)
print(liveSupportRating)

