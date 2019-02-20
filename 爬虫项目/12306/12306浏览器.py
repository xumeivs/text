'''
实现自动抢票，（基于python 3.6+splinter'）
Created in 2018/11/19
'''
from splinter.browser import Browser
from time import sleep
import traceback
from selenium import webdriver
#实现购买的类
class Buy_tickets():
    def __init__(self,uername,passwd,order,passengers,dtime,starts,ends):
        self.username=uername
        self.passwd=passwd
        self.order=order
        self.passengers=passengers
        self.dtime=dtime
        self.starts=starts
        self.ends=ends
        self.login_url='https://kyfw.12306.cn/otn/login/init'
        self.my_url="https://kyfw.12306.cn/otn/view/index.html"
        self.ticket_url="https://kyfw.12306.cn/otn/leftTicket/init"
        self.driver_name="chrome"
        self.executable_path='C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe'
#实现登入
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill('loginUserDTO.user_name',self.username)
        self.driver.fill('userDTO.password',self.passwd)
        print('请输入验证码')
        while True:
            if self.driver.url !=self.my_url:
                sleep(1)
            else:
                break
#买票功能实现
    def start_buy(self):
        self.driver=Browser(driver_name=self.driver_name,executable_path=self.executable_path)
        #self.driver=webdriver.Chrome()
        #窗口大小的操作
        self.driver.driver.set_window_size(1200,700)
        self.login()
        self.driver.visit(self.ticket_url)
        try:
            print('开始买票')
            #加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation":self.starts})
            self.driver.cookies.add({"_jc_save_toStation":self.ends})
            self.driver.cookies.add({"_jc_save_fromDate":self.dtime})
            self.driver.reload()
            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count+=1
                    print('第%d次查询...'%count)
                    try:
                        self.driver.find_by_text('预订')[self.order-1].click()
                        sleep(1.5)
                    except Exception as e:
                        print('预定失败:'+str(e))
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count+=1
                    print('第%d次查询...'%count)
                    try:
                        for i in self.dirver.find_by_text('查询'):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print('预定失败')
                        continue
            print('开始预定')
            sleep(1)
            print('开始选择用户')
            for p in self.passengers:
                self.driver.find_by_text(p).last.click()
                sleep(0.5)
                if p[-1] ==')':
                    self.driver.find_by_id('dialog_xsertcj_ok').click()
                    '''
            print('提交订单')
            self.driver.find_by_id('submitOrder_id').click()
            sleep(2)
            print('确认选座')
            self.driver.find_by_id('dialog_fczk_ok').click()
            print('预定成功')
            '''
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 用户名

    username = '15138259738'

    # 密码

    password = '13579zheng'

    # 车次选择，0代表所有车次

    order = 2

    # 乘客名，比如passengers = ['XXX', 'XXX']

    # 学生票需注明，注明方式为：passengers = ['XXX(学生)', 'XXX']

    passengers = ['郑威']

    # 日期，格式为：'2018-01-20'

    dtime = '2018-11-19'

    # 出发地(需填写cookie值)

    starts = '_%u5317%u4EAC%2CBJP'  # 阜阳

    # 目的地(需填写cookie值)

    ends = '%u4E0A%u6D77%2CSHH'  # 福州

    # xb =['硬座座']

    # pz=['成人票']

    Buy_tickets(username, password, order, passengers, dtime, starts, ends).start_buy()

