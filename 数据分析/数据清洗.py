import numpy
import matplotlib.pylab
import pandas
import pymysql
#数据清洗
#发现空值
#conn=pymysql.connect(host='127.0.0.1',user='root',passwd='13579zheng',db='shuju')
#sql='select * from book'
#data=pandas.read_sql(sql,conn)
#print(data.describe())
data=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/book.csv')

'''
x=0
data['commentcount'][(data['commentcount']==0)]=None
for i in  data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[j][i]='20'
            x+=1
'''
#异常值处理
#画散点图（横轴为价格，纵轴为评论数）
#get pricel
data2=data.T
x=data2.values[5]
y=data2.values[3]

matplotlib.pylab.plot(x,y,'o')
matplotlib.pylab.show()
line=len(data.values)
clo=len(data.values[0])
da=data.values
for i in range(0,line):
    for j in range(0,clo):
        if(da[i][3]>20000):
            print(da[i][j])
            da[i][j]=20000
        if(da[i][5]>1600):
            print(da[i][j])
            da[i][j]=1500
da2=da.T
pricel=da2[5]
comment=da2[3]
matplotlib.pylab.plot(pricel,comment,'o')
matplotlib.pylab.show()
#分步分析
pricelmax=da2[5].max()
pricelmin=da2[5].min()
commentmax=da2[3].max()
commentmin=da2[3].min()
#极差：最大减最小
jjicha=pricelmax-pricelmin
cojicha=commentmax-commentmin
#组距：极差/组数
zuji=jjicha/12
comzuji=cojicha/12
#画价格直方图
pricedst=numpy.arange(pricelmin,pricelmax,zuji)
matplotlib.pylab.hist(da2[5],pricedst)
matplotlib.pylab.show()

            
            
