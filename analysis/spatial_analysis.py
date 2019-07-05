import numpy as np
import pandas as pd
from haversine import haversine
import concurrent.futures
import time
from joblib import Parallel, delayed
import multiprocessing
import pickle

pos = 0

# TODO : change max by min
def min_distance_coor_km(id, lat, lon, coordinates_m, umbral):
    global pos
    print(pos)
    pos = pos + 1
    coord = (lat, lon)
    sorted_dists = np.array([haversine(coord, (e[0], e[1])) for e in coordinates_m])
    sorted_dists.sort()
    i = 0
    coeff = 0
    while(True):
        if sorted_dists[i] > umbral:
            break
        coeff = coeff + ((umbral - sorted_dists[i]) / umbral)
        i = i + 1
    # print(coord)
    return [id, sorted_dists[0] , coeff]


# nombre = "paris-attraction.csv"
nombre = "paris-poi.csv"

coord_airbnbs_df = pd.read_csv("caracteristicas_coord.csv")
coord_airbnbs_df = coord_airbnbs_df[["id","latitude", "longitude"]]
print(coord_airbnbs_df.dtypes)

coord_tourist_attractions_df = pd.read_csv(nombre)
# print(coord_tourist_attractions_df.dtypes)
coord_tourist_attractions_df = coord_tourist_attractions_df[["lat", "lng"]]

coord_airbnbs_m = coord_airbnbs_df.to_numpy()
coord_tourist_attractions_m = coord_tourist_attractions_df.to_numpy()

def get_matrix_dists(coord_airbnbs_m, coord_tourist_attractions_m):
    n = len(coord_airbnbs_m)
    dists = np.zeros(n)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(n):
            print(i)
            dists[i] = min_distance_coor_km(coord_airbnbs_m[i][1], coord_airbnbs_m[i][2], coord_tourist_attractions_m)
    return dists

# start = time.time()
# print(min_distance_coor_km(coord_airbnbs_m[0][0],coord_airbnbs_m[0][1], coord_airbnbs_m[0][2], coord_tourist_attractions_m, 1))
# end = time.time()
# print(end - start)

umbral = 1
min_distances_coord = np.array([ min_distance_coor_km(e[0],e[1], e[2], coord_tourist_attractions_m, umbral) for e in coord_airbnbs_m])
results_df = pd.DataFrame(min_distances_coord)
results_df = results_df.drop(results_df.columns[0], axis = 1)
results_df.to_csv("poi_dists_min.csv")


# num_cores = multiprocessing.cpu_count()
# get_matrix_dists(coord_airbnbs_m, coord_tourist_attractions_m)

# n = len(coord_airbnbs_m)

# results = Parallel(n_jobs=num_cores)(delayed(min_distance_coor_km)(coord_airbnbs_m[i][1], coord_airbnbs_m[i][2], coord_tourist_attractions_m) for i in range(n))

