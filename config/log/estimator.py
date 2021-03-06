import csv
import sys
import math

with open("Graph2.txt") as f:
    reader = csv.reader(f)
    vals = []
    for row in reader:
        vals.append(row[1])
    vals = [float(i) for i in vals[1:]]
mean = float(sum(vals)/len(vals))

s=0
for i in vals:
    s = s + (i - mean)**2

print(math.sqrt(s/len(vals)))

# graph 1 - 0.706559393950126
# graph 2 - 0.49296059129345754