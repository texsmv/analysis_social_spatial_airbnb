from keras.layers import Input, Dense
from keras.models import Model
import pandas as pd
from utils_analysis import normalize_dataframe2
from math import ceil
import numpy as np
from keras.models import load_model

#-------------------- change this ------------------------
# laten_dim = 15
# laten_dim = 10
# laten_dim = 3
laten_dim = 5
#--------------------------------------------------------

df_coordenadas = pd.read_csv("caracteristicas_coord.csv")


data = pd.read_csv("caracteristicas.csv")
data = data.drop(data.columns[0], axis = 1)
data = data.drop(labels=['id'], axis=1)
data = data.to_numpy()

autoencoder = load_model("autoencoder"+ str(laten_dim) + ".h5")
encoder = load_model("encoder"+ str(laten_dim) + ".h5")
decoder = load_model("decoder"+ str(laten_dim) + ".h5")



def encode(x):
    return encoder.predict(np.array([x]))[0]

def decode(x):
    return decoder.predict(np.array([x]))[0]

def encode_batch(x):
    return encoder.predict(x)

def decode_batch(x):
    return decoder.predict(x)
 

encoded_data = encode_batch(data)

df_encoded_data = pd.DataFrame(encoded_data)

print(df_encoded_data.shape)
print(df_coordenadas.shape)
df_encoded_data["latitude"] = df_coordenadas["latitude"].values
df_encoded_data["longitude"] = df_coordenadas["longitude"].values
encoded_data_with_coord = df_encoded_dara.to_numpy()

print(encoded_data )


import pickle
 
pickle_file = open('todo2.pk', 'wb')
pickle.dump(encoded_data, pickle_file)

pickle_file = open('todo3.pk', 'wb')
pickle.dump(encoded_data_with_coord, pickle_file)

print("--------------------------")
print("Model loaded succesfully")
print("--------------------------")

