import jieba
import pandas
import os
import numpy
from wordcloud import WordCloud
import matplotlib.pyplot
import matplotlib.pylab
from gensim import corpora,models,similarities
import gensim
import re
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#遍历文件下所以文件路径
def mubiao(dress):
    alldress=[]
    path=dress
    for dirpath,dirnames,filenames in os.walk(path):
        for filepath in filenames:
            fullpath=os.path.join(dirpath,filepath)
            alldress.append(fullpath)
    return alldress
#使用jieba分词
def jieci (filedress):
    fh=open(filedress,'rb').read().decode('utf-8')
    fh=re.sub('\s','',fh)
    fh=fh.strip()
    file=jieba.cut(fh)
    content=[]
    for item in file:
        if item !='\r\n'and len(item)>0:
            content.append(item)
    return content
#df_data11=pandas.DataFrame({'词':data11})
#打开停用词 并分好 也可使用结巴工具
def stopwordsF (filedress):
    stopwords=[line.strip() for line in open(filedress,'r',encoding='utf-8').readlines()]
    return stopwords
#清洗数据
def qingxi(yuanshuju,tingci):
    clean_word=[]
    all_words=''
    for item in yuanshuju:
        if item not in tingci:
            clean_word.append(item)
            all_words+=item
    return clean_word,all_words
filedresss=mubiao('E:/测试/百度百科/')
allclean=[]
allwords=' '
for i in range(0,50):
    content=jieci(filedresss[i])
    stopwords=stopwordsF('F:/数据分析/文本分析/停用词.txt')
    clean_word,all_words=qingxi(content,stopwords)
    allclean.append(clean_word)
    allwords+=all_words+ ' '
allwordf=jieba.cut(allwords)
allwordsr=[]
for word in allwordf:
    if len(word)>0:
        allwordsr.append(word)
df_allclean=pandas.DataFrame({'allclean':allclean})
df_allwords=pandas.DataFrame({'allwords':allwordsr})
words_count=df_allwords.groupby(by=['allwords'])['allwords'].agg({'count':numpy.size})
words_count=words_count.reset_index().sort_values(by=['count'],ascending=False)

'''
#可视化
backgroud_Image = matplotlib.pyplot.imread('F:/数据分析/素材/79726bdb-2247-4db6-ac16-6d170dc48982.jpg')
#matplotlib.rcParams['figure.figsize']=(10.0,5.0)
word_frequence={x[0]:x[1] for x in words_count.head(50).values}
wordcloud=WordCloud(font_path='./data/simhei.ttf',background_color='white',mask=backgroud_Image,max_words=50,max_font_size=150)
wordcloud=wordcloud.fit_words(word_frequence)
matplotlib.pyplot.imshow(wordcloud)
matplotlib.pyplot.show()
d=os.path.dirname('F:/数据分析/文本分析/')
wordcloud.to_file(os.path.join(d,'词图.jpg'))
print('热词生成完成')
'''
'''
content=[]
for i in range(0,len(filedresss)):
    fh=open(filedresss[i],'r',encoding='utf-8').read()
    content.append(fh)
#关键词提取
import jieba.analyse
index=21
print(content[index])#输出原文
content_str=''.join(allclean[index])#将分词完得 变成str
tags=jieba.analyse.extract_tags(content_str,topK=10)#关键词提取
print('  '.join(tags))#输出关键词
'''

#词频统计
frequency=defaultdict(int)
for token in allwordsr:
    frequency[token]+=1
allwordsr=[token for token in allwordsr if frequency[token]>1]
fh=open('E:/下载/语料.txt','w',encoding='utf-8')
fh.write(str(allwordsr))
fh.close()
fh=open('E:/下载/待分类.txt','w',encoding='utf-8')
fh.write(str(allwordsr))
fh.close()
def GG (num_):
    texts=[]
    for i in range(0,num_):
        fh=open(filedresss[i],'r',encoding='utf-8').read()
        texts.append(fh)
    return texts
    
vectorizer = TfidfVectorizer(norm="l1")
vectorizer.fit(allwordsr)
#print(dictionary.dfs)
x = vectorizer.fit_transform(GG(50)).toarray()
num_clusters=10
kmm=KMeans(n_clusters=num_clusters)
y=kmm.fit_predict(x)
print(y)
s=numpy.arange(0,len(y))
matplotlib.pylab.plot(s,y,'o')
matplotlib.pylab.show()
label_pred = kmm.labels_
print(label_pred)




















