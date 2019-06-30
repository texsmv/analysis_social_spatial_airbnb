from sklearn import preprocessing
import numpy as np
import pandas as pd

# cast percentage to int
def percentage_2_int(x):
    return int(x.strip('%'))


def dolar_2_float(x):
    return float(x.strip('$'))

def get_amenitie(x):
    t = x.strip('{')
    t = t.strip('}')
    t = t.replace('"', '')
    t = t.split(',')
    return t

def normalize_dataframe(df):
    x = df.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled)
    return df


def normalize_dataframe2(df):
    x = df.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled)
    return df, min_max_scaler

def count_amenities(counts, lista, x):
    for e in x:
        indice = lista.index(e)
        counts[indice] = counts[indice] + 1

def has_x(e, lista):
    if e in lista:
        return 1
    return 0
    
