# easyTalk
easyTalk, 一款轻量级简易聊天室

自带服务器、HTML界面。适用于任何系统环境。欢迎改编。

使用方式：

### 第一部分 安装easyTalk依赖的环境
您需要准备：
1.SQL数据库（Windows用户参考[这里](https://docs.microsoft.com/zh-cn/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver15 "这里")，其它系统用户可自行上网查找）；
2.python环境（参考[这里](https://www.runoob.com/python/python-install.html "这里")）；

### 第二部分 下载文件
1.点击“下载ZIP”，得到压缩包。
2.解压。

### 第三部分 配置并运行
1.注意数据库名：
```python
   cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql1="insert into chatroom.chat_msg (name, msg,msg_time) values (%s, %s,%s);"
        cursor.execute(sql1,[name,text,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        conn.commit()
        conn.close()
#另外，你的数据库表格要有
id  #这个会递增 ,name, msg,msg_time
```

2.在当前文件夹打开命令行。
命令：
```shell
python3 index.py
```
然后服务器就会自动运行了。

3.打开网页，自由冲浪！
打开网页，http://localhost:127
即可访问您的聊天室！
默认端口127，
用户如有需要可以在index.py中修改。

---
easyTalk，一个轻量级聊天室。
由A.C.工作室的 AC工作室toby 和 ZH-Y-Q 制作。
联系我们：toby_lai@126.com diyanqi@foxmail.com
采用MIT许可证。原创。:tw-1f1e8-1f1f3:
