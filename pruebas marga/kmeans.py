#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D

get_ipython().run_line_magic('matplotlib', 'widget')
get_ipython().run_line_magic('matplotlib', 'notebook')
get_ipython().run_line_magic('pylab', '')


# In[56]:


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on points')

line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print('onpick points:', points)

fig.canvas.mpl_connect('pick_event', onpick)

# plt.show()


# In[51]:


get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib widget
# %matplotlib notebook
# %pylab
plt.rcParams['figure.figsize'] = (8,8)

etiquetasAll = []

def kmeans(x,k,colores,dim):
    kmeans = KMeans(n_clusters=k).fit(x)
    centroids = kmeans.cluster_centers_
    print("\t~~~~centroides~~~~")
    print(centroids)
    labels = kmeans.predict(x)
    print("\t~~~~Etiquetas~~~~")
    print(labels)
    etiquetasAll.append(labels)
    # Getting the cluster centers
    C = kmeans.cluster_centers_
#     print(C.shape, "shape")
    asignar=[]
    for row in labels:
        asignar.append(colores[row])
    fig = plt.figure()
    if dim == 3:
        ax = Axes3D(fig)
        ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=asignar,s=60)
        ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000) #centroides 
    elif dim ==2:
        plt.scatter(x[:, 0], x[:, 1], c=asignar, s=70)
        plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
        
        fig.canvas.mpl_connect('pick_event', onpick)
        plt.show()


# In[14]:


def testClusters(limit,X):
    Nc = range(1, limit)
    kmeans = [KMeans(n_clusters=i) for i in Nc]
    score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
    plt.plot(Nc,score)
    plt.xlabel('Numero de clusters')
    plt.ylabel('Y')
    plt.title('X')
    plt.show()


# In[15]:


#Procesando data de PRUEBA
dataframe = pd.read_csv(r"analisis.csv")

colores=['red','green','blue','cyan']
X = np.array(dataframe[["op","ex","ag"]])


# In[16]:


#Processando 2
dataframe = pd.read_csv(r"caracteristicas.csv")
dataframe
# X = np.array(dataframe[["price","accommodates","cleaning_fee"]])


# In[75]:


# testClusters(20,X)


# In[76]:


# kmeans(X,4,colores,2)


# In[64]:


# np.random.seed(1)

# x = np.random.rand(15)
# y = np.random.rand(15)
# names = np.array(list("ABCDEFGHIJKLMNO"))
# c = np.random.randint(1,5,size=15)

# norm = plt.Normalize(1,4)
# cmap = plt.cm.RdYlGn

# fig,ax = plt.subplots()
# sc = plt.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)

# annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
#                     bbox=dict(boxstyle="round", fc="w"),
#                     arrowprops=dict(arrowstyle="-|>"))
# annot.set_visible(False)

# a = [1,2,3,4]
# def update_annot(ind):
    

#     pos = sc.get_offsets()[ind["ind"][0]]
#     annot.xy = pos
#     text = "{}".format(a[0])
#     annot.set_text(text)
#     annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
#     annot.get_bbox_patch().set_alpha(0.4)

    


# def hover(event):
#     vis = annot.get_visible()
#     if event.inaxes == ax:
#         cont, ind = sc.contains(event)
#         if cont:
#             update_annot(ind)
#             annot.set_visible(True)
#             fig.canvas.draw_idle()
#         else:
#             if vis:
#                 annot.set_visible(False)
#                 fig.canvas.draw_idle()

# fig.canvas.mpl_connect("motion_notify_event", hover)

# plt.show()


# In[18]:


import pickle
infile = open('todo.pk','rb')
data_re = pickle.load(infile)
infile.close()
print(data_re)
data_re.shape
# len(data_re[0])


# In[63]:


def matrix(data):
    print ("hi")
    data = np.array(data)
    

    size = len(data[0])
    size = 1
    print(size)
    colores=['red','green','blue','cyan']
    for i in range (size-1):
#         print(data[:,i:i+1])
        print("~~~~~~~~~~~~>>>>>>>>> i ",i,"<<<<<<<<~~~~~~~~~")
        for j in range(i+1,size):
            print("~~~~~~~~~~~~>>>>>>>>> j ",j,"<<<<<<<<~~~~~~~~~")
            X = np.concatenate((data[:,i:i+1],data[:,j:j+1]),axis=1)
            kmeans(X,4,colores,2)
            print(X)
        print("-----")

m = [[1,4,20,30],[2,5,21,31],[3,6,22,32],[3,6,22,32]]
matrix(data_re)


# m = np.array(m)

# m[:,1:2]


# In[69]:


# data_re[:,:3].shape
X = data_re
etiquetasAll = np.array(etiquetasAll)
# print(np.array(etiquetasAll))
etiquetasAll[1]
# testClusters(20,X)
# for h in etiquetasAll[2]:
#     print(h)
dataframe
dataa = np.array(dataframe)
dataa.shape
# len(dataa)
newData = []
for g in range(len(dataa)):
#     print(dataa[g].shape)
    newData.append(np.append(dataa[g],etiquetasAll[2][g]))
# pd.DataFrame(dataa)


# In[70]:


from pandas import DataFrame
dataa = pd.DataFrame(newData)
export_csv = dataa.to_csv (r'dataframe.csv', index = None, header=False)


# In[79]:


# pd.DataFrame(X).describe()


# In[80]:


#Processando 3
# dataframe = pd.read_csv(r"caracteristicas.csv")
# dataframe.describe()
# X = np.array(dataframe[["price","accommodates","cleaning_fee"]])

# kmeans(X,4,colores,3)


# In[81]:


x1 = X[:,:2]

colores=['red','blue','cyan']
# kmeans(x1,3,colores,2)


# In[85]:


x2 = X[:,1:3]

colores=['red','blue','cyan']
# kmeans(x2,3,colores,2)
# print(pd.DataFrame(X).describe())
# pd.DataFrame(x2).describe()


# In[83]:


x1 = X[:,0:2]

colores=['red','blue','cyan','yellow','purple']
# kmeans(x1,5,colores,2)

