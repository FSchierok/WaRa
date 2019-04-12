import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g


def flugwinkel(x, t):
    return np.arctan(t**2*g/(2*x))


def startGeschwindigkeit(x, alpha):
    return np.sqrt(x*g/(np.sin(2*alpha)))


def flughöhe(v, alpha, t):
    return v*np.sin(alpha)*t/2 - g*t**2/8


def flugparabel():
    pass


data = np.genfromtxt("data/2019-04-12.txt", unpack=True)

alpha = flugwinkel(data[2], data[3])
v0 = startGeschwindigkeit(data[2], alpha)
ymax = flughöhe(v0, alpha, data[3])
