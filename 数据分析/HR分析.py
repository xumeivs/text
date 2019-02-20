import pandas
import numpy
import scipy.stats
import matplotlib.pyplot
import matplotlib.pylab
import seaborn
df=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/HR.csv')
df=df.dropna(axis=0,how='any')
df=df[df['last_evaluation']<=1][df['salary']!='nme'][df['department']!='sale']
hg=df.groupby('department').mean()
fg=df.loc[:,['last_evaluation','satisfaction_level','department']].groupby('department').mean()
seaborn.set_style(style='whitegrid')
matplotlib.pyplot.title('SALARY')
matplotlib.pyplot.xlabel('salary')
matplotlib.pyplot.ylabel('Number')
matplotlib.pyplot.xticks(numpy.arange(len(df['salary'].value_counts()))+0.5,df['salary'].value_counts().index)
matplotlib.pyplot.axis([0,4,0,10000])
matplotlib.pyplot.bar(numpy.arange(len(df['salary'].value_counts()))+0.5,df['salary'].value_counts(),width=0.5)
for x,y in zip(numpy.arange(len(df['salary'].value_counts()))+0.5,df['salary'].value_counts()):
    matplotlib.pyplot.text(x,y,y,ha='center',va='bottom')
matplotlib.pyplot.show()
#直方图
f=matplotlib.pyplot.figure()
f.add_subplot(1,3,1)
seaborn.distplot(df['satisfaction_level'],bins=10)
f.add_subplot(1,3,2)
seaborn.distplot(df['last_evaluation'],bins=10)
f.add_subplot(1,3,3)
seaborn.distplot(df['average_monthly_hours'],bins=10)
matplotlib.pyplot.show()
#箱线图
seaborn.boxplot(y=df['time_spend_company'])
matplotlib.pyplot.show()
#折线图
#sub_df=df.groupby('time_spend_company').mean()
#seaborn.pointplot(sub_df.index,sub_df['left'])
seaborn.pointplot(x=df['time_spend_company'],y=df['left'])
matplotlib.pyplot.show()
#饼图
lbs=df['department'].value_counts().index
explodes=[0.1 if i=='sales' else 0 for i in  lbs]
matplotlib.pyplot.pie(df['department'].value_counts(normalize=True),explode=explodes,labels=lbs,autopct='%1.1f%%')
matplotlib.pyplot.show()
