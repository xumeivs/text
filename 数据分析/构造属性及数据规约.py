import pymysql
import numpy
import pandas
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='shuju')
sql='select hits,comment from myhexun'
data=pandas.read_sql(sql,conn)
#属性构造
ch=data[u'comment']/data[u'hits']
data[u'评点比']=ch
file='C:/Users/Administrator/Desktop/DATA/1.xlsx'
data.to_excel(file,index=False)#index 索引
#数据规约
import pymysql
import numpy
import pandas
from sklearn.decomposition import PCA
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='shuju')
sql='select hits,comment from myhexun'
data2=pandas.read_sql(sql,conn)
ch=data2[u'comment']/data2[u'hits']
data2['评点比']=ch
#主成分分析
pca1=PCA()
pca1.fit(data2)
characteristic=pca1.components_#返回模型中各个特征量
rate=pca1.explained_variance_ratio_#各个成分中各自方差百分百，贡献率
pca2=PCA(2)
pca2.fit(data2)
reduction=pca2.transform(data2)#降维
hexun=pca2.inverse_transform(reduction)#恢复


