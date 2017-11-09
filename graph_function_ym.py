import matplotlib.pyplot as plt
import numpy as np

filedirectory = 'GOOG.csv'
def get_data(x):
    return data = np.genfromtxt(x)

def graph(x,filename):
    """ this function will plot the graph using mapplotlib package"""
    plt.scatter(x[:, 0], x[:, -1])
    #plt.xlim((-1, 5))
    #plt.ylim((-1, 5))
    plt.axis("equal")
    plt.savefig(filename)
    plt.show(filename)
    plt.close()

get_data(filedirectory)
graph(data,test.jpg)
