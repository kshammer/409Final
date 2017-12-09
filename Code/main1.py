from Code.graph import graph
import math
import random
patterns = []
neurons = []
def readFile():
    with open("../Data/Ex1_data.txt") as data:
        lines = data.read().split('\n')[1:]
        for line in lines:
            pattern = []
            tokens = line.split(',')
            for token in tokens:
                try:
                    pattern.append(float(token))
                except:
                    print("Could not add pattern " + token)
            if len(pattern) == 0:
                print("no pattern found")
            else:
                patterns.append(pattern)

def normalizeData():
    for pattern in patterns:
        normal = (pattern[0] ** 2) + (pattern[1] ** 2)
        normal = math.sqrt(normal)
        pattern[0] = (pattern[0] / normal)
        pattern[1] = (pattern[1] / normal)
def genNeurons(amount):
    for i in range(amount):
        neuron = []
        x = random.uniform(-1, 1)
        neuron.append(x)
        y = random.uniform(-1,1)
        neuron.append(y)
        neurons.append(neuron)
def normalizeNeurons():
    for neuron in neurons:
        normal = (neuron[0] ** 2) + (neuron[1] ** 2)
        normal = math.sqrt(normal)
        neuron[0] = (neuron[0] / normal)
        neuron[1] = (neuron[1] / normal)




readFile()
normalizeData()
graph(patterns)
genNeurons(2)
print(neurons)
