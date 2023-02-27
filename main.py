import os
###import pyperclip3
import time
import datetime
import random
#获取日程
f=open("date.ini","r",encoding="UTF-8")
datesss=f.read().split("\n")
datesss.pop()
f.close()
#获取星期文案
f=open("weekday.ini","r",encoding="UTF-8")
weekdaysaying=f.read().split("\n")
weekdaysaying.pop()
f.close()
weekdaysayinglist=[]
for i in range(7):
    weekdaysayinglist.append([])
for i in weekdaysaying:
    i=i.split(" ")
    weekdaysayinglist[int(i[0])].append(i[1])
#获取每日名言
f=open("saying.ini","r",encoding="UTF-8")
saying=f.read().split("\n")
saying.pop()
f.close()
#开始输出
weeklist=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
weekday=datetime.date.today().weekday()
content=time.strftime("xxx摸鱼办提醒您\n今天是%Y年%m月%d日"+weeklist[weekday]+"\n上午好，摸鱼人！\n工作再累，一定不要忘记摸鱼哦，有事没事起身去茶水间，去厕所，去廊道走走别老在工位上坐着，钱是老板的,但命是自己的。\n========", time.localtime())
content = content+"\n今天是"+weeklist[weekday]+"\n"+weekdaysayinglist[weekday][random.randint(0,int(len(weekdaysayinglist[weekday]))-1)]+"\n========\n下面是节日倒计时~~~\n"
for datess in datesss:
    datess = datess.split(" ")
    today=datetime.date.today()
    detla=datetime.date(today.year,int(datess[1]),int(datess[2])).__sub__(datetime.date(today.year,today.month,today.day)).days
    if detla==0:
        content = content + "今天是" + datess[0] + "\n"
    elif detla>0:
        content = content + "距离" + datess[0] + "还有" + str(detla) + "天\n"
    elif detla <0:
        content = content + "距离" + datess[0] + "还有" + str(datetime.date(today.year+1,int(datess[1]),int(datess[2])).__sub__(datetime.date(today.year,today.month,today.day)).days) + "天\n"
content = content + "========\n" + saying[random.randint(0,int(len(saying)-1))] + "\n" + "最后，祝愿天下所有摸鱼人都能愉快的渡过每一天！"
print(content)
##fpyperclip3.copy(content)
