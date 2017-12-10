import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.mlab as mlab
train = []
test = []
trainDic = {}
info = []
accuracy = [0, 0]
def readFile():
    with open("../Data/Ex2_train.txt") as data:
        lines = data.read().split('\n')[1:]
        for line in lines:
            pattern = []
            tokens = line.split(',')

            try:
                pattern.append(float(tokens[0]))
                pattern.append(int(tokens[1]))
            except:
                print(tokens)
            if len(pattern) == 0:
                print("no pattern found")
            else:
                train.append(pattern)
    with open("../Data/Ex2_test.txt") as data:
        lines = data.read().split('\n')[1:]
        for line in lines:
            pattern = []
            tokens = line.split(',')

            try:
                pattern.append(float(tokens[0]))
                pattern.append(float(tokens[1]))
            except:
                print(tokens)
            if len(pattern) == 0:
                print("no pattern found")
            else:
                test.append(pattern)

def splitDataByClass():
    trainDic[1] = []
    trainDic[2] = []
    trainDic[3] = []
    for t in train:
        trainDic[t[1]].append(t[0])

def getInfo():
    for key in trainDic:
        information = []
        information.append(np.mean(trainDic[key]))
        information.append(np.std(trainDic[key]))
        info.append(information)

def graphDistro():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    sigma = math.sqrt(info[0][1])
    x = np.linspace(info[0][0]- 3* sigma, info[0][0] + 3 * sigma, 100)
    ax1.plot(x,mlab.normpdf(x,info[0][0], sigma), c='b', label='class 1')
    sigma1 = math.sqrt(info[1][1])
    x1 = np.linspace(info[1][1]-3*sigma1, info[1][0]+3*sigma, 100)
    ax1.plot(x1, mlab.normpdf(x1,info[1][0], sigma1), c='r', label='class 2')
    sigma2 = math.sqrt(info[2][1])
    x2 = np.linspace(info[2][1]-3*sigma2, info[2][0]+3*sigma2, 100)
    ax1.plot(x2,mlab.normpdf(x2, info[2][0], sigma2), c='g', label='class 3')
    plt.legend(loc='upper left')
    plt.show()

def testAccuracy():
    for pattern in test:
        results = []
        for x in range(3):
            top = math.exp(-(math.pow(pattern[0]-info[x][0],2)/(2*math.pow(info[x][1],2))))
            bottom = 1/(math.sqrt(2*math.pi) * info[x][1])
            results.append(top * bottom)
        print(results)
        print(pattern[1])
        best = results.index(max(results))
        if best + 1 == pattern[1]:
            accuracy[0] += 1
        else:
            accuracy[1] += 1



readFile()
splitDataByClass()
getInfo()
graphDistro()
testAccuracy()
print(accuracy)