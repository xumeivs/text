import numpy
import pandas
import matplotlib.pylab
import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='shuju')
sql='select price,comment from taob limit 300'
data=pandas.read_sql(sql,conn)
x=data.iloc[:,:].as_matrix()
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)
for i in range(0,len(y)):
    if(y[i]==0):
        matplotlib.pylab.plot(data.iloc[i:i+1,0:1].as_matrix(),data.iloc[i:i+1,1:2].as_matrix(),'*r')
    if(y[i]==1):
        matplotlib.pylab.plot(data.iloc[i:i+1,0:1].as_matrix(),data.iloc[i:i+1,1:2].as_matrix(),'sy')
    else:
        matplotlib.pylab.plot(data.iloc[i:i+1,0:1].as_matrix(),data.iloc[i:i+1,1:2].as_matrix(),'dk')
matplotlib.pylab.show()
