input = open('input', 'r').read().split(',')
listOfFish = input
daysToSimulate = 80

for day in range (0, daysToSimulate):
    newFishes = 0
    for i in range(len(listOfFish)):
        listOfFish[i] = int(listOfFish[i]) - 1
        if listOfFish[i] == -1:
            listOfFish[i] = 6
            newFishes = newFishes +1

    newFishes = [8] * newFishes
    listOfFish.extend(newFishes)

    print("Day " + str(day+1) + ": " + str(len(listOfFish)) + " fishes")
