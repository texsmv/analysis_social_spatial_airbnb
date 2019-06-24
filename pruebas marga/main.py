import pandas as pd
import numpy as np
import matplotlib as plt

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D

# %matplotlib inline
plt.rcParams['figure.figsize'] = (16,19)
# plt.style.use('ggplot')