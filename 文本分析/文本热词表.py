import jieba
import matplotlib.pyplot
import os
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
fh=open('F:/数据分析/文本分析/词.txt','r',encoding='utf-8').read()
data=jieba.cut(fh)
allwords=''
for word in data:
    allwords+=word+' '
#加载图片
backgroud_Image = matplotlib.pyplot.imread('F:/数据分析/素材/timg.jpg')
STOPWORDS=[line.strip() for line in open('F:/数据分析/文本分析/停用词.txt','r',encoding='utf-8').readlines()]
print('图片加载成功')
#加载词云样式
wordcloud=WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='./data/simhei.ttf',
    max_words=2000,
    #stopwords=STOPWORDS,
    max_font_size=150,
    random_state=30
    )
wordcloud.generate_from_text(allwords)
print('开始加载文本')
img_colors=ImageColorGenerator(backgroud_Image)
wordcloud.recolor(color_func=img_colors)
matplotlib.pyplot.imshow(wordcloud)
matplotlib.pyplot.show()
