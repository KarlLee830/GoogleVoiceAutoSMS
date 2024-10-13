# Google Voice Auto SMS

本项目为Google Voice保号的Python脚本

可用于青龙面板全自动化保号

# 使用方法

首先使用需要保号的Google Voice收一条短信，此时打开Gmail可以看到关于这条短信的一封邮件

复制这封邮件的发件域名备用

格式为 你的GV号.发送者号码.英文乱码@txt.voice.google.com



然后打开下面的网址生成一个应用专用密码

https://myaccount.google.com/apppasswords



然后在脚本中替换sender_email为你GV号所属的Gmail地址，sender_password为应用专用密码，receiver_email为@txt.voice.google.com结尾的邮件地址



方法参考：https://linux.do/t/topic/99191