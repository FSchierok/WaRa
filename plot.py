import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.constants import g
from database import DataBase


def flugparabel(t, alpha, v0):
    x = v0*np.cos(alpha)*t
    y = v0*np.sin(alpha)*t-(g/2)*t**2
    return x, y


df = DataBase()
fig = plt.figure(1)
for index, flug in df.iterrows():

    plt.plot(*flugparabel(np.linspace(0, flug["Zeit"], 200),
                          flug["Winkel"], flug["v0"]), label=index)
plt.xlabel(r"Weite/$m$")
plt.ylabel(r"Höhe/$m$")
plt.legend()
# plt.show()
# plt.savefig("2019-04-12.svg")
plt.clf()
ax = fig.add_subplot(111, projection='3d')
ax.plot(df["Druck"], df["Wasser"], np.sqrt(
    df["Weite"]**2/4+df["Höhe"]**2), ".")
ax.set_xlabel("Druck")
ax.set_ylabel("Wasser")
ax.set_zlabel("Abstand")
plt.show()
