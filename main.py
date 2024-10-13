import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random

# 邮箱设置
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"  # 替换为你的Gmail邮箱
sender_password = "your_app_password"  # 替换为你的应用专用密码
receiver_email = "xxxxxxxx@txt.voice.google.com"  # 替换为接收者的邮箱地址

def generate_random_chinese(length):
    return ''.join(chr(random.randint(0x4e00, 0x9fff)) for _ in range(length))

subject = "Google Voice 保号短信"
body = "此短信为自动保号Google Voice所用的自动发送短信，后方中文乱码为规避风控所用，请勿理会。" + generate_random_chinese(32)
message = MIMEText(body, 'plain', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['From'] = sender_email
message['To'] = receiver_email

server = None
try:
    print("正在连接到SMTP服务器...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    
    print("正在登录...")
    server.login(sender_email, sender_password)
    
    print("正在发送邮件...")
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("邮件发送成功！")

except smtplib.SMTPConnectError as e:
    print(f"连接SMTP服务器失败：{e}")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP认证失败：{e}")
except smtplib.SMTPException as e:
    print(f"SMTP错误：{e}")
except Exception as e:
    print(f"发生未知错误：{e}")

finally:
    # 关闭连接
    if server:
        print("正在关闭连接...")
        server.quit()
    else:
        print("未能建立SMTP连接")