import jieba
from gensim import corpora,models,similarities
from collections import defaultdict
d1=open('E:/Major/python数据分析/python3数据分析与挖掘实战/源码/源码/第7周/盗墓笔记.txt','rb').read()
d2=open('E:/Major/python数据分析/python3数据分析与挖掘实战/源码/源码/第7周/老九门.txt','rb').read()
#对文档进行分词
data1=jieba.cut(d1)
data2=jieba.cut(d2)
#2.把分词整理为指定格式 ‘词语1 词语2 。。。词语n‘
data11=''
for item in data1:
    data11+=item+'  '
data21=''
for item in data2:
    data21+=item+'  '
#存储文档
documents=[data11,data21]
texts=[[word for word in document.split()]
      for document in documents]
#计算频率collections.defaultdict

frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1
#5.对低频词进行过滤
        '''
texts=[[word for word in text if frequency[token]>3]
       for text in texts]
'''
dictionary=corpora.Dictionary(texts)
dictionary.save('F:/数据分析/文本分析/wenben3.txt')
d3=open('E:/Major/python数据分析/python3数据分析与挖掘实战/源码/源码/第7周/《鬼吹灯》全本.txt','rb').read()
data3=jieba.cut(d3)
data31=''
for item in data3:
    data31+=item+' '
new_doc=data31
new_vec=dictionary.doc2bow(new_doc.split())
corpus=[dictionary.doc2bow(text) for text in texts]
#corpora.MmCorpus.serialize("F:/数据分析/文本分析/d3.mm",corpus)
tfidf=models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[new_vec]]
print(sim)

