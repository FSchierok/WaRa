import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g
from glob2 import glob
import pandas as pd


def flugwinkel(x, t):
    print(x, t)
    return np.arctan(t**2*g/(2*x))


def startGeschwindigkeit(x, alpha):
    return np.sqrt(x*g/(np.sin(2*alpha)))


def flughöhe(v, alpha, t):
    return v*np.sin(alpha)*t/2 - g*t**2/8


def flugparabel(t, alpha, v0):
    x = v0*np.cos(alpha)*t
    y = v0*np.sin(alpha)*t-(g/2)*t**2
    return x, y


df = pd.DataFrame()
paths = glob("data/*.csv")
for path in paths:
    df = pd.concat([df, pd.read_csv(path, encoding="utf-8-sig")])

df["Winkel"] = df.apply(lambda x: flugwinkel(x["Weite"], x["Zeit"]), axis=1)
df["v0"] = df.apply(lambda x: startGeschwindigkeit(
    x["Weite"], x["Winkel"]), axis=1)
df["Höhe"] = df.apply(lambda x: flughöhe(
    x["v0"], x["Winkel"], x["Zeit"]), axis=1)
