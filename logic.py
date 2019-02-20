import pandas
import numpy
import matplotlib.pylab
import statsmodels.api
import csv
dataf=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/luqu.csv')
#x=dataf.iloc[:,1:4].as_matrix()#转为数组 方法后记得加（）
#y=dataf.iloc[:,0:1].as_matrix()
#from sklearn.linear_model import LogisticRegression as LR
#from sklearn.linear_model import RandomizedLogisticRegression as RLR

d=pandas.crosstab(dataf['admit'],dataf['rank1'],rownames=['admit'])#频率表，表示rank与admit的值相应的数量关系
print(d)
dataf.hist()#绘制表格
matplotlib.pylab.show()
dummy_ranks = pandas.get_dummies(dataf['rank1'],prefix='rank1')#将rank 设置成虚拟变量 分类变量
keep=['admit','gre','gpa']
data=dataf[keep].join(dummy_ranks.ix[:,'rank1_1':])#将rank转化的虚拟变量
#需要
#自行添加逻辑回归的intercept变量
data['intercept']=1.0
train_clos=data.columns[1:]
logit=statsmodels.api.Logit(data['admit'],data[train_clos])
#拟合模型
result=logit.fit()
combos=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/yuce.csv')
dummy1_ranks=pandas.get_dummies(combos['rank1'],prefix='rank1')
keep1=['gre','gpa']
combos=combos[keep1].join(dummy1_ranks.ix[:,'rank1_1':])

combos['intercept']=1.0
predict_clos=combos.columns[:]

predict=combos['predict']=result.predict(combos[predict_clos])
#print(combos['predict'])
with open('C:/Users/Administrator/Desktop/DATA/yuce.csv','a',newline='pridict') as csvfile:
    writer=csv.writer(csvfile)
    for i in range(len(predict)):
        writer.writerows(str(predict[i]))
csvfile.close()
total=0
hit=0
'''
for value in combos.values:
    predict = value[-1]
    if predict >0.5:
        total+=1
        for j in data.values:
            admit= int(j[0])
            if admit==1:
                hit+=1
 
print('预测录取:%d,真实录取取:%d,预测命中率:%.2f'%(total,hit,100.0*(total/hit)))
'''
