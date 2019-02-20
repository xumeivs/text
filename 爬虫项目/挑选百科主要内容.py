import requests
from  bs4 import BeautifulSoup
import re
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import jieba

try:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    proxies={'http':'http://60.211.166.42:63000',
             'https':'https://60.211.166.42:63000',}
    response=requests.get('https://baike.baidu.com/',headers=headers)
    print(response.status_code)
except ReadTimeout:
    print('超时访问')
except HTTPError:
    print('网址错误')
except RequestExceptin:
    print('错误')
soup=BeautifulSoup(response.content,'lxml')
#获取百科地址
links=soup.find_all('a', href=re.compile(r"/item/(.*)"))
pat='<a href="https://baike.baidu.com/item(.*?)" '
new_urls=re.compile(pat).findall(str(links))
try:
    for i in range(0,len(new_urls)):
        response=requests.get('https://baike.baidu.com/item'+new_urls[i],headers=headers)
        soup=BeautifulSoup(response.content,'lxml')
        links=soup.find_all('a',href=re.compile(r'/item/(.*?)'))
        pat='href="/item(.*?)"'
        links=re.compile(pat).findall(str(links))
        for link in links:
            if len(link)>0 and link!='\r\n':
                new_urls.append(link)
        fh=open('E:/测试/阿修罗.txt','w',encoding='utf-8')
        fh.write(str(new_urls))
        fh.close()
    for i in range(0,len(new_urls)):
        print('第'+str(i)+'个任务开始')
        u=new_urls[i]
        url='https://baike.baidu.com/item'+u
        hj=requests.get(url,headers=headers)
        soup=BeautifulSoup(hj.content,'lxml')
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        name=title_node.get_text()
        #summary_node=soup.find('div',class_='lemma-summary')
        #content=summary_node.get_text()
        neirong=soup.find_all('div',class_='para')
        #for j in range(len(new_urls)):
        fh=open('E:/测试/百度百科/'+name+'.txt','w',encoding='utf-8')
        for z in range(0,len(neirong)):
            fh.write(neirong[z].get_text())
        fh.close()
        print(name+'爬取成功')
except Exception as e:
    print(e)
        
'''
title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
print(title_node.get_text())
'''
'''
summary_node = soup.find('div', class_="lemma-summary")
print(summary_node.get_text())
for i in soup.find_all('div',class_='para'):
    print(i.string)
'''
#print(soup.get_text())
