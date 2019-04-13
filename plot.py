import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from scipy.constants import g


def flugwinkel(x, t):
    return np.arctan(t**2*g/(2*x))


def startGeschwindigkeit(x, alpha):
    return np.sqrt(x*g/(np.sin(2*alpha)))


def flughöhe(v, alpha, t):
    return v*np.sin(alpha)*t/2 - g*t**2/8


def flugparabel(t, alpha, v0):
    x = v0*np.cos(alpha)*t
    y = v0*np.sin(alpha)*t-(g/2)*t**2
    return x, y


data = np.genfromtxt("data/2019-04-12.txt", unpack=True)

alpha = flugwinkel(data[2], data[3])
v0 = startGeschwindigkeit(data[2], alpha)
ymax = flughöhe(v0, alpha, data[3])

fig = plt.figure(1)

for flug in range(len(v0)):
    t_plot = np.linspace(0, data[3][flug], 1000)
    plt.plot(*flugparabel(t_plot, alpha[flug],
                          v0[flug]), label=f"Flug {flug}")

plt.xlabel(r"Weite/$m$")
plt.ylabel(r"Höhe/$m$")
plt.legend()
# plt.show()
# plt.savefig("2019-04-12.png")
