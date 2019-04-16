import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g
from glob2 import glob
import pandas as pd
from datetime import datetime


def flugwinkel(x, t):
    return np.arctan(t**2*g/(2*x))


def startGeschwindigkeit(x, alpha):
    return np.sqrt(x*g/(np.sin(2*alpha)))


def flughöhe(v, alpha, t):
    return v*np.sin(alpha)*t/2 - g*t**2/8


def DataBase():
    df = pd.DataFrame()
    paths = glob("data/*.csv")
    for path in paths:
        print(f"Loading data from {path}")
        df = pd.concat(
            [df, pd.read_csv(path, encoding="utf-8-sig")], ignore_index=True)

    df["Datum"] = df.apply(
        lambda x: datetime.fromisoformat(x["Datum"]), axis=1)
    df["Winkel"] = df.apply(lambda x: flugwinkel(
        x["Weite"], x["Zeit"]), axis=1)
    df["v0"] = df.apply(lambda x: startGeschwindigkeit(
        x["Weite"], x["Winkel"]), axis=1)
    df["Höhe"] = df.apply(lambda x: flughöhe(
        x["v0"], x["Winkel"], x["Zeit"]), axis=1)

    print(f"{df.shape[0]} entrys found")
    return df
