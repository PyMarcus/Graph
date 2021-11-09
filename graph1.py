# matplotlib é a biblioteca mais utilizada para  a construção de gráficos com python
# matplotlib faz parte da etapa de visualização dos dados Dashboard & visualization
# para gráficos, menos é mais.
# definindo o eixo do gráfico
# plt.plot([1, 3, 5], [2, 4, 7])   # plot cria um gráfico simples
# plt.show()
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *

print(mpl.__version__)


class PlotGraphSimple:
    def __init__(self, x, y):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        plt.plot(self.x, self.y)

    def plota_x(self):
        """
        plota eixo x
        :return:
        """
        plt.xlabel('Variável 1')

    def plota_y(self):
        """
        plota eixo y
        :return:
        """
        plt.ylabel('Variável 2')

    def titulo(self):
        """
        define o título
        :return:
        """
        plt.title('Teste Plot')

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()


class GraphBar:
    def __init__(self, x, y):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        plt.bar(self.x, self.y, label = 'Barras', color = 'r') # r = red, label = legenda

    def plota_(self):
        """"""
        plt.legend()

    def titulo(self):
        """
        define o título
        :return:
        """
        plt.title('Teste Plot')

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()


class GraphBar2:
    def __init__(self, x, y):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        plt.bar(self.x, self.y, label = 'Barras', color = 'r') # r = red, label = legenda

    def plota_(self):
        """"""
        plt.legend()

    def titulo(self):
        """
        define o título
        :return:
        """
        plt.title('Teste Plot')

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()


class Histograma:
    def __init__(self, x, y):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        plt.hist(self.x, self.y, histtype='stepfilled', rwidth=0.9) # r = red, label = legenda

    def plota_(self):
        """"""
        plt.legend()

    def titulo(self):
        """
        define o título
        :return:
        """
        plt.title('Teste Plot')

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()


class Point:
    def __init__(self, x, y):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.x = x
        self.y = y
        plt.scatter(self.x, self.y, label = 'Pontos', color = 'r', marker = 'o', s = 100) # r = red, label = legenda

    def plota_(self):
        """"""
        plt.legend()

    def titulo(self):
        """
        define o título
        :return:
        """
        plt.title('Teste Plot')

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()


class StackPlot:
    def __init__(self, dias, dormir, comer, trabalhar, passear):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.dia = dias
        self.dormir = dormir
        self.comer = comer
        self.trabalhar = trabalhar
        self.passear = passear
        plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m', 'c', 'r', 'k', 'b']) # r = red, label = legenda

    def plota_(self):
        """"""
        pass

    def titulo(self):
        """
        define o título
        :return:
        """
        pass

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()

class Pizza:
    def __init__(self, fatias, labels, colors, starangle, shadow):
        """
        Plota o gráfico com base nas listas passadas x e y
        :param x:
        :param y:
        """
        self.fatias = fatias
        self.labels = labels
        self.colors = colors
        self.starangle = starangle
        self.shadow = shadow
        plt.pie(self.fatias, labels= self.labels, colors= self.colors, startangle=self.starangle, shadow= self.shadow) # r = red, label = legenda

    def plota_(self):
        """"""
        pass

    def titulo(self):
        """
        define o título
        :return:
        """
        pass

    def exibe(self):
        """
        Exibe o gráfico
        :return:
        """
        plt.show()


class PyLab:
    def __init__(self, x):
        self.x = x

    def geraGrafico(self):
        y = self.x ** 2
        fig = plt.figure()
        # eixos
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.plot(self.x, y, 'r')
        axes.set_xlabel('x')
        axes.set_ylabel('y')
        axes.set_title('gráfico de linha')
        



class PyLab2:
    def __init__(self, x):
        self.x = x

    def geraGrafico2(self):
        y = self.x ** 2
        fig = plt.figure()
        # eixos
        axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

        # figura principal
        axes1.plot(self.x, y, 'r')
        axes1.set_xlabel('x')
        axes1.set_ylabel('y')
        axes1.set_title('Principal')

        # figura secundária
        axes2.plot(y, self.x, 'g')
        axes2.set_xlabel('y')
        axes2.set_ylabel('x')
        axes2.set_title('Secundário')



if __name__ == '__main__':
    x = [1, 4, 5]
    y = [3, 7, 2]
    # gráfico simples, ou ploat
    grafico = PlotGraphSimple(x, y)
    grafico.plota_x()
    grafico.plota_y()
    grafico.titulo()
    grafico.exibe()

    # gráfico de barras
    barras = GraphBar(x, y)
    barras.titulo()
    barras.plota_()
    barras.exibe()

    # Outro gráfico de barras
    z = [x for x in range(20)]
    p = [z for z in range(20)]
    barras = GraphBar2(z, p)
    barras.titulo()
    barras.plota_()
    barras.exibe()

    # histograma
    histo = Histograma(z, p)
    histo.titulo()
    histo.plota_()
    histo.exibe()

    # graficos de pontos
    pontos = Point(z, p)
    pontos.titulo()
    pontos.plota_()
    pontos.exibe()

    # gráfico de área
    dias = [x for x in range(1, 6)]
    dormir = [x for x in range(1, 6)]
    comer = [x for x in range(1, 6)]
    trabalhar = [x for x in range(1, 6)]
    passear = [x for x in range(1, 6)]
    grafico = StackPlot(dias, dormir, comer, trabalhar, passear)
    grafico.exibe()

    # gráfico de pizza
    fatias = [x for x in range(7, 13)]
    atividades = ['dormir', 'comer', 'trabalhar', 'passear', 'cantar', 'camsad']
    colunas = ['c', 'm', 'r', 'k', 'b']
    graf = Pizza(fatias, atividades, colunas,90,True)
    graf.exibe()


    # pylab
    #junção do matplotlib com o numpy
    x = linspace(0, 5, 10)
    pylabb = PyLab(x)
    pylabb.geraGrafico()


    # gráficos de duas figuras
    pylabb2 = PyLab2(x)
    pylabb2.geraGrafico2()