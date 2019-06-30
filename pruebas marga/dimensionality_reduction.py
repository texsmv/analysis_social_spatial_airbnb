#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import SparsePCA
from sklearn.manifold import MDS
from sklearn.manifold import Isomap#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import SparsePCA
from sklearn.manifold import MDS
from sklearn.manifold import Isomap
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import GaussianRandomProjection
from sklearn.decomposition import FastICA
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.random_projection import SparseRandomProjection
from sklearn import preprocessing
from utils_analysis import normalize_dataframe


# In[4]:


caracteristicas_df = pd.read_csv('caracteristicas.csv')


# In[5]:


# def df_pca(df, n_comp = 2):
#     caracteristicas_df = normalize_dataframe(df)
#     pca = PCA(n_components=n_comp)
#     pca.fit(caracteristicas_df)
#     caracteristicas_pca = pca.transform(caracteristicas_df)
#     caracteristicas_pca_df = pd.DataFrame(caracteristicas_pca)
#     return caracteristicas_pca_df


def df_svd(df, n_comp = 2, max_iter = 10):
    rd_df = normalize_dataframe(df)
    rd = TruncatedSVD(n_components=n_comp,algorithm='randomized', random_state=2019, n_iter=max_iter)
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df


def df_pca(df, n_comp = 2):
    rd_df = normalize_dataframe(df)
    rd = PCA(n_components=n_comp)
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df

def df_isomap(df, n_comp = 2, n_jobs = 1, n_neighbors = 5, max_iter = 1000):
    rd_df = normalize_dataframe(df)
    rd = Isomap(n_components=n_comp, n_neighbors = n_neighbors, max_iter = max_iter )
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df

   
def df_kernel_pca(df, n_comp = 2, n_jobs = 1):
    rd_df = normalize_dataframe(df)
    rd = KernelPCA(kernel="rbf",n_components=n_comp, gamma=None, fit_inverse_transform=False, random_state = 2019, n_jobs=n_jobs)
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df    

def df_mds(df, n_comp = 2, n_jobs = 1, max_iter = 1000):
    rd_df = normalize_dataframe(df)
    rd =  MDS(n_components=n_comp, max_iter=max_iter, metric=True, n_jobs=n_jobs, random_state=2019)
#     rd.fit(caracteristicas_df[:1000])
    caracteristicas_rd = rd.fit_transform(caracteristicas_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df


# In[11]:


# df_rd = df_mds(caracteristicas_df, n_comp=3, n_jobs=1, max_iter=1)
# df_rd = df_isomap(caracteristicas_df[:1000], n_comp=3, n_jobs=1, max_iter=10)
# df_rd = df_pca(caracteristicas_df)
# df_rd = df_svd(caracteristicas_df, max_iter=100)
df_rd = df_kernel_pca(caracteristicas_df, n_comp = 2, n_jobs=24)


# In[12]:


print(df_rd.min())
print(df_rd.max())

df_rd.head(5)
print(df_rd.describe())


# In[6]:





# In[ ]:





# In[ ]:





# In[ ]:





from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import GaussianRandomProjection
from sklearn.decomposition import FastICA
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.random_projection import SparseRandomProjection
from sklearn import preprocessing
from utils_analysis import normalize_dataframe


# In[2]:


caracteristicas_df = pd.read_csv('caracteristicas.csv')


# In[3]:


# def df_pca(df, n_comp = 2):
#     caracteristicas_df = normalize_dataframe(df)
#     pca = PCA(n_components=n_comp)
#     pca.fit(caracteristicas_df)
#     caracteristicas_pca = pca.transform(caracteristicas_df)
#     caracteristicas_pca_df = pd.DataFrame(caracteristicas_pca)
#     return caracteristicas_pca_df


def df_svd(df, n_comp = 2, max_iter = 10):
    rd_df = normalize_dataframe(df)
    rd = TruncatedSVD(n_components=n_comp,algorithm='randomized', random_state=2019, n_iter=max_iter)
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df


def df_pca(df, n_comp = 2):
    rd_df = normalize_dataframe(df)
    rd = PCA(n_components=n_comp)
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df

def df_isomap(df, n_comp = 2, n_jobs = 1, n_neighbors = 5, max_iter = 1000):
    rd_df = normalize_dataframe(df)
    rd = Isomap(n_components=n_comp, n_neighbors = n_neighbors, max_iter = max_iter, )
    rd.fit(caracteristicas_df)
    caracteristicas_rd = rd.transform(rd_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df

    
def df_mds(df, n_comp = 2, n_jobs = 1, max_iter = 1000):
    rd_df = normalize_dataframe(df)
    rd =  MDS(n_components=n_comp, max_iter=max_iter, metric=True, n_jobs=n_jobs, random_state=2019)
#     rd.fit(caracteristicas_df[:1000])
    caracteristicas_rd = rd.fit_transform(caracteristicas_df)
    caracteristicas_rd_df = pd.DataFrame(caracteristicas_rd)
    return caracteristicas_rd_df


# In[4]:

# EJEMPLOS

# df_rd = df_mds(caracteristicas_df, n_comp=3, n_jobs=1, max_iter=1)    
# df_rd = df_isomap(caracteristicas_df, n_comp=3, n_jobs=1, max_iter=1)


# df_rd = df_pca(caracteristicas_df)
df_rd = df_svd(caracteristicas_df,n_comp = 3, max_iter=100)


# In[5]:


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




