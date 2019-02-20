import numpy
import pandas
import matplotlib.pylab
data=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/luqu.csv')
x=data.iloc[:,1:4].as_matrix()
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)
s=numpy.arange(0,len(y))
matplotlib.pylab.plot(s,y,'o')
matplotlib.pylab.show()
