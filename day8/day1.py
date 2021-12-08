input = open('input', 'r').read().split('\n')

SimpleDigitAmount=0
for line in input:
    CurrentSignalCollection = line.split('|')[1].split()
    for signal in CurrentSignalCollection:
        if len(signal) in (2, 3, 4, 7):
            SimpleDigitAmount+=1

print(SimpleDigitAmount)