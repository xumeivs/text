import numpy
import matplotlib.pylab
import pandas
import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='shuju')
sql='select price,comment from taob'
data=pandas.read_sql(sql,conn)
#离差标准化 （data-data.min()）/(data.max()-data.min())（最小最大标准化）
data2=(data-data.min())/(data.max()-data.min())
#标准差标准化（零-均值标准化）
data3=(data-data.mean())/data.std()
#小数定标规范化
#求对数 k=numpy.log abs()绝对值
k=numpy.ceil(numpy.log10(data.abs().max()))#numpy.ceil  进1取整法
data4=data/10**(k)
#连续型数据离散化
#1等宽离散化
data5=data[u'price'].copy()
data6=data5.T
data7=data6.values
c1=pandas.cut(data7,4,labels=['便宜','适中','偏贵','贵'])#非等宽 修改4的位置 自定义范围[x,y,z,u]
c2=pandas.cut(data7,[0,50,100,130,200,300,data7.max()])
#2等频率离散化
#3一维聚类离散化
#属性构造
