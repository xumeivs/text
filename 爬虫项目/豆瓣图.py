import urllib.request
import re
headers=('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(0,20):
    url='https://www.dbmeinv.com/?pager_offset='+str(i)
    data=urllib.request.urlopen(url).read().decode('utf-8')
    pat='class="img_single"> <a href="(.*?)" class="link"'
    imurl=re.compile(pat).findall(data)
    for j in range(0,len(imurl)):
      
        data2=urllib.request.urlopen(imurl[j]).read().decode('utf-8')
        pat2='src="(.*?)" width="500"'
        thisurl=re.compile(pat2).findall(data2)
        for z in range(0,len(thisurl)):
            print(str(j)+str(z))
            imaurl=thisurl[z]
            file='E:/测试/豆瓣图片/'+str(i)+str(j)+'.jpg'
            urllib.request.urlretrieve(imaurl,filename=file)
            print('ok')
        
            
        
    
