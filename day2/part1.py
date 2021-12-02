import pandas as pd
values = pd.read_csv('input', sep=" ", header=None, names=['direction', 'value'])
HorizontalPos=VerticalPos=0
for index, row in values.iterrows():
    if row['direction'] == "forward":
        HorizontalPos = HorizontalPos + row['value']
    if row['direction'] == "down":
        VerticalPos = VerticalPos + row['value']
    if row['direction'] == "up":
        VerticalPos = VerticalPos - row['value']
print("Horizontal: " + str(HorizontalPos) + ", Vertical: " + str(VerticalPos) + ", Position: " + str(HorizontalPos * VerticalPos))