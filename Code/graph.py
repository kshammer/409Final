import matplotlib.pyplot as plt
def graph(data):
    x = []
    y = []
    for d in data:
        x.append(d[0])
        y.append(d[1])
    plt.scatter(x,y)
    plt.show()