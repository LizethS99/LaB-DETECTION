import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(7)

x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2))
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
x4 = np.random.standard_normal((100,2))*0.3-2*np.ones((100,2))+10
X = np.concatenate((x1,x2,x3,x4),axis=0)

plt.plot(X[:,0],X[:,1],'k.')
plt.show()

n = 4
k_means = KMeans(n_clusters=n)
k_means.fit(X)
centroides = k_means.cluster_centers_
etiquetas = k_means.labels_
plt.plot(X[etiquetas==0,0],X[etiquetas==0,1],'r.', label='cluster 1')
plt.plot(X[etiquetas==1,0],X[etiquetas==1,1],'b.', label='cluster 2')
plt.plot(X[etiquetas==2,0],X[etiquetas==2,1],'g.', label='cluster 3')
plt.plot(X[etiquetas==3,0],X[etiquetas==3,1],'g.', label='cluster 4')

plt.plot(centroides[:,0],centroides[:,1],'mo',markersize=8, label='centroides')

plt.legend(loc='best')
plt.show()