import requests
import time
from PIL import Image
from json import loads
from collections import deque,OrderedDict
from urllib import parse
import re
s=requests.Session()
class Login123006(object):
    #session=UUU.getsession()
    def __init__(self,seat_class):
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        #self.cookies=requests.cookies.RequestsCookieJar()
        #self.s=requests.Session()
        self.seat_class=seat_class
        self.username='郑威'
    def getimg(self):
        url="https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
        response=s.get(url,headers=self.headers,verify=False)
        #self.cookies.update(response.cookies)
        with open("img.jpg",'wb') as f:
            f.write(response.content)
        try:
            im=Image.open('img.jpg')
            im.show()
            im.close()
        except:
            print('请输入验证码')
        captcha_solution = str(input('请输入验证码位置'))
        #return captcha_solution
        self.check(captcha_solution)

    def check(self,solution):
        #分割输入的验证码位置
        solist=solution.split(',')
        #大概坐标
        yansol=['36,45','109,44','184,42','254,45','40,113','115,111','186,112','261,111']
        yanlist=[]
        for item in solist:
            print (item)
            yanlist.append(yansol[int(item)])
        yanstr=','.join(yanlist)
        checkurl='https://kyfw.12306.cn/passport/captcha/captcha-check'
        #未抓包到信息 网上找的解决方案
        data={
            'answer': yanstr,
            'login_site':'E',
            'rand':'sjrand'
        }
        #发送验证码
        cont=s.post(url=checkurl,data=data,headers=self.headers,verify=False)
        #self.cookies.update(cont.cookies)
        #返回json格式字符串,用json模块解析
        dic=loads(cont.content)
        #code=dic['result_code']
        #4--成功,5--验证失败,7--验证吗过期
        if dic['result_code']=='4':
            print('验证码通过')
        else:
            print('验证码验证失败')
        self.loginto()
    def loginto(self):
        #username=input('想登入就输入你的账户:')
        username='15138259738'
        #passwd=input('输入你的密码:')
        passwd='13579zheng'
        #登入网址需要找
        loginurl='https://kyfw.12306.cn/passport/web/login'
        data={
            'username':username,
            'password':passwd,
            'appid':'otn'
        }
        result=s.post(url=loginurl,data=data,headers=self.headers,verify=False)
        #self.cookies.update(result.cookies)
        dic=loads(result.content)
        #print(result.content)
        #mes=dic['result_code']
        if dic['result_code'] ==0:
            print('登入成功啦')

        #else:
            #print(dic['result_message'])
        #self.checktick()
            yzdata={
                'appid':'otn'
            }
            yzurl1='https://kyfw.12306.cn/passport/web/auth/uamtk'
            yzrespon=s.post(yzurl1,data=yzdata,headers=self.headers,verify=False)
            print('第一次验证')
            dic1=loads(yzrespon.content)
            print(dic1['result_message'])
            yzdata2={
                'tk':dic1['newapptk']
            }
            yzurl2='https://kyfw.12306.cn/otn/uamauthclient'
            yzrespon2=s.post(yzurl2,data=yzdata2,headers=self.headers,verify=False)
            print('第二次验证')
            dic2=loads(yzrespon2.content)
            user=dic2['username']
            print(user,dic2['result_message'])
            self.checktick()
        else:
            print('登入失败')

    def checktick(self):
        #buyurl='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'
        #start=input('请输入起始站:')
        start='BJP'
        #end=input('请输入终点站:')
        end='SHH'
        #time=input('请输入乘车日期:(格式为xxxx-xx-xx)')
        time='2019-01-22'
        #data={
        #data= 'leftTicketDTO.train_date={}&'\
              #'leftTicketDTO.from_station={}&'\
             # 'leftTicketDTO.to_station={}&'\
             # 'purpose_codes=ADULT'\
        #.format(time,start,end)
       # }
        buyurl='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(time,start,end)
        result=s.get(url=buyurl,headers=self.headers,verify=False)
        #self.cookies.update(result.cookies)
        #print(result.cookies)
        result=loads(result.content)
        result=dict(result)
        if result.get('data').get('map'):
            train_info=result.get('data').get('result')
            train_list=deque()#双向队列
            map=result['data']['map']
            for item in train_info:
                split_item=item.split('|')
                item_dict={}
                for index,item in enumerate(split_item,0):
                    if split_item[11] =='Y':#判断是否可以狗屁票
                        item_dict['secretStr']=split_item[0]
                        item_dict['出发地点']=map[split_item[6]]
                        item_dict['抵达地点']=map[split_item[7]]
                        item_dict['车次名']=split_item[3]
                        item_dict['发车时间']=split_item[8]
                        item_dict['到站时间']=split_item[9]
                        item_dict['历经时间']=split_item[10]
                        item_dict['硬座']=split_item[29]
                        item_dict['硬卧']=split_item[28]
                        item_dict['无座']=split_item[26]
                        item_dict['软卧']=split_item[23]
                        item_dict['特等座']=split_item[32]
                        item_dict['一等座']=split_item[31]
                        item_dict['二等座']=split_item[30]
                        item_dict['动卧']=split_item[33]
                    #item_dict['判断车票是否剩余']=split_item[0]
                        train_list.append(item_dict)
                    elif split_item[0]=='':
                        print('_query_train_info():车次{}的票暂时不能购买'.format(split_item[3]))
                    else:
                        print('_query_train_info():车次{}的票还未开卖，起售时间为：{}'.format(split_item[3],split_item[1]))
                    break
                #调用方法函数打印车票信息
        #try:
            self._print_train(train_info, start, end, train_list)
        #except Exception as e:
           # print('无{}到{}车次信息，请重新选择路线'.format(str(start),str(end)))
    def _print_train(self,train_info,start,end,train_list):
        if not train_list:
            print('车次信息为空')
            return
        print('从{}到{}还有余票的列车有：'.format(start,end))
        for item in train_list:
            if 'G'in item['车次名']:
                print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t特等座:{:4s}\t一等座:{:4s}\t二等座:{:4s}'.format(item['车次名'],item['发车时间'],item['到站时间'],item['历经时间'],item['特等座'],item['一等座'],item['二等座']))
            elif 'D' in item['车次名']:
                print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t一等座:{:4s}\t二等座:{:4s}\t软卧:{:4s}\t动卧:{:4s}'.format(item['车次名'],item['发车时间'],item['到站时间'],item['历经时间'],item['一等座'],item['二等座'],item['软卧'],item['动卧']))
            else:
                print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t软卧:{:4s}\t硬卧:{:4s}\t硬座:{:4s}\t无座:{:4s}'.format(item['车次名'],item['发车时间'],item['到站时间'],item['历经时间'],item['软卧'],item['硬卧'],item['硬座'],item['无座']))
        self.xuapiao(train_list,start,end)
    def xuapiao(self,train_list,start,end):
        print('开始购票')
        seat_class=self.seat_class
        i=0
        for item in train_list:
            if item[seat_class] == '有' or item[seat_class].isdigit():
                print('查询到{}到{}列车,车次为{},座位类型为{}还有余票'.format(start,end,item['车次名'],seat_class))
                self.tijiao(item)
                return

            else:

                i+=1
                if i>=len(train_list):
                    print('无余票')
                    #self.checktick()
    def tijiao(self,item):
        #print(item)
        datae = {'_json_att': ''}
        urlo = 'https://kyfw.12306.cn/otn/login/checkUser'
        res = s.post(url=urlo, data=datae, headers=self.headers,verify=False)
        #self.cookies.update(res.cookies)
        res = loads(res.content)
        print(res['data'])
        #time=input('请再输入一遍乘车日期确认：')
        # return
        dataa = {
            'secretStr': parse.unquote(item['secretStr']),
            'train_date':'2019-01-22',
            'back_train_date': "2018-12-27",
            'tour_flag': 'dc',
            'purpose_codes': 'ADULT',
            'query_from_station_name': item['出发地点'],
            'query_to_station_name': item['抵达地点'],
            'undefined': ''
        }
        print(dataa)
        urle = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
        results = s.post(url=urle, data=dataa, headers=self.headers,verify=False)
        #self.cookies.update(results.cookies)
        results = loads(results.content)
        result = dict(results)
        if results['status']:
            print('请确认订单')
        self.buyticket()
    def gettoken(self):
        url='https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        data={
            '_json_att':''
        }
        response=s.post(url,data=data,headers=self.headers,verify=False)
        try:
            pat="var globalRepeatSubmitToken = '(.*?)'"
            pat1="key_check_isChange':'(.*?)'"
            token=re.compile(pat).findall(response.text)
            checkischange=re.compile(pat1).findall(response.text)
            return  token,checkischange
        except:
            print("获取参数失败")
    def buyticket(self):
        url='https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
        token,checkischange=self.gettoken()
        data={
            '_json_att':'',
            'REPEAT_SUBMIT_TOKEN':token
        }
        response=s.post(url,data=data,headers=self.headers,verify=False)
        dic=loads(response.content)
        dic=dict(dic)
        passengers=dic.get('data').get('normal_passengers')
        for passenger in passengers:
            if passenger['passenger_name']==self.username:
                self.checkorder(token,passenger)
                self.getqueuecount(token,checkischange)






if __name__ == "__main__":
    login=Login123006('硬座')
    yan=login.getimg()
    #chek=login.check(yan)
    #login.loginto()
    #login.checktick()