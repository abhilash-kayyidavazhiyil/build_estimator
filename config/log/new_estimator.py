import csv
import math

graph1 = []
graph2 = []


with open("Graph1.txt") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None) # skip the headers
    for row in csv_reader:
        graph1.append(float(row[1]))


with open("Graph2.txt") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None) # skip the headers
    for row in csv_reader:
        graph2.append(float(row[1]))

mean_graph1 = sum(graph1)/len(graph1)
mean_graph2 = sum(graph2)/len(graph2)

std1 = 0
for i in graph1:
    std1 = std1 + (i - mean_graph1)**2

std2 = 0
for i in graph2:
    std2 = std2 + (i - mean_graph2)**2

std_deviation_graph1 = math.sqrt(std1/len(graph1))

std_deviation_graph2 = math.sqrt(std2/len(graph2))


print("graph1 std deviation", std_deviation_graph1)
print("graph2 std deviation", std_deviation_graph2)


