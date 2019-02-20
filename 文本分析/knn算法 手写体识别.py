from numpy import *
import operator
from os import listdir
#tile(a,(size,1))从列方向扩展
def knn(k,traindata,testdata,labels):
    traindatasize=traindata.shape[0]#获得traindata的行数
    dif=tile(testdata,(traindatasize,1))-traindata#扩展后的trestdata-traindata
    sqdif=dif**2
    sqdifsum=sqdif.sum(axis=1)
    distance=sqdifsum**0.5
    sortdistance=distance.argsort()#对得到的距离进行排序
    count={}
    for i in range(0,k):
        vote=labels[sortdistance[i]]
        count[vote]=count.get(vote,0)+1#获取次数最多的count【vote】
        sortcount=sorted(count.items(),key=operator.itemgetter(1),reverse=True)#进行降序排序
        return sortcount[0][0]
#图片处理
#先将图片转为固定宽高，比如32*32，再转为文本
from PIL import Image
'''
fh=open('F:/数据分析/素材/timg.txt','a')
im=Image.open('F:/数据分析/素材/u=1612787314,404742205&fm=27&gp=0.jpg')
width=im.size[0]
height=im.size[1]
for i in range(0,width):
    for j in range(0,height):
        cl=im.getpixel((i,j))
        allcl=cl[0]+cl[1]+cl[2]#三个元素
        if (allcl==0):
            fh.write('1')
        else:
            fh.write('0')
    fh.write('\n')
fh.close()
'''               
#加载数据
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
arr1=datatoarray('F:/数据分析/素材/digits/trainingDigits/0_4.txt')
#建立一个函数取文件前缀
def spelabel(fname):
    filestr=fname.split('.')[0]
    label=int(filestr.split('_')[0])
    return label
#建立训练文本
def traindata():
    labels=[]
    trainfile=listdir('F:/数据分析/素材/digits/trainingDigits')
    num=len(trainfile)
    #行数32*32=1024（列）每一行储存一个文件
    #用一个数组储存所以训练数据，行：文件总数 列：1024
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisfname=trainfile[i]
        thislabel=spelabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("F:/数据分析/素材/digits/trainingDigits/"+thisfname)
    return trainarr,labels
#用测试数据调用KNN算法，看是否能够精确识别

def testdata():
    trainarr,labels=traindata()
    testlist=listdir('F:/数据分析/素材/digits/testDigits')
    tnum=len(testlist)
    for i in range(0,tnum):
        thistestfile=testlist[i]
        testarr=datatoarray('F:/数据分析/素材/digits/testDigits/'+thistestfile)
        rknn=knn(3,trainarr,testarr,labels)
        print(rknn)
#testdata()
#抽某一个文件测试
trainarr,labels=traindata()
thistestfile='1_95.txt'
testarr=datatoarray('F:/数据分析/素材/digits/testDigits/'+thistestfile)
rknn=knn(3,trainarr,testarr,labels)
print(rknn)






















    
