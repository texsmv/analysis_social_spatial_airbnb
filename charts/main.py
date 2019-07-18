import pandas as pd
import numpy as np
data = pd.read_csv('data2km.csv')
numeros = np.array(data['n_airbnbs'])

# print(numeros)

from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

# data = {'score': [234,24,14,27,-74,46,73,-18,59,160]}
df = pd.DataFrame(numeros)
# print(df)

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled)
a = round(df_normalized*10)


data['nor_n_ar'] = a
data['promedio_normalizado'] = round(data['promedio_normalizado'])

data.to_json('data2km.json',orient='index')
print(data)