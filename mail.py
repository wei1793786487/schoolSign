
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from mongoutlis import getlist

from_addr='1793786487@qq.com'   #邮件发送账号
to_addrs='1793786487@qq.com'   #接收邮件账号
qqCode=''   #授权码（这个要填自己获取到的）
smtp_server='smtp.qq.com'#固定写死
smtp_port=465#固定端口
message="放假了，不签了，告辞，明年再见"

#配置服务器
stmp=smtplib.SMTP_SSL(smtp_server,smtp_port)
stmp.login(from_addr,qqCode)

def sendQQ(message,user):
    # 组装发送内容
    message = MIMEText(message, 'plain', 'utf-8')  # 发送的内容
    message['From'] = Header("学校签到通知", 'utf-8')  # 发件人
    message['To'] = Header("admin", 'utf-8')  # 收件人
    subject = '签到停止'
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    try:
        stmp.sendmail(from_addr, user, message.as_string())
    except Exception as e:
        print('邮件发送失败--' + str(e))
    print('邮件发送成功')

c = getlist()
for c1 in c:
 sendQQ(message,str(c1.get("qq"))+"@qq.com")