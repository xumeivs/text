#折线图绘制/散点图
import matplotlib.pylab as pyl
import numpy as npy
#y=[2,3,5,7,8]
#pyl.plot(x,y,)#直方图  plot(x轴数据，y轴数据，展现图形形式)
#pyl.show()
#pyl.plot(x,y,'o')#散点图 
#pyl.show()
#pyl.plot(x,y,'om')
'''
c--cyan--青色
r--red--红色
m--magente--品红
g--green--绿色
b--blue--蓝色
y--yellow--黄色
k--black--黑色
w--white--白色

'''
#pyl.show()
#线条样式
'''
- 直线
--虚线
-. -.形式
：细小的虚线
'''
#pyl.plot(x,y,':')
#pyl.show()
#改变点的样式
'''
s 方形
h 六角形
H  六角形
* 星形
+ +号形式
x  x形
d  棱形
p  五角形

'''

#pyl.plot(x,y,'p')
#pyl.show()
'''
pyl.plot(x,y,'r')
x2=[1,4,5,6,6,8]
y2=[4,5,1,6,2,9]
pyl.plot(x2,y2,'b')
pyl.title('show')
pyl.xlabel('hh')
pyl.ylabel('yy')
pyl.xlim(0,10)
pyl.ylim(1,10)
pyl.show()
'''
#如何生产随机数
import numpy as npy
data=npy.random.random_integers(0,20,10)#(最小值，最大值，生成随机数个数)
#生成正太分布随机数
data2=npy.random.normal(182,3,49)#(均数，方差，个数)
#直方图hist绘制
data3=npy.random.normal(56,34,1000)
#pyl.hist(data3)
#pyl.title('shk')
#sty=pyl.arange(2,18,4)2 是起始位置 18 最后位置 4是步长
#pyl.hist(data,sty,histtype='stepfilled')#stepfilled 取消轮廓
#pyl.show()
#子图
#pyl.subplot(4,2,3)#(拆分多少行，xxxx列，当前区域)
#pyl.show()
#pyl.subplot(2,2,1)
#x=[1,2,3,4,5]
#y=[3,4,5,1,3]
#pyl.plot(x,y)

#pyl.subplot(2,2,2)
#x1=[2,4,6,3,1]
#y1=[7,4,3,1,2]
#pyl.plot(x1,y1)
#pyl.subplot(2,1,2)
#x2=[5,6,3,1,6]
#y2=[5,4,68,8,3]
#pyl.plot(x2,y2)
#pyl.show()
#读取和讯博客的数据并可视化
import pandas
import numpy
import matplotlib.pylab
data4=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/hexun.csv')
data4.values#[第几行][第几列]
data5=data4.T#转置
x=data5.values[3]
y=data5.values[4]
matplotlib.pylab.plot(x,y)
matplotlib.pylab.show()


