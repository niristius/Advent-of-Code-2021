from collections import Counter
input = open('input', 'r').read().split('\n')
SumOfCoordinates = []
for coordinates in input:
    X1 = int(coordinates.split()[0].split(',')[0])
    Y1 = int(coordinates.split()[0].split(',')[1])
    X2 = int(coordinates.split()[2].split(',')[0])
    Y2 = int(coordinates.split()[2].split(',')[1])
    if X1 == X2:
        if Y1 < Y2:
            LowY, HiY = Y1, Y2
        else:
            LowY, HiY = Y2, Y1
        for i in range(LowY, HiY+1):
            CurrentCoordinate = []
            CurrentCoordinate.append(X1)
            CurrentCoordinate.append(i)
            SumOfCoordinates.append(CurrentCoordinate)
    elif Y1 == Y2:
        if X1 < X2:
            LowX, HiX = X1, X2
        else:
            LowX, HiX = X2, X1
        for i in range(LowX, HiX+1):
            CurrentCoordinate = []
            CurrentCoordinate.append(i)
            CurrentCoordinate.append(Y1)
            SumOfCoordinates.append(CurrentCoordinate)
print(sum(v>1 for v in Counter(map(tuple, SumOfCoordinates)).values()))