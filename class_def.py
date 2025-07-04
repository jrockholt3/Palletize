import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d


class box:
    def __init__(self, c1=(0,0), c2=(1,1), L=1, W=1):
        self.c1 = c1
        self.c2 = c2
        self.L = L
        self.W = W


class ConeSurface:
    def __init__(self, a=-1,b=1,c=-1,d=1,e=100):
        self.a = np.double(a)
        self.b = np.double(b)
        self.c = np.double(c)
        self.d = np.double(d)
        self.e = np.double(e)

    def get_z(self, x:np.double, y:np.double):
        #z = self.a*x**2 + self.b*x + self.c*y**2 + self.d*y + self.e
        z = self.a*x**2 + self.c*y**2 + self.e
        return z
    
    def get_grad(self, x:np.double, y:np.double):
        pzpx = 2*self.a*x
        pzpy = 2*self.c*y
        return np.array([pzpx, pzpy])
    
    def make_plot(self):
        x_base = []
        y_base = []
        xx = np.zeros((201,201))
        yy = np.zeros((201,201))
        zz = np.zeros((201,201))

        val = -100
        for i in range(201):
            x_base.append(val)
            y_base.append(val)
            val += 1
        print(x_base)
        for i,x in enumerate(x_base):
            for j,y in enumerate(y_base):
                xx[i,j] = x
                yy[i,j] = y
                zz[i,j] = self.get_z(x,y)

        ax = plt.figure().add_subplot(projection='3d')
        ax.plot_surface(xx,yy,zz)
        plt.show()



cone = ConeSurface()
cone.make_plot()







