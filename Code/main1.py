from Code.graph import graph
patterns = []
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

#x between -3 and 3
#y between -2 and 2
def normalize():
    for pattern in patterns:
        pattern[0] = ((pattern[0] + 3)/(6))
        pattern[1] = ((pattern[1] + 2) / 4)


readFile()
#removes empty lists
print(patterns)
normalize()
print(patterns)