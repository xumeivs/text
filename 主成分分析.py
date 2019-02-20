import numpy
import matplotlib.pylab
import pandas
'''
data=pandas.read_excel('C:/Users/Administrator/Desktop/DATA/renkou.xls')
data2=data.T
x=data2.values[0]
y=data2.values[1]
matplotlib.pylab.plot(x,y,'o')
matplotlib.pylab.show()
'''
import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='shuju')
sql='select price,comment from taob'
data=pandas.read_sql(sql,conn)
#data2=data.T
#x=data2.values[0]
#y=data2.values[1]
#matplotlib.pylab.plot(x,y,'or')
#matplotlib.pylab.show()
hang=len(data.values)
lie=len(data.values[0])
da=data
for i in range(0,hang):
    for j in range(0,lie):
        if(da.values[i][1]>400000):
            #print(da[i][j])
            da.values[i][1]='300000'
#da1=da.T
#x=da1[0]
#y=da1[1]
#matplotlib.pylab.plot(x,y,'or')
#matplotlib.pylab.show()
#离散化
data2=(da-da.min())/(da.max()-da.min())
#发现缺失值
x=0
data2['price'][(data2['price'])==0]=None
for i in data2.columns:
    for j in range (len(data2)):
        if(data2[i].isnull())[j]:
            data2[i][j]='0.008132'
            x+=1
#print(x)
#属性构造
ch=data2[u'comment']/data2[u'price']
data2[u'评价比']=ch
#主成分分析
from sklearn.decomposition import PCA
pca1=PCA(2)
pca1.fit(data2)
tz1=pca1.components_
rate=pca1.explained_variance_ratio_
reduction=pca1.transform(data2)
