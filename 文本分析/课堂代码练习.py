#练习
from gensim import corpora,models,similarities
import jieba
data1=open('F:/数据分析/文本分析/d1.txt','rb').read()
data2=open('F:/数据分析/文本分析/d2.txt','rb').read()
w1=jieba.cut(data1)
w2=jieba.cut(data2)
w11=''
for item in w1:
    w11+=item+' '
w22=''
for item in w2:
    w22+=item+' '
documents=[w11,w22]
texts=[[word for word in document.split()]
           for document in documents]
from collections import defaultdict
frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1
