from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

Xdata, Ydata = np.meshgrid(np.linspace(0, 1, 50, endpoint=True), np.linspace(0, 1, 50, endpoint=True))

class Negator:
    @staticmethod
    def standard(x):
        return 1-x
    @classmethod
    def godel(cls, x):
        if isinstance(x, float) or isinstance(x, int):
            if x == 0: return 1
            else: return 0
        l = []
        for i in x:
            l.append( cls.godel(i) )
        return np.array(l)
    @classmethod
    def dualgodel(cls, x):
        if isinstance(x, float) or isinstance(x, int):
            if x == 1: return 0
            else: return 1
        l = []
        for i in x:
            l.append( cls.godel(i) )
        return np.array(l)
    sugencoef = 2
    yagercoef = 2
    @classmethod
    def sugen(cls, x):
        return (1 - x)/(1 + cls.sugencoef*x)
    @classmethod
    def yager(cls, x):
        return (1 - x**cls.yagercoef)**(1/cls.yagercoef)
    @classmethod
    def setSugenCoef(cls, val):
        cls.sugencoef = val
    @classmethod
    def setYagerCoef(cls, val):
        cls.yagercoef = val

class Implicator:
    @staticmethod
    def maximum(x,y, negator=Negator.standard):
        return np.maximum(negator(x), y)
    @staticmethod
    def probsum(x,y, negator=Negator.standard):
        return negator(x) + y - negator(x)*y
    @staticmethod
    def drastic(x,y, negator=Negator.standard):
        l = []
        for i,j in zip(negator(x),y):
            k = []
            for m,n in zip(i,j):
                if min(m,n) == 0: k.append(max(m,n))
                else: k.append(1)
            l.append(np.array(k))
        return np.array(l)
    @staticmethod
    def lukasiewicz(x,y, negator=Negator.standard):
        return np.minimum(negator(x)+y, 1)
    @staticmethod
    def reichenbach(x,y, negator=Negator.standard):
        return negator(x) - y + x*y
    @staticmethod
    def wtf(z,y, negator=Negator.standard):
        l = []
        for i,j in zip(x,y):
            k = []
            for m,n in zip(i,j):
                if n==0: k.append( negator(m) )
                elif m==1: k.append( n )
                else: k.append(1)
            l.append(np.array(k))
        return np.array(l)
        return np.minimum(negator(x)+y, 1)
        

def plotImplication(implicator=Implicator.maximum, negator=Negator.standard):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Zdata = implicator(Xdata, Ydata, negator)
    #ax.contour3D(Ydata, Xdata, Zdata, 40, cmap='plasma')
    ax.plot_surface(Xdata, Ydata, Zdata, cmap='plasma')
    plt.axis([Xdata.max(), Xdata.min(), Ydata.min(), Ydata.max()])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    fig.show()

print("\033[1;33mWelcome to ImplyPlot!\033[0m")
print("Type: \033[0;36mplotImplication(Implicator.\033[0;35m<implicator>\033[0;36m, Negator.\033[0;35m<negator>\033[0;36m)\033[0m")
print("\033[0;35m<implicator>\033[0m: maximum, probsum, drastic, reichenbach, lukasiewicz")
print("\033[0;35m<negator>\033[0m: standard, godel, dualgodel, sugen, yager")

