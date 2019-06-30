from keras.layers import Input, Dense
from keras.models import Model
import pandas as pd
from utils_analysis import normalize_dataframe2
from math import ceil
import numpy as np
from keras.models import load_model


data = pd.read_csv("caracteristicas.csv")
data = data.drop(data.columns[0], axis = 1)
data = data.drop(labels=['id'], axis=1)
data = data.to_numpy()

autoencoder = load_model("autoencoder.h5")
encoder = load_model("encoder.h5")
decoder = load_model("decoder.h5")



def encode(x):
    return encoder.predict(np.array([x]))[0]

def decode(x):
    return decoder.predict(np.array([x]))[0]

def encode_batch(x):
    return encoder.predict(x)

def decode_batch(x):
    return decoder.predict(x)
 

encoded_data = encode_batch(data)
print(encoded_data)


print("--------------------------")
print("Model loaded succesfully")
print("--------------------------")

