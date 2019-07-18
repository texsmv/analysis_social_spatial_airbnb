import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D

# get_ipython().run_line_magic('matplotlib', 'widget')
# get_ipython().run_line_magic('matplotlib', 'notebook')
# get_ipython().run_line_magic('pylab', '')

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



# get_ipython().run_line_magic('matplotlib', 'inline')
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



def testClusters(limit,X):
    Nc = range(1, limit)
    kmeans = [KMeans(n_clusters=i) for i in Nc]
    score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
    plt.plot(Nc,score)
    plt.xlabel('Numero de clusters')
    plt.ylabel('Y')
    plt.title('X')
    plt.show()




#Procesando data de PRUEBA
dataframe = pd.read_csv(r"analisis.csv")

colores=['red','green','blue','cyan']
X = np.array(dataframe[["op","ex","ag"]])



#Processando 2
dataframe = pd.read_csv(r"caracteristicas.csv")
dataframe
# X = np.array(dataframe[["price","accommodates","cleaning_fee"]])




import pickle
infile = open('todo.pk','rb')
data_re = pickle.load(infile)
infile.close()
print(data_re)
data_re.shape
# len(data_re[0])




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

