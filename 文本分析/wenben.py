import jieba
sentence='我喜欢上海东方明珠塔'
w1=jieba.cut(sentence,cut_all=True)#cut_all=True 全分析模式 False 精准模式
#循环输出
for item in w1:
    print(item)
print('  ')
w2=jieba.cut(sentence,cut_all=False)
for i in w2:
    print(i)
print('    ')
#搜收引擎模式
w3=jieba.cut_for_search(sentence)
for item in w3:
    print(item)
print('    ')
#词性标注
import  jieba.posseg
w4=jieba.posseg.cut(sentence)
#.flag词性
#.word词语
for item in w4:
    print(item.word+'---'+item.flag)
print('     ')
'''
a:形容词
c:连词
d:副词
e:叹词
f:方位词
i:成语
m:数词
n:名词
nr:人名
ns:地名
nt:机构团体
nz:其他专有名词
p:介词
r:代词
t:时间
u:助词
v:动词
vn:名动词
w:标点符号
un:未知词语
'''
#自创词典加载
#jieba.load_userdict('地址')
#添加词进字典
w7=jieba.cut(sentence)
for item in w7:
    print(item)
print('   ')
jieba.add_word('东方明珠塔')
w8=jieba.cut(sentence)
for item in w8:
    print(item)
print('      ')
#更改频率





#返回文本高频词汇
import jieba.analyse
tag=jieba.analyse.extract_tags(sentence,3)#(对象，个数)
print(tag)
print('     ')

#返回词语位置
w9=jieba.tokenize(sentence)
for item in w9:
    print(item)

print('    ')

w10=jieba.tokenize(sentence,'search')#搜索引擎模式
for item in w10:
    print(item)

#分析盗墓笔记词频
data=open('E:/python数据分析/python3数据分析与挖掘实战/源码/源码/第7周/盗墓笔记(1).txt','rb').read()
p=jieba.analyse.extract_tags(data,20)
print(p)












