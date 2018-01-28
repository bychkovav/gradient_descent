import simpleGD as simple
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Gradient descent will be performed for Rosenbrock function: (a-x)**2+ b(y-x**2)**2
history = simple.process(100, 0.00001, -3, -3, 1, 100)

X = np.arange(-3, 3, 0.1)
Y = np.arange(-3, 3, 0.1)

xx, yy = np.meshgrid(X, Y)

ax = plt.axes(projection='3d')

surf = ax.plot_surface(xx, yy, simple.get_f(xx, yy, 1, 100), cmap=cm.coolwarm,
                       linewidth=3, antialiased=False)

ax.plot3D([w[0] for w in history], [w[1] for w in history], [w[2] for w in history], '-ok',color='red')

# Customize the z axis.


# ax.plot3D([w[0] for w in history], [w[1] for w in history], [w[2] for w in history])
plt.show()
# print(res)
