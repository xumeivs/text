# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request
class DlSpider(scrapy.Spider):
    name = 'dl'
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    allowed_domains = ['douban.com']
    '''
    start_urls = ['http://douban.com/']
'''
    def start_requests(self):
        return [Request("https://accounts.douban.com/login",callback=self.parse,meta={"cookiejar":1})]
    def parse(self, response):
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()
        url="https://accounts.douban.com/login"
        if len(captcha)>0:
            print ("此时又验证码")
            lock="F:/python/课程/lianxi/验证码.png"
            urllib.request.urlretrieve(captcha[0],filename=lock)
            print ("请查看验证码并输入验证码")
            captcha_value=input()
            data = {
                "form_email": "15138259738",
                "form_password": "13579zheng",
                "captcha-solution": captcha_value,
                "redir": "https://www.douban.com/people/145403553/",
            }
        else:
            print ("此时没有验证码")
            data={"form_email":"15138259738",
                  "form_password":"13579zheng",
                  "redir":"https://www.douban.com/people/145403553/"}
        print ("登入中----")
        return[FormRequest.from_response(response,
                                               meta={"cookiejar":response.meta["cookiejar"] },
                                               headers=self.header,
                                               formdata=data,
                                               callback=self.next
                                               )]
    def next(self, response):
        print("此时已经登陆完成并爬取了个人中心的数据")
        title = response.xpath("/html/head/title/text()").extract()
        print(title[0])

