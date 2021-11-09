# gráficos gerados a partir do numpy
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D


class Figdsa:
    def plotar(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 2, 1)
        ax1.plot(np.random.randn(50), color='red')

        ax2 = fig.add_subplot(1, 2, 2)
        ax2.scatter(np.arange(50), np.random.randn(50))
        return plt.show()


if __name__ == '__main__':
    fig = Fig()
    fig.plotar()
