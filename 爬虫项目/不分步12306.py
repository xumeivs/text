import  requests
from PIL import Image
from json import loads
from collections import deque,OrderedDict
from urllib import parse
s=requests.session()
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
yanzhengurl='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
response=s.get(url=yanzhengurl,headers=headers,verify=False)
with open ("img.jpg","wb") as f:
    f.write(response.content)
try:
    im=Image.open("img.jpg")
    im.show()
    im.close()
except:
    print('请输入验证码')
solution=str(input('请输入验证码位置'))
solit=solution.split(',')
yansol=['36,45','109,44','184,42','254,45','40,113','115,111','186,112','261,111']
yanlist=[]
for item in solit:
    print(item)
    yanlist.append(yansol[int(item)])
yanstr=','.join(yanlist)
checkurl='https://kyfw.12306.cn/passport/captcha/captcha-check'
data={
            'answer': yanstr,
            'login_site':'E',
            'rand':'sjrand'
        }
cont=s.post(url=checkurl,headers=headers,verify=False)
dic=loads(cont.content)
if dic['result_code']=='4':
            print('验证码通过')
            username='15138259738'
            passwd='13579zheng'
            loginurl = 'https://kyfw.12306.cn/passport/web/login'
            datan = {
                'username': username,
                'password': passwd,
                'appid': 'otn'
            }
            result=s.post(url=loginurl,headers=headers,verify=False)
            nnn=loads(result.content)
            if nnn['result_code'] == 0:
                print('登入成功啦')
                start='BJP'
                end='SHH'
                time='2018-12-26'
                buyurl = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
                str(time), str(start), str(end))
                resultn=s.get(url=buyurl,headers=headers,verify=False)
                resultn=loads(resultn.content)
                resultn=dict(resultn)
                if resultn.get('data').get('map'):
                    train_info=resultn.get('data').get('result')
                    train_list=deque()
                    map=resultn['data']['map']
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
                                train_list.append(item_dict)
                            elif split_item[0] == '':
                                print('_query_train_info():车次{}的票暂时不能购买'.format(split_item[3]))
                            else:
                                print('_query_train_info():车次{}的票还未开卖，起售时间为：{}'.format(split_item[3], split_item[1]))
                            break
                    # if not train_list:
                    #     print('无改车次信息')
                    #
                    print('从{}到{}还有余票的列车有：'.format(start, end))
                    for item in train_list:
                        if 'G' in item['车次名']:
                            print('车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t特等座:{:4s}\t一等座:{:4s}\t二等座:{:4s}'.format(
                                item['车次名'], item['发车时间'], item['到站时间'], item['历经时间'], item['特等座'], item['一等座'],
                                item['二等座']))
                        elif 'D' in item['车次名']:
                            print(
                                '车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t一等座:{:4s}\t二等座:{:4s}\t软卧:{:4s}\t动卧:{:4s}'.format(
                                    item['车次名'], item['发车时间'], item['到站时间'], item['历经时间'], item['一等座'], item['二等座'],
                                    item['软卧'], item['动卧']))
                        else:
                            print(
                                '车次:{:4s}\t起始时间:{:4s}\t到站时间:{:4s}\t时长:{:4s}\t软卧:{:4s}\t硬卧:{:4s}\t硬座:{:4s}\t无座:{:4s}'.format(
                                    item['车次名'], item['发车时间'], item['到站时间'], item['历经时间'], item['软卧'], item['硬卧'],
                                    item['硬座'], item['无座']))


        #     else:
        #         print(nnn['result_message'])
        # else:
        #     print('验证码验证失败')


