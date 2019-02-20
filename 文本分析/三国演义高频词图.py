import jieba
import os
import matplotlib.pyplot
import pandas
from wordcloud import WordCloud,ImageColorGenerator
import numpy
def jiebaq (dress):
    fh=open(dress,'rb').read().decode('utf-8')
    data=jieba.cut(fh)
    SAN=[]
    for word in data:
        if word !='\r\n'and len(word)>0:
            SAN.append(word)
    return SAN
SAN=jiebaq('E:/下载/金瓶梅.txt')
stopwords=[line.strip() for line in open('F:/数据分析/文本分析/停用词.txt','r',encoding='utf-8').readlines()]

def qingxi(content,stopwords):
    SAN_CLEAN=[]
    for item in content:
        if item not in stopwords:
            SAN_CLEAN.append(item)
    return SAN_CLEAN
SAN_CLEAN=qingxi(SAN,stopwords)
df_SAN_CLEAN=pandas.DataFrame({'SAN_CLEAN':SAN_CLEAN})
words_frequence=df_SAN_CLEAN.groupby(by=['SAN_CLEAN'])['SAN_CLEAN'].agg({'count':numpy.size})
words_frequence=words_frequence.reset_index().sort_values(by=['count'],ascending=False)
matplotlib.rcParams['figure.figsize']=(10.0,5.0)
#background_Image=matplotlib.pyplot.imread('F:/数据分析/素材/timg (1).jpg')
wordcloud=WordCloud(  
    background_color='white',
    #mask=background_Image,
    font_path='./data/simhei.ttf',
    max_font_size=80)
word_frequence={x[0]:x[1] for x in words_frequence.head(500).values}
wordcloud=wordcloud.fit_words(word_frequence)
matplotlib.pyplot.imshow(wordcloud)
matplotlib.pyplot.show()
d=os.path.dirname('F:/数据分析/文本分析/')
wordcloud.to_file(os.path.join(d,'金瓶梅.jpg'))
print('构图完成')

