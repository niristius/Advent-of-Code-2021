import pandas as pd
values = pd.read_csv('input', sep=" ", header=None, names=['direction', 'value'])
HorizontalPos=VerticalPos=CurrentAim=0
for index, row in values.iterrows():
    if row['direction'] == "forward":
        HorizontalPos = HorizontalPos + row['value']
        VerticalPos = VerticalPos + ( CurrentAim * row['value'])
    if row['direction'] == "down":
        CurrentAim = CurrentAim + row['value']
    if row['direction'] == "up":
        CurrentAim = CurrentAim - row['value']
print("Horizontal: " + str(HorizontalPos) + ", Vertical: " + str(VerticalPos) + ", Position: " + str(HorizontalPos * VerticalPos))