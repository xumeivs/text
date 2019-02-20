import requests
from json import loads
import re
from collections import deque,OrderedDict
import pandas
from urllib import parse
class buy12306():
    def __init__(self,seat_class):
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        self.s=requests.session()
        self.seat_class=seat_class
    def chick(self):
        #seat_class='动卧'
        #seat_class=input('请输入要乘坐座位类型,硬座，硬卧，无座，软卧，特等座，一等座，二等座，动卧\n')
        time='2019-01-21'
        start='BJP'
        end='SHH'
        url='https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(time,start,end)
        data=self.s.get(url,headers=self.headers,verify=False)
        neirong=loads(data.content)
        #add=neirong['data']
        #result=add['result']
        #self.chickticket(neirong)
    #def chickticket(self,neirong):
        result=dict(neirong)
        if result.get('data').get('map'):
            train_info = result.get('data').get('result')
    #print(train_info)
            train_list=deque()
            for item in train_info:
                split_item=item.split('|')
                item_dict={}
                for item,index in enumerate(split_item,start=0):
    #print('{}:\t{}'.format(index, item))
                    if split_item[11] == 'Y': # 已经开始卖票了
                        item_dict['secretStr']=split_item[0]
                        item_dict['车次名'] = split_item[3]
                        #item_dict['出发地点']=map[split_item[6]]
                        item_dict['发车时间'] = split_item[8] # 出发时间
                        item_dict['到站时间'] = split_item[9] # 到站时间
                        item_dict['历经时间'] = split_item[10] # 经历时长
                        item_dict['硬座'] = split_item[29] # 无座
                        item_dict['硬卧'] = split_item[28] # 硬座
                        item_dict['无座'] = split_item[26] # 硬卧
                        item_dict['软卧'] = split_item[23] # 软卧
                        item_dict['特等座'] = split_item[32] # 特等座
                        item_dict['一等座'] = split_item[31] # 一等座
                        item_dict['二等座'] = split_item[30] # 二等座
                        item_dict['动卧'] = split_item[33] # 动卧
                        train_list.append(item_dict)
                        #print(train_list)
                    elif split_item[0]=='':
                        print('_query_train_info():车次{}的票暂时不能购买'.format(split_item[3]))
                    else:
                        print('_query_train_info():车次{}的票还未开卖，起售时间为：{}'.format(split_item[3],split_item[1]))
                    break
        self.xxx(train_info,train_list,start,end)
    def xxx(self,train_info,train_list,start,end):
        try:
            print('从{}到{}还有余票的列车有：'.format(start,end))
            for item in train_list:
            #print(item['车次名'])
                if 'G'in item['车次名']:
                    print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t特等座:{:4s}\t一等座:{:4s}\t二等座:{:4s}'.format(item['车次名'],item['发车时间'],item['到站时间'],item['历经时间'],item['特等座'],item['一等座'],item['二等座']))
                elif 'D' in item['车次名']:
                    print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t一等座:{:4s}\t二等座:{:4s}\t软卧:{:4s}\t动卧:{:4s}'.format(item['车次名'],item['发车时间'],item['到站时间'],item['历经时间'],item['一等座'],item['二等座'],item['软卧'],item['动卧']))
                else:
                    print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t软卧:{:4s}\t硬卧:{:4s}\t硬座:{:4s}\t无座:{:4s}'.format(item['车次名'],item['发车时间'],item['到站时间'],item['历经时间'],item['软卧'],item['硬卧'],item['硬座'],item['无座']))
        except Exception as e:
                print(e)
        self.xuanpiao(train_list,start,end)
    def xuanpiao(self,train_list,start,end):
        print('正在查询')
        seat_class=self.seat_class
        i=0
        for item in train_list:
            if item[seat_class] == '有' or item[seat_class].isdigit():
                print('查询到{}到{}列车,车次为{},座位类型为{}还有余票'.format(start,end,item['车次名'],seat_class))
                #print(item['secretStr'])
                #print(item['车次名'])
                self.queding(item)
                return
    def queding(self,item):
        datae = {
            '_json_att': ''

        }
        urlo = 'https://kyfw.12306.cn/otn/login/checkUser'
        res = self.s.post(url=urlo, data=datae, headers=self.headers, verify=False)
        res = loads(res.content)
        print(res['data'])
        dataa = {
            'secretStr': parse.unquote(item['secretStr']),
            'train_date': '2018-12-25',
            'back_train_date': "2018-12-26",
            'tour_flag': 'dc',
            'purpose_codes': 'ADULT',
            'query_from_station_name': '北京',
            'query_to_station_name': '上海',
            'undefined': ''
        }
        print('正在运行')
        urle = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
        results = self.s.post(url=urle, data=dataa, headers=self.headers, verify=False)
        results = loads(results.content)
        result = dict(results)
        if results['status']:
            print('系统提交订单成功')
if __name__ =="__main__":
    chicktick=buy12306('硬座')
    piao=chicktick.chick()
    
        
