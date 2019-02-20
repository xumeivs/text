#HR数据分析
import numpy
import pandas
import scipy.stats
df=pandas.read_csv('C:/Users/Administrator/Desktop/DATA/HR.csv')
#正态分布与三大抽样分部基础操作
df.mean()#均值
df.std()#标准差
df.median()#中位数
df.quantile()#分位数
df.var()#方差
df.mode()#众数
df.skew()#偏态系数
df.kurt()#峰度系数
df.sum()#求和
scipy.stats.norm()#构造标准正态分布
scipy.stats.norm.stats(moment='mvsk')#标准正态分布属性
scipy.stats.norm.pdf()
scipy.stats.norm.ppf()
scipy.stats.norm.cdf()
scipy.stats.norm.rvs(size=10)#十个符合正态分布的数字
scipy.stats.chi2#卡方分布
scipy.stats.t#t分布
scipy.stats.f#f分布
df.sample(n=10)#对df抽样十个
df.sample(frac=0.001)#按比例抽取
#satisfaction level 的分析
al=df['satisfaction_le']
al.isnull()#异常值
al=al.dropna()#抛弃异常值
numpy.histogram(al.values,bins=numpy.arange(0.0,1.1,0.1))#取值 arange里是取值范围和步长，前一项是出现次数
#lastevaluation的分析
#四分位之间取值
#先求出上四分位数和下 四分位数，再相减。上界=上四分位数+k*相减得到的值 下界=下四分位数-k*相减得到得值
#numberproject 分析
#计数
np=df['']
np.values_counts(normalize=True).sort_index()#按比例 升序得顺序排序
