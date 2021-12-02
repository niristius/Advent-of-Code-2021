import pandas as pd
values = pd.read_csv('input', header=None, names=['value'])
values['Moving Average'] = values['value'].rolling(window=3).mean()
PreviousValue=AmoutOfIncreases=0
for mean in values['Moving Average']:
    CurrentValue = mean
    if CurrentValue > PreviousValue:
        AmoutOfIncreases = AmoutOfIncreases +1
    PreviousValue = CurrentValue
print(AmoutOfIncreases)