import matplotlib.pyplot as plt
import numpy as np

filedirectory = "GOOG.csv"
data = np.genfromtxt(filedirectory,delimiter=',')

def graph(x,filename):
    """ this function will plot the graph using mapplotlib package"""
    plt.plot(x[:, 1])
    #plt.xlim((-1, 5))
    #plt.ylim((-1, 5))
    plt.axis("equal")
    plt.savefig(filename)
    plt.show(filename)
    plt.close()

graph(data,"test.png")
