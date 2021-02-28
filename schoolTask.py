import datetime
import threading
import time

from apscheduler.schedulers.blocking import BlockingScheduler

from mongoutlis import getlist, add_log

import random
from addSign import add_sign

class MyThread(threading.Thread):
    def __init__(self,lists):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.lists=lists

    def run(self):
        while len(self.lists) != 0:
            # 随机睡眠
            time.sleep(random.randint(0, 600))
            print("=======================")
            # 删除随机索引
            randint = random.randint(0, len(self.lists) - 1)
            print(self.lists[randint])
            one = self.lists[randint]
            # 拿出该索引的数据,签到
            sign_info = add_sign(one.get("id"))
            # 删除随机索引的数据
            del self.lists[randint]
            time1_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            add_log(one.get("name"),sign_info,time1_str)
            print("随机时间{}".format(time1_str))
            print(self.name)
            print(sign_info)
            # sendEmail("学校签到信息",str(sign_info),str(li.get("qq"))+"@qq.com")


def list_split(items, n):
    return [items[i:i+n] for i in range(0, len(items), n)]


def sign():
    split = list_split(list(getlist()), 10)
    for  i in  range(len(split)):
        MyThread(split[i]).start()


sched = BlockingScheduler()
sched.add_job(sign, 'cron', hour=7, minute=30,max_instances=3)
print("sched success run")
time1_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
print(time1_str)
sched.start()




