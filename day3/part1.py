input = open('input','r').read().split('\n')
charCount = len(input[0])
RateValue=[0] * charCount
for line in input:
    for i in range(charCount):
        if int(line[i]) == 1:
            RateValue[i] += 1
        elif int(line[i]) == 0:
            RateValue[i] -= 1
gammaRange=epsilonRange=""
for i in range(charCount):
    if int(RateValue[i]) < 0:
        gammaRange = gammaRange + "0"
        epsilonRange = epsilonRange + "1"
    else:
        gammaRange = gammaRange + "1"
        epsilonRange = epsilonRange + "0"
powerConsumption = int(gammaRange, 2) * int(epsilonRange, 2)
print(powerConsumption)

