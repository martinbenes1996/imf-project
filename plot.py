from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

class Negator:
    @staticmethod
    def standard(x):
        return 1-x
    def godel(x):
        return np.array( [1 if i == 0 else 0 for i in x] )

class Implicator:
    @staticmethod
    def maximum(x, y, negator=Negator.standard):
        return np.maximum(negator(x), y)
    @staticmethod
    def probsum(x,y, negator=Negator.standard):
        return negator(x) + y - negator(x)*y

def plotMaximum(x,y, negator=Negator.standard):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = Implicator.maximum(X, Y, negator)
    ax.contour3D(y, x, z, 70, cmap='plasma')
    ax.set_xlabel('y')
    ax.set_ylabel('x')
    ax.set_zlabel('z')
    fig.show()

def plotProbsum(x,y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = Implicator.probsum(X,Y)
    ax.contour3D(y, x, z, 70, cmap='plasma')
    ax.set_xlabel('y')
    ax.set_ylabel('x')
    ax.set_zlabel('z')
    fig.show()

if __name__=="__main__":
    x = np.linspace(0, 1, 1000)
    y = np.linspace(0, 1, 1000)
    X, Y = np.meshgrid(x, y)
    
    plotMaximum(X,Y)