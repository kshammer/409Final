import matplotlib.pyplot as plt
import math
import random
patterns = []
neurons = []
alpha = 0.1
orignalNeurons = []

#Reads the file and tokenizes the data
def readFile():
    with open("../Data/Ex1_data.txt") as data:
        lines = data.read().split('\n')[1:]
        for line in lines:
            pattern = []
            tokens = line.split(',')
            for token in tokens:
                try:
                    #makes sure data is correct
                    pattern.append(float(token))
                except:
                    print(token)
            #accounts for empty lines
            if len(pattern) == 0:
                print("no pattern found")
            else:
                patterns.append(pattern)

#does a vector normalization
def normalizeData():
    for pattern in patterns:
        normal = (pattern[0] ** 2) + (pattern[1] ** 2)
        normal = math.sqrt(normal)
        pattern[0] = (pattern[0] / normal)
        pattern[1] = (pattern[1] / normal)

#generates an amount of random neurons
def genRandomNeurons(amount):
    for i in range(amount):
        neuron = []
        neuron2 = []
        x = random.uniform(-1, 1)
        neuron.append(x)
        neuron2.append(x)
        y = random.uniform(-1,1)
        neuron.append(y)
        neuron2.append(y)
        neurons.append(neuron)
        orignalNeurons.append(neuron2)

#normalizes their weights
def normalizeNeurons():
    for neuron in neurons:
        normal = (neuron[0] ** 2) + (neuron[1] ** 2)
        normal = math.sqrt(normal)
        neuron[0] = (neuron[0] / normal)
        neuron[1] = (neuron[1] / normal)
    # used to keep track of the original positions
    for coolNeuron in orignalNeurons:
        normal = (coolNeuron[0] ** 2) + (coolNeuron[1] ** 2)
        normal = math.sqrt(normal)
        coolNeuron[0] = (coolNeuron[0] / normal)
        coolNeuron[1] = (coolNeuron[1] / normal)

#displays the data without any nueurons
def graphData():
    x = []
    y = []
    for pattern in patterns:
        x.append(pattern[0])
        y.append(pattern[1])
    plt.scatter(x,y, s=10, c='b', marker='s', label='patterns')
    plt.legend(loc='upper left')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.ylim([-1.1,1.1])
    plt.xlim([-1.1,1.1])
    plt.show()

#creates a plot with the neurons
def graphNeurons():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    xData = []
    yData = []
    xNeurons = []
    yNeurons = []
    xOG = []
    yOG = []
    for pattern in patterns:
        xData.append(pattern[0])
        yData.append(pattern[1])
    for neuron in neurons:
        xNeurons.append(neuron[0])
        yNeurons.append(neuron[1])
    for neuron1 in orignalNeurons:
        xOG.append(neuron1[0])
        yOG.append(neuron1[1])
    ax1.scatter(xData, yData, s=10, c='b', marker='s', label='patterns')
    ax1.scatter(xNeurons,yNeurons, s=15, c='r', marker='o', label='neurons')
    ax1.scatter(xOG, yOG, s=15, c='g', marker='x', label='originalPosition')
    plt.legend(loc='upper left')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.ylim([-1.1, 1.1])
    plt.xlim([-1.1, 1.1])
    plt.show()

#calculates the net distance between neuron and pattern
def calcNet(x):
    for i in range(x):
        for pattern in patterns:
            total = []

            for neuron in neurons:
                value = 0
                value += pattern[0] * neuron[0]
                value += pattern[1] * neuron[1]
                total.append(value)

            best = total.index(max(total))
            print(best)
            neurons[best][0] = neurons[best][0] + alpha*pattern[0]
            neurons[best][1] = neurons[best][1] + alpha*pattern[1]
            normalizeNeurons()
        graphNeurons()

#creates non random neurons
def genNeurons():
    neuron1 = [1,0]
    neuron2 = [-1,-1]
    neuron3 = [1, 0]
    neuron4 = [-1, -1]
    neurons.append(neuron1)
    neurons.append(neuron2)
    orignalNeurons.append(neuron3)
    orignalNeurons.append(neuron4)



readFile()
normalizeData()
#graphData()
#how many random neurons to generate
genRandomNeurons(3)
#genNeurons()
normalizeNeurons()
graphNeurons()
#the value is how many iterations to run
calcNet(1)
