import jieba
from gensim import corpora,models,similarities
from collections import defaultdict
d1=open('E:/下载/金瓶梅.txt','rb').read()
d2=open('E:/下载/《三国演义》罗贯中.txt','rb').read()
data1=jieba.cut(d1)
data2=jieba.cut(d2)
data11=''
for item in data1:
    data11+=item+' '
data21=''
for item in data2:
    data21+=item+' '
documents=[data11,data21]
texts=[[word for word in document.split()]
       for document in documents]
frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1
text=[[token for token in text if frequency[token]>20]
      for text in texts]
dictionary=corpora.Dictionary(texts)
dictionary.save('E:/下载/2.txt')
d2=open('E:/下载/《红楼梦》完整版.txt','rb').read()
data2=jieba.cut(d2)
data21=''
for item in data2:
    data21+=item+' '
new_doc=data21
new_vce=dictionary.doc2bow(new_doc.split())
corpus=[dictionary.doc2bow(text) for text in texts]
tfidf=models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[new_vce]]
print(sim)
