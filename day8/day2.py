from collections import Counter

# Get input
input = open('input', 'r').read().split('\n')

# Map Default Display Values for each Digit
DefaultMapping = {"abcefg": "0", "cf": "1", "acdeg": "2", "acdfg": "3", "bcdf": "4", "abdfg": "5", "abdefg": "6", "acf": "7", "abcdefg": "8", "abcdfg": "9"}

# Create Empty Array to hold final values for each line later
OutputValues = []

# Iterate through the lines
for line in input:

    # Seperate the Reference Digits and the four Output Digits
    ReferenceDigits, OutputDigits = line.split("|")

    # Count Occurences of each Display Segment
    SegOccurence = Counter(ReferenceDigits.replace(" ",""))
    # Since the default Segment e, b, and f have a uniq number of occurences in the References, its easy to find their scrambled counterparts
    key = {x[0]: {4:"e",6:"b",9:"f"}[x[1]]for x in SegOccurence.items() if x[1] in (4,6,9)}

    # So a "1" is displayed with 2 Segments, one of which is already known (f)
    for digit in ReferenceDigits.split():
        if len(digit) == 2:
            key.update({seg: "c" for seg in digit if seg not in key})
    # "7" has just one segment more so easy enough to find the "a" equivalent
    key.update({x[0]: "a" for x in SegOccurence.items() if x[1] == 8 and x[0] not in key})

    # Now 4 will show us "d"
    for digit in ReferenceDigits.split():
        if len(digit) == 4:
            key.update({seg: "d" for seg in digit if seg not in key})

    # And then there's only one segment left
    key.update({x[0]: "g" for x in SegOccurence.items() if x[1] == 7 and x[0] not in key})

    # Decrypt the Four Output Digits
    Decrypted = OutputDigits.translate(str.maketrans(key)).split()

    # Translate them through the Default Mapping to a number, buld the 4 Digit ouput code and append it to the List of output Codes
    OutputValues.append(int("".join([DefaultMapping["".join(sorted(term))] for term in Decrypted])))

# Sum all output codes and output them
print(sum(OutputValues))

