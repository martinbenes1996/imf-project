
"""
This module demonstrates fuzzy implication forms.
For educational purposes.
@author Martin Benes
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# generated space of plots
Xdata, Ydata = np.meshgrid(np.linspace(0, 1, 50, endpoint=True), np.linspace(0, 1, 50, endpoint=True))


class Negator:
    """
    Negator class. Not instanciable.
    """
    def __init__(self, *args, **kwargs):
        """ Can not be constructed. """
        raise NotImplementedError

    @staticmethod
    def standard(x):
        """
        Standard negator.
        @param Scalar or numpy array.
        """
        return 1-x

    @classmethod
    def godel(cls, x):
        """
        Gödel negator, implemented recursively.
        @param Scalar or numpy array.
        """
        # scalar - final conditions
        if isinstance(x, float) or isinstance(x, int):
            if x == 0: return 1
            else: return 0
        # vector
        l = []
        for i in x:
            l.append( cls.godel(i) )
        return np.array(l)

    @classmethod
    def dualgodel(cls, x):
        """
        Dual Gödel negator, implemented recursively.
        @param Scalar or numpy array.
        """
        # scalar - final conditions
        if isinstance(x, float) or isinstance(x, int):
            if x == 1: return 0
            else: return 1
        # vector
        l = []
        for i in x:
            l.append( cls.dualgodel(i) )
        return np.array(l)
    
    sugencoef = 2 # sugen coefficient
    @classmethod
    def setSugenCoef(cls, val):
        """ Sugen coefficient setter. """
        cls.sugencoef = val

    yagercoef = 2 # yager coefficient
    @classmethod
    def setYagerCoef(cls, val):
        """ Yager coefficient setter. """
        cls.yagercoef = val

    @classmethod
    def sugen(cls, x):
        """
        Sugen negator.
        @param Scalar or numpy array.
        """
        return (1 - x)/(1 + cls.sugencoef*x)

    @classmethod
    def yager(cls, x):
        """
        Yager negator.
        @param Scalar or numpy array.
        """
        return (1 - x**cls.yagercoef)**(1/cls.yagercoef)
    
    @staticmethod
    def circle(x):
        """
        Circle negator.
        @param Scalar or numpy array.
        """
        return np.sqrt(1 - np.square(x))

    @staticmethod
    def parabolic(x):
        """
        Parabolic negator.
        @param Scalar or numpy array.
        """
        return 1 - np.square(x)
    

class Implicator:
    """
    Implicator class. Not instanciable.
    """
    def __init__(self, *args, **kwargs):
        """ Can not be constructed. """
        raise NotImplementedError

    @staticmethod
    def maximum(x,y, negator=Negator.standard):
        """
        Maximum conorm.
        """
        return np.maximum(negator(x), y)
    
    @staticmethod
    def probsum(x,y, negator=Negator.standard):
        """
        (Reichenbach) Probability sum conorm.
        """
        return negator(x) + y - negator(x)*y
    @staticmethod
    def drastic(x,y, negator=Negator.standard):
        """
        Drastic conorm.
        """
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
        """
        Lukasiewicz conorm.
        """
        return np.minimum(negator(x)+y, 1)
        

def plotImplication(implicator=Implicator.maximum, negator=Negator.standard):
    """
    Implication plotter (3D).
    """
    # create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # count results
    Zdata = implicator(Xdata, Ydata, negator)
    # plot
    ax.plot_surface(Xdata, Ydata, Zdata, cmap='plasma')
    # set axis
    plt.axis([Xdata.max(), Xdata.min(), Ydata.min(), Ydata.max()])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # show
    fig.show()

def plotClassicImplication():
    """
    Classic implication plotter (2D).
    """
    # create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # prepare data
    x = np.array([1,1,0,0])
    y = np.array([1,0,1,0])
    z = np.array([1,0,1,1])
    # plot
    ax.scatter(x,y,z)
    # set axis
    plt.axis([x.max(), x.min(), y.min(), y.max()])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # show
    fig.show()

def plotNegator(negator=Negator.standard):
    """
    Negator plotter (2D).
    """
    # create figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # prepare data, count results
    x = np.linspace(0, 1, 50, endpoint=True)
    y = negator(x)
    # set axis
    ax.plot(x, y, color='magenta')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # show
    fig.show()

print("\033[1;33mWelcome to ImplyPlot!\033[0m")
print("\033[0;36mplotImplication(Implicator.\033[0;35m<implicator>\033[0;36m, Negator.\033[0;35m<negator>\033[0;36m)\033[0m")
print("\033[0;36mplotNegator(Negator.\033[0;35m<negator>\033[0;36m)\033[0m")
print("\033[0;36mplotClassicImplication()\033[0m")
print("\033[0;35m<implicator>\033[0m: maximum, probsum, drastic, lukasiewicz")
print("\033[0;35m<negator>\033[0m: standard, godel, dualgodel, sugen, yager, circle, parabolic")

