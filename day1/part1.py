import pandas as pd
values = pd.read_csv('lukas_input', header=None, names=['value'])
PreviousValue=values['value'][0]
AmoutOfIncreases=0
for CurrentValue in values['value']:
    if CurrentValue > PreviousValue:
        AmoutOfIncreases = AmoutOfIncreases +1
    PreviousValue = CurrentValue
print(AmoutOfIncreases)




