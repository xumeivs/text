#决策树
import pandas
data=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/lesson2.csv')
x=data.iloc[:,1:5].as_matrix()
y=data.iloc[:,5:].as_matrix()
for i in range(0,len(x)):
    for j in range (0,len(x[i])):
        thisdata=x[i][j]
        if(thisdata=='是' or thisdata=='高' or thisdata=='多'):
            x[i][j]=int(1)
        else:
            x[i][j]=int(-1)
            
for i in range(0,len(y)):
    thisdata=y[i]
    if (thisdata=='高'):
        y[i]=int(1)
    else:
        y[i]=int(-1)
x2=pandas.DataFrame(x).as_matrix().astype(int)
y2=pandas.DataFrame(y).as_matrix().astype(int)
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC(criterion='entropy')
dtc.fit(x2,y2)
import numpy
f=numpy.array([[1,-1,1,1],[1,-1,1,-1]])
rst=dtc.predict(f)
print(rst)
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open('C:/Users/Administrator/Desktop/DATA/dtc.dot','w')as file:
    export_graphviz(dtc,feature_names=['combat','num','promotion','datum'],out_file=file)
    
