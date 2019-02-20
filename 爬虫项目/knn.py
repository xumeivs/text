from numpy import *
from os import listdir
import operator
def knn (k,traindata,testdata,labels):
    traindatasize=traindata.shape[0]
    dif=tile(testdata,(traindatasize,1))-traindata
    sqldif=dif**2
    sumsqldif=sqldif.sum(axis=1)
    distance=sumsqldif**0.5
    sortdistance=distance.argsort()
    count={}
    for i in range(0,k):
        vote=labels[sortdistance[i]]
        count[vote]=count.get(vote,0)+1
        sortcount=sorted(count.items(),key=operator.itemgetter,reverse=True)
    return sortcount[0][0]
def datatoarry(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
def spelabel(fname):
    fiststr=fname.split('.')[0]
    label=int(fiststr.split('_')[0])
    return label
def traindata():
    labels=[]
    trainfile=listdir('F:/数据分析/素材/digits/trainingDigits')
    num=len(trainfile)
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisfname=trainfile[i]
        thislabel=spelabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarry("F:/数据分析/素材/digits/trainingDigits/"+thisfname)
    return trainarr,labels
def testdata():
    trainarr,labels=traindata()
    testfile=listdir('F:/数据分析/素材/digits/testDigits')
    tnum=len(testfile)
    for i in range(0,tnum):
        thistest=testfile[i]
        testarr=datatoarry('F:/数据分析/素材/digits/testDigits/'+thistest)
        rknn=knn(3,trainarr,testarr,labels)
        print(rknn)
#testdata()
trainarr,labels=traindata()
thistest='0_3.txt'
testarr=datatoarry('F:/数据分析/素材/digits/testDigits/'+thistest)
rknn=knn(3,trainarr,testarr,labels)
print(rknn)
